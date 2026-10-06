"""Fetch public documentation pages for the 2026-10-06 data-feasibility audit.

Saves response bodies only when the server returns a small text or JSON/CSV
payload. Records HTTP failures. Does not follow file types that are rasters,
archives, or polygon downloads.
"""

from __future__ import annotations

import json
import ssl
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
MAX_BYTES = 8_000_000
TIMEOUT = 60
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)

URLS = [
    "https://extranet.who.int/ncdsmicrodata/index.php/catalog/944",
    "https://extranet.who.int/ncdsmicrodata/index.php/catalog/944/study-description",
    "https://extranet.who.int/ncdsmicrodata/index.php/catalog/944/data-dictionary",
    "https://extranet.who.int/ncdsmicrodata/index.php/catalog/944/related-materials",
    "https://extranet.who.int/ncdsmicrodata/index.php/catalog/944/get-microdata",
    "https://www.oecd.org/en/data/datasets/pisa-2022-database.html",
    "https://eogdata.mines.edu/products/vnl/",
    "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/archives/?month=06&type=strengths&year=2026",
    "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/",
    "https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED",
    "https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2",
    "https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC09_C02_T1_L2",
    "https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMSLCFG",
    "https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database",
    "https://www.ncei.noaa.gov/products/land-based-station/global-summary-of-the-day",
    "https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation",
    "https://psa.gov.ph/classification/psgc",
    "https://www.globeatnight.org/",
    "https://www.protectedplanet.net/en/legal",
    "https://bmb.gov.ph/",
    "https://www.bmb.gov.ph/",
]


def slug(url: str) -> str:
    keep = []
    for ch in url:
        if ch.isalnum():
            keep.append(ch.lower())
        else:
            keep.append("-")
    text = "".join(keep).strip("-")
    while "--" in text:
        text = text.replace("--", "-")
    return text[:120]


def main() -> None:
    ctx = ssl.create_default_context()
    log = []
    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for url in URLS:
        entry = {
            "url": url,
            "fetched_at_utc": fetched_at,
            "status": None,
            "final_url": None,
            "content_type": None,
            "bytes": 0,
            "saved_as": None,
            "error": None,
        }
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/json,text/plain,*/*"})
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
                entry["status"] = getattr(resp, "status", None)
                entry["final_url"] = resp.geturl()
                entry["content_type"] = resp.headers.get("Content-Type")
                length_hdr = resp.headers.get("Content-Length")
                if length_hdr and length_hdr.isdigit() and int(length_hdr) > MAX_BYTES:
                    entry["error"] = f"content-length {length_hdr} exceeds cap; body not saved"
                    log.append(entry)
                    print(f"SKIP {entry['status']} {url}")
                    continue
                body = resp.read(MAX_BYTES + 1)
                entry["bytes"] = len(body)
                if len(body) > MAX_BYTES:
                    entry["error"] = "body exceeded cap; not saved"
                    log.append(entry)
                    print(f"CAP {entry['status']} {url}")
                    continue
                ctype = (entry["content_type"] or "").lower()
                if any(tok in ctype for tok in ("zip", "tiff", "geotiff", "octet-stream", "shapefile")):
                    entry["error"] = "blocked file type; body not saved"
                    log.append(entry)
                    print(f"TYPE {entry['status']} {url}")
                    continue
                ext = ".html"
                if "json" in ctype:
                    ext = ".json"
                elif "csv" in ctype or "text/plain" in ctype:
                    ext = ".txt"
                name = slug(url) + ext
                path = OUT / name
                path.write_bytes(body)
                entry["saved_as"] = name
                log.append(entry)
                print(f"OK {entry['status']} {entry['bytes']} {name}")
        except urllib.error.HTTPError as exc:
            entry["status"] = exc.code
            entry["error"] = f"HTTPError {exc.code}: {exc.reason}"
            err_body = exc.read(20000)
            err_name = slug(url) + ".error.txt"
            (OUT / err_name).write_bytes(err_body)
            entry["saved_as"] = err_name
            entry["bytes"] = len(err_body)
            log.append(entry)
            print(f"HTTP {exc.code} {url}")
        except Exception as exc:  # noqa: BLE001 — record access failure
            entry["error"] = f"{type(exc).__name__}: {exc}"
            log.append(entry)
            print(f"ERR {type(exc).__name__} {url}")
    (OUT / "fetch-log.json").write_text(json.dumps(log, indent=2), encoding="utf-8")
    print(f"logged {len(log)} urls")


if __name__ == "__main__":
    main()
