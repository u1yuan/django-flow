"""Count distinct eligible electricity prediction targets in local CSV exports.

Inputs are read-only. This tool never imputes missing readings. Run with --help.
The input timestamp is the END of the measured interval, in a single, already
resolved time basis. Convert publisher files to the documented column contract
before running; retain those originals separately.
"""

import argparse
import csv
import json
import math
import statistics
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path


def timestamp(value):
    return datetime.fromisoformat(value.strip().replace("Z", "+00:00"))


def number(value):
    try:
        x = float(value)
    except (ValueError, TypeError):
        return None
    return x if math.isfinite(x) and x >= 0 else None


def read_csv(path):
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        yield from csv.DictReader(handle)


def distribution(counts):
    values = list(counts.values())
    return {"entities": len(values), "min": min(values, default=0),
            "median": statistics.median(values) if values else 0,
            "max": max(values, default=0)}


def ordered_rows(paths):
    """Require globally sorted entity/timestamp input and reject duplicate keys."""
    previous = None
    for path in paths:
        for row in read_csv(path):
            key = (row["entity"], timestamp(row["timestamp"]))
            if previous is not None and key <= previous:
                raise ValueError("input must be globally sorted by entity,timestamp with unique keys")
            previous = key
            yield key, row


def recon(paths):
    days = defaultdict(lambda: defaultdict(int))
    per_entity = defaultdict(int)
    previous = None
    raw = 0
    valid_deltas = 0
    for (entity, end), row in ordered_rows(paths):
        raw += 1
        reading = number(row["cumulative_kwh"])
        if previous and previous[0] == entity:
            _, start, prior = previous
            if reading is not None and prior is not None and end - start == timedelta(minutes=15) and reading >= prior:
                # A midnight end belongs to the preceding 15-minute interval.
                day = (end - timedelta(microseconds=1)).date()
                days[entity][day] += 1
                valid_deltas += 1
        previous = (entity, end, reading)
    complete = {e: {d for d, n in counts.items() if n == 96} for e, counts in days.items()}
    targets = 0
    for e, ds in complete.items():
        per_entity[e] = sum(d - timedelta(days=1) in ds for d in ds)
        targets += per_entity[e]
    return {"mode": "recon-cumulative", "raw_rows": raw, "valid_15_minute_deltas": valid_deltas,
            "complete_household_days": sum(map(len, complete.values())),
            "eligible_next_household_days_with_complete_previous_day": targets,
            "incomplete_observed_household_days": sum(n != 96 for counts in days.values() for n in counts.values()),
            "eligible_targets_per_household": distribution(per_entity)}


def bdg(paths):
    previous = {}
    meters = set()
    per_meter = defaultdict(int)
    rows = 0
    cells = 0
    targets = 0
    invalid_cells = 0
    last_time = None
    for path in paths:
        with Path(path).open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames or "timestamp" not in reader.fieldnames:
                raise ValueError("BDG2 wide CSV requires a timestamp column")
            columns = [c for c in reader.fieldnames if c != "timestamp"]
            for row in reader:
                end = timestamp(row["timestamp"])
                if last_time is not None and end <= last_time:
                    raise ValueError("BDG2 timestamps must be strictly increasing")
                last_time = end
                rows += 1
                for meter in columns:
                    cells += 1
                    value = number(row[meter])
                    if value is None:
                        invalid_cells += 1
                        previous.pop(meter, None)
                        continue
                    meters.add(meter)
                    if meter in previous and end - previous[meter] == timedelta(hours=1):
                        targets += 1
                        per_meter[meter] += 1
                    previous[meter] = end
    return {"mode": "bdg2-electricity-wide", "hour_rows": rows, "meter_cells": cells,
            "meters_with_valid_readings": len(meters), "eligible_next_meter_hours": targets,
            "invalid_or_missing_meter_cells": invalid_cells,
            "eligible_targets_per_meter": distribution({m: per_meter[m] for m in meters})}


def london(paths, prices_path):
    prices = {}
    for row in read_csv(prices_path):
        t = timestamp(row["timestamp"])
        p = number(row["price_p_per_kwh"])
        if t in prices or p is None:
            raise ValueError("price schedule contains duplicate timestamp or invalid price")
        prices[t] = p
    previous = None
    raw = valid_2013 = matched = targets = 0
    households = set()
    per_entity = defaultdict(int)
    for (entity, end), row in ordered_rows(paths):
        raw += 1
        kwh = number(row["kwh"])
        # End timestamps of 2013 intervals: (Jan 1 00:00, Jan 1 2014 00:00].
        in_2013 = datetime(2013, 1, 1, tzinfo=end.tzinfo) < end <= datetime(2014, 1, 1, tzinfo=end.tzinfo)
        current_ok = in_2013 and kwh is not None and end in prices
        if in_2013 and kwh is not None:
            valid_2013 += 1
        if current_ok:
            matched += 1
            households.add(entity)
            if previous and previous[0] == entity and end - previous[1] == timedelta(minutes=30) and previous[2]:
                targets += 1
                per_entity[entity] += 1
        # The prior lag needs observed kWh, not a price. Only the target charge
        # interval must join to the tariff schedule.
        previous = (entity, end, kwh is not None)
    return {"mode": "london-tou", "raw_rows": raw, "valid_2013_kwh_intervals": valid_2013,
            "price_matched_2013_intervals": matched, "eligible_next_half_hours_with_prior_interval": targets,
            "valid_2013_intervals_without_price_match": valid_2013 - matched,
            "eligible_targets_per_household": distribution({e: per_entity[e] for e in households}),
            "price_schedule_intervals": len(prices)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["recon", "bdg2", "london"])
    parser.add_argument("files", nargs="+", help="local, uncompressed CSV files; see data-feasibility.md")
    parser.add_argument("--prices", help="normalized 2013 tariff CSV, required for London")
    args = parser.parse_args()
    if args.mode == "recon":
        result = recon(args.files)
    elif args.mode == "bdg2":
        result = bdg(args.files)
    else:
        if not args.prices:
            parser.error("London requires --prices")
        result = london(args.files, args.prices)
    result["gate_10000_pass"] = result.get("eligible_next_household_days_with_complete_previous_day",
                                           result.get("eligible_next_meter_hours",
                                                      result.get("eligible_next_half_hours_with_prior_interval", 0))) >= 10000
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
