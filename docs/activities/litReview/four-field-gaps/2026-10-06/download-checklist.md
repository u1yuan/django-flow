# Download checklist

6 October 2026. The combined register is `dataset-register.csv`. This file tells the group which files to place on disk. No file in this list was downloaded into the repository. `data/raw/` is gitignored. A catalog total is not an eligible-record count. Work stops here until these files are on disk.

Read the license clause on the page before saving the file. Noncommercial files are marked. They can support a thesis draft, and they are flagged again when a later step matches a competition.

## Files to download

| Field | Dataset | Page | Account | Exact file | Save to | License clause to read |
| --- | --- | --- | --- | --- | --- | --- |
| Psychology, cards 2 and 3 | Philippines GSHS 2019 | https://extranet.who.int/ncdsmicrodata/index.php/catalog/944 | Accept the get-microdata terms. A Login link is on the page. Accept was not submitted in this run. | PHL2019 national file from that catalog | `data/raw/psychology/gshs-phl2019/` | Noncommercial, not-for-profit public-health use. Aggregated reporting only. Not for investigation of specific individuals. |
| Psychology, card 3 | World Bank income groups | https://datahelpdesk.worldbank.org/knowledgebase/articles/906519-world-bank-country-and-lending-groups | None shown | `CLASS_2026_07_15.xlsx` from https://ddh-openapi.worldbank.org/resources/DR0095333/download | `data/raw/psychology/world-bank-income/` | License page was not opened. |
| Astronomy, cards 1, 2, and 4 | Globe at Night | https://globeatnight.org/maps-data/ | None on the opened page | https://globeatnight.org/documents/1190/GaN2025.csv | `data/raw/astronomy/globe-at-night/` | Creative Commons Attribution 4.0 International. A header request returned HTTP 302. The body was not saved. |
| Astronomy, cards 1, 2, and 4 | VIIRS nighttime lights | https://eogdata.mines.edu/products/vnl/ | Free account with a verified email at https://eogdata.mines.edu/products/register/. Login was not completed. The file index redirected to sign-in. | One annual GeoTIFF from https://eogdata.mines.edu/nighttime_light/annual/v22/ after sign-in | `data/raw/astronomy/viirs-vnl/` | CC BY 4.0, including commercial use, for the VIIRS nighttime lights named on the product page. |
| Meteorology, card 1 | ISD Global Hourly | https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database | None shown | Station CSVs in https://www.ncei.noaa.gov/data/global-hourly/access/2024/ | `data/raw/meteorology/isd-global-hourly/2024/` | The opened metadata page gives a use-liability statement, not a license name. |
| Meteorology, card 1 | GSOD | https://www.ncei.noaa.gov/data/global-summary-of-the-day/doc/readme.txt | None shown | Station CSVs in https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2024/ | `data/raw/meteorology/gsod/2024/` | Non-U.S. locations: the data or any derived product shall not be provided to other users or be used for the re-export of commercial services. |
| Meteorology, card 2 | IBTrACS v04r01 | https://www.ncei.noaa.gov/products/international-best-track-archive | Optional user registration. The CSV links do not require it. | https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r01/access/csv/ibtracs.ALL.list.v04r01.csv | `data/raw/meteorology/ibtracs/` | Cite Gahtan et al. (2024) doi:10.25921/82ty-9e16 and Knapp et al. (2010) doi:10.1175/2009BAMS2755.1. Electronic downloads are described as free in most cases. |
| Meteorology, card 3 | EPA hourly ozone | https://aqs.epa.gov/aqsweb/airdata/download_files.html | None shown | `hourly_44201_2024.zip` linked from that page | `data/raw/meteorology/epa-hourly-ozone/` | The zip page did not state a data license. The EPA disclaimers page discusses noncommercial use of documents. That sentence was not confirmed as the zip-file license. |
| Urban, card 2 | Philippines health facilities | https://data.humdata.org/dataset/hotosm_phl_health_facilities | None. A header check returned HTTP 200. | `hotosm_phl_health_facilities_points_shp.zip` | `data/raw/urban/hotosm-ph-health-facilities/` | Open Database License (ODC-ODbL): attribute, share-alike, and keep open. |
| Urban, card 2 | 2020 population by barangay | https://data.humdata.org/dataset/2020-census-total-population-by-barangay_admin4 | None. A header check returned HTTP 200. | `P-coded 2020 Census Total Popn Brgy_Adm4_New Pcode.xlsx` | `data/raw/urban/psa-barangay-population/` | CC BY 4.0, including commercial use. |
| Urban, card 1 | Ookla speed tiles | https://github.com/teamookla/ookla-open-data/blob/master/README.md | None. The AWS registry page says no AWS account is required. | 2024 Q4 fixed-network shapefile linked under “Download via URL” in that README. A header check of the link named in the register returned Content-Length 248196642 bytes. | `data/raw/urban/ookla-tiles/` | CC BY-NC-SA 4.0. Noncommercial. |

ISD and GSOD are folders of station files. Save the 2024 folder the page lists. Do not treat “more than 20,000 stations” or “over 9000 stations” as an eligible count.

## Do not download for this screen

- TIMSS 2019 Grade 4. The opened user guide and Supplement 3 do not name belonging or bullying items. Psychology card 1 has no passing file. Card 2 does not use TIMSS as its bullying file.
- PISA 2022. https://www.oecd.org/en/data/datasets/pisa-2022-database.html returned HTTP 403.
- OpenAQ. The opened page is an API with a key, not a browser file. Card 3 uses the EPA hourly zip instead.
- SHIPS developmental data. https://rammb2.cira.colostate.edu/research/tropical-cyclones/ships/developmental-data/ did not open.
- UK-AIR Atom feeds are an extra meteorology card 3 lead in the register. The Atom page does not say the feed is hourly. They are not on the required list above.

## After the files are in place

Reply that the folders above are on disk. The next step counts eligible records from those files and does not move or rewrite them.
