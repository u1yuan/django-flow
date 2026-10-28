"""Tiny synthetic boundary check; does not stand in for publisher-data analysis."""

import csv
import importlib.util
from datetime import datetime, timedelta
from pathlib import Path


HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location("counter", HERE / "data-target-count.py")
counter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(counter)


def write(path, columns, rows):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(columns)
        writer.writerows(rows)


root = HERE
try:
    start = datetime(2013, 1, 1)
    recon = root / "_selfcheck_recon.csv"
    write(recon, ["entity", "timestamp", "cumulative_kwh"],
          [("H1", (start + timedelta(minutes=15 * i)).isoformat(), i) for i in range(193)])
    assert counter.recon([recon])["eligible_next_household_days_with_complete_previous_day"] == 1

    bdg = root / "_selfcheck_bdg.csv"
    write(bdg, ["timestamp", "A", "B"],
          [["2016-01-01T00:00:00", 1, 1], ["2016-01-01T01:00:00", 2, ""],
           ["2016-01-01T02:00:00", 3, 3]])
    assert counter.bdg([bdg])["eligible_next_meter_hours"] == 2

    london = root / "_selfcheck_london.csv"
    prices = root / "_selfcheck_prices.csv"
    times = [f"2013-01-01T00:{minute:02d}:00" for minute in (30,)] + ["2013-01-01T01:00:00", "2013-01-01T01:30:00"]
    write(london, ["entity", "timestamp", "kwh"], [("H1", t, 1) for t in times])
    # First observed lag has no price; both later targets still qualify.
    write(prices, ["timestamp", "price_p_per_kwh"], [(t, 11.76) for t in times[1:]])
    assert counter.london([london], prices)["eligible_next_half_hours_with_prior_interval"] == 2
finally:
    for name in ("_selfcheck_recon.csv", "_selfcheck_bdg.csv", "_selfcheck_london.csv", "_selfcheck_prices.csv"):
        (root / name).unlink(missing_ok=True)

print("synthetic boundary checks passed: RECON=1, BDG2=2, London=2")
