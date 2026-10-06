"""Parse the already-saved CPC RONI HTML table. No network calls."""

from __future__ import annotations

import csv
import json
from html.parser import HTMLParser
from pathlib import Path

SRC = Path(__file__).resolve().parent / (
    "https-www-cpc-ncep-noaa-gov-products-analysis-monitoring-enso-roni.html"
)
OUT = Path(__file__).resolve().parent
SEASONS = ["DJF", "JFM", "FMA", "MAM", "AMJ", "MJJ", "JJA", "JAS", "ASO", "SON", "OND", "NDJ"]


class Tables(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tables: list[list[list[str]]] = []
        self._table: list[list[str]] | None = None
        self._row: list[str] | None = None
        self._cell: list[str] | None = None
        self._in_cell = False

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag == "table":
            self._table = []
        elif tag == "tr" and self._table is not None:
            self._row = []
        elif tag in ("td", "th") and self._row is not None:
            self._cell = []
            self._in_cell = True

    def handle_endtag(self, tag: str) -> None:
        if tag in ("td", "th") and self._in_cell and self._row is not None and self._cell is not None:
            self._row.append(" ".join("".join(self._cell).split()))
            self._cell = None
            self._in_cell = False
        elif tag == "tr" and self._table is not None and self._row is not None:
            if any(c.strip() for c in self._row):
                self._table.append(self._row)
            self._row = None
        elif tag in ("tbody", "table") and self._table is not None and self._row is not None:
            # The saved 2026 row omits a closing tr tag.
            if any(c.strip() for c in self._row):
                self._table.append(self._row)
            self._row = None
            if tag == "table":
                self.tables.append(self._table)
                self._table = None
        elif tag == "table" and self._table is not None:
            self.tables.append(self._table)
            self._table = None

    def handle_data(self, data: str) -> None:
        if self._in_cell and self._cell is not None:
            self._cell.append(data)


def main() -> None:
    parser = Tables()
    parser.feed(SRC.read_text(encoding="utf-8", errors="replace"))
    rows = []
    for table in parser.tables:
        for row in table:
            if not row:
                continue
            year_text = row[0].strip()
            if len(year_text) == 4 and year_text.isdigit() and len(row) >= 2:
                values = row[1:]
                rows.append((int(year_text), values))
    # The page repeats header+year blocks. Keep the first occurrence of each year.
    seen = {}
    for year, values in rows:
        if year not in seen:
            seen[year] = values
    records = []
    for year in sorted(seen):
        values = seen[year]
        if len(values) > 12:
            raise SystemExit(f"{year} has {len(values)} season cells: {values}")
        for idx, raw in enumerate(values):
            if raw == "":
                continue
            records.append(
                {
                    "year": year,
                    "season": SEASONS[idx],
                    "season_index": idx,
                    "roni_c": float(raw),
                    "very_strong_ge_2": float(raw) >= 2.0,
                }
            )
    very = [r for r in records if r["very_strong_ge_2"]]
    # Independent episodes: group seasons >= 2.0 that are not separated by a
    # season in the ordered series falling below +0.5 (CPC warm-episode threshold
    # stated on the same page). Seasons are overlapping, so adjacency in this
    # ordered list is the dependence structure.
    episodes = []
    current = []
    below = False
    for rec in records:
        if rec["very_strong_ge_2"]:
            if current and below:
                episodes.append(current)
                current = []
            current.append(rec)
            below = False
        elif current:
            if rec["roni_c"] < 0.5:
                below = True
    if current:
        episodes.append(current)

    csv_path = OUT / "roni-seasons-parsed.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["year", "season", "season_index", "roni_c", "very_strong_ge_2"],
        )
        writer.writeheader()
        writer.writerows(records)

    summary = {
        "source_file": SRC.name,
        "source_url": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/",
        "season_values_parsed": len(records),
        "first": records[0] if records else None,
        "last": records[-1] if records else None,
        "very_strong_seasons": [
            f"{r['year']} {r['season']} {r['roni_c']:.1f}" for r in very
        ],
        "independent_very_strong_episodes": [
            {
                "seasons": [f"{r['year']} {r['season']} {r['roni_c']:.1f}" for r in ep],
                "n_seasons_ge_2": len(ep),
                "peak_c": max(r["roni_c"] for r in ep),
            }
            for ep in episodes
        ],
        "n_independent_very_strong_episodes": len(episodes),
        "years_with_cell_counts": {str(y): len(seen[y]) for y in sorted(seen)},
    }
    (OUT / "roni-very-strong-summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
