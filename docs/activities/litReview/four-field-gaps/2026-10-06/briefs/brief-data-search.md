# Brief — dataset leads for kept gaps

Research question or topic:
For each kept gap in the assigned field, which Philippine or global datasets can a person download in a browser, including free registration, so a later script could count eligible records?

Requested output:
`docs/activities/litReview/four-field-gaps/2026-10-06/dataset-register-<field>.csv`

One header row, then one row per dataset. Columns, in this order:

field,card,dataset_name,official_url,license_text,documented_size,observation_unit,philippine_rows,registration_steps,access_note

Input locations:
- `gap-prescore.md` in this folder, section "What was kept."
- The assigned `gap-candidates-<field>.md` and `title-cards-<field>.md`.
- This brief.

Constraints:
- Search only the cards that `gap-prescore.md` says advance. Do not add a stopped card.
- Find 1 to 3 datasets per kept card. A dataset may be Philippine, multi-country, or global.
- Open the official page. Record license words only from text that opened. If the license page is blocked, write "license page not opened."
- A catalog total is not an eligible-record count. Write it in `documented_size` with the words "catalog figure, not an eligible count."
- Manual browser download, including free account registration, is in scope. Earth Engine, Copernicus accounts, scraping, primary collection, and partner requests are out. An API with a key and no file download is recorded as "API, not a file" and does not count as the card's passing lead.
- Noncommercial licenses are kept and flagged in `access_note`.
- If a page returns 403, 404, or a timeout, record that status. Do not bypass it.
- Do not download the data file. Do not fit a model. Do not commit. Write only your CSV.

Acceptance criteria:
- Every kept card in the field has at least one row, or one row that says no passing file was opened.
- `official_url` is a page opened in this run, or the cell says the page did not open.
- `philippine_rows` is "named on the opened page," "not named on the opened page," or "page did not open."

Data handling restrictions:
No raw files are saved into the repository or into `data/raw/`. Record URLs and the license wording you actually saw.
