"""Second-round public fetches. Records failures. Skips rasters and archives."""

from __future__ import annotations

import json
import ssl
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
MAX_BYTES = 12_000_000
TIMEOUT = 60
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)

URLS = [
    "https://extranet.who.int/ncdsmicrodata/index.php/metadata/export/944/json",
    "https://extranet.who.int/ncdsmicrodata/index.php/catalog/944/download/6666",
    "https://extranet.who.int/ncdsmicrodata/index.php/catalog/944/download/6665",
    "https://eogdata.mines.edu/files/EOG_products_CC_License.pdf",
    "https://eogdata.mines.edu/nighttime_light/monthly/v10/",
    "https://www.globeatnight.org/maps-data/",
    "https://developers.google.com/earth-engine/datasets/catalog/JRC_GHSL_P2023A_GHS_POP",
    "https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_HOURLY",
    "https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD11A1",
    "https://www.ncei.noaa.gov/pub/data/noaa/isd-history.csv",
    "https://www.ncei.noaa.gov/pub/data/noaa/country-list.txt",
    "https://www.ncei.noaa.gov/data/global-summary-of-the-day/doc/readme.txt",
    "https://www.ncei.noaa.gov/support/access-search-service-api-user-documentation",
    "https://webfs.oecd.org/pisa2022/",
    "https://www.oecd-ilibrary.org/education/pisa-2022-results-volume-i_53f23881-en",
    "https://doi.org/10.1787/53f23881-en",
    "https://openstat.psa.gov.ph/",
    "https://elibrary.bmb.gov.ph/",
    "https://www.denr.gov.ph/",
    "https://www.protectedplanet.net/country/PHL",
    "https://www.lightpollutionmap.info/",
]


def slug(url: str) -> str:
    keep = []
    for ch in url:
        keep.append(ch.lower() if ch.isalnum() else "-")
    text = "".join(keep).strip("-")
    while "--" in text:
        text = text.replace("--", "-")
    return text[:140]


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
        req = urllib.request.Request(
            url,
            headers={"User-Agent": UA, "Accept": "*/*"},
        )
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
                entry["status"] = getattr(resp, "status", None)
                entry["final_url"] = resp.geturl()
                entry["content_type"] = resp.headers.get("Content-Type")
                disp = resp.headers.get("Content-Disposition")
                length_hdr = resp.headers.get("Content-Length")
                ctype = (entry["content_type"] or "").lower()
                blocked = any(
                    tok in ctype
                    for tok in ("tiff", "geotiff", "zip", "shapefile", "octet-stream")
                )
                if "content-disposition" and disp and ".tif" in disp.lower():
                    blocked = True
                if length_hdr and length_hdr.isdigit() and int(length_hdr) > MAX_BYTES:
                    entry["error"] = f"content-length {length_hdr} exceeds cap; body not saved"
                    log.append(entry)
                    print("SKIP", entry["status"], url)
                    continue
                if blocked:
                    entry["error"] = "blocked file type; body not saved"
                    log.append(entry)
                    print("TYPE", url, ctype)
                    continue
                body = resp.read(MAX_BYTES + 1)
                entry["bytes"] = len(body)
                if len(body) > MAX_BYTES:
                    entry["error"] = "body exceeded cap; not saved"
                    log.append(entry)
                    print("CAP", url)
                    continue
                ext = ".bin"
                if "pdf" in ctype or body[:4] == b"%PDF":
                    ext = ".pdf"
                elif "json" in ctype or body[:1] in (b"{", b"["):
                    ext = ".json"
                elif "csv" in ctype or url.endswith(".csv"):
                    ext = ".csv"
                elif "html" in ctype or body[:15].lower().startswith(b"<!doctype html") or body[:6].lower().startswith(b"<html"):
                    ext = ".html"
                elif "text" in ctype or url.endswith(".txt"):
                    ext = ".txt"
                name = slug(url) + ext
                (OUT / name).write_bytes(body)
                entry["saved_as"] = name
                log.append(entry)
                print("OK", entry["status"], entry["bytes"], name)
        except urllib.error.HTTPError as exc:
            entry["status"] = exc.code
            entry["error"] = f"HTTPError {exc.code}: {exc.reason}"
            err_body = exc.read(8000)
            err_name = slug(url) + ".error.txt"
            (OUT / err_name).write_bytes(err_body)
            entry["saved_as"] = err_name
            entry["bytes"] = len(err_body)
            log.append(entry)
            print("HTTP", exc.code, url)
        except Exception as exc:  # noqa: BLE001
            entry["error"] = f"{type(exc).__name__}: {exc}"
            log.append(entry)
            print("ERR", type(exc).__name__, url)
    (OUT / "fetch-log-round2.json").write_text(json.dumps(log, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
