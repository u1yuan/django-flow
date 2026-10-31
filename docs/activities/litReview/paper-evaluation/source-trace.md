# Source trace

Track: shared. Access date for every row: 2026-10-31 (UTC+8).

No PDF or full text is stored in this repository. Full texts were read in memory during the session. Only short quotes (25 words or fewer) with section or page locators appear in this folder.

## Paper A

**Citation (from Crossref metadata and the ACM landing page):** Effendy, V., Suyanto, S., Sabariah, M. K., & Utomo, R. G. (2025). A Quality Assurance Framework for Model Building in Machine Learning Workflow – A Research Plan. In *Proceedings of the 2025 8th International Conference on Software Engineering and Information Management (ICSIM '25)*, pp. 63–67. ACM. https://doi.org/10.1145/3725899.3725909

**Status:** research plan. The paper reports no results, and its framework is not validated.

| URL | Method | Result |
| --- | --- | --- |
| https://api.crossref.org/works/10.1145/3725899.3725909 | HTTP GET | Metadata: four authors with affiliations (Telkom University), pp. 63–67, `published-print` 2025-01-10, `published-online` 2025-07-11 |
| https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3725899.3725909 | HTTP GET | Abstract; open-access status "HYBRID", license "CCBY" |
| https://dl.acm.org/doi/10.1145/3725899.3725909 | Scripted GET | Cloudflare challenge (not full text) |
| https://dl.acm.org/doi/pdf/10.1145/3725899.3725909 | Scripted GET | Cloudflare HTML interstitial (5,790 bytes), not a PDF |
| https://dl.acm.org/doi/full/10.1145/3725899.3725909 | IDE browser, after cookie dialog | **Full text (HTML)**. Labelled "FREE ACCESS". License link on the page: Creative Commons Attribution 4.0 International License. Sections 1–5, Figure 1 caption, acknowledgments, and references were read in this session |

**Access level obtained:** full text (HTML). Publisher page confirms CC BY 4.0.

**Locator limits:**
- The HTML view has no per-page numbers. Locators use section numbers (for example, "§4.2"). Page numbers within 63–67 are [unverified].
- The two date sources disagree. Crossref gives `published-print` 2025-01-10, and the ACM page says "Published: 11 July 2025". The brief's date (2025-01-10) matches the Crossref print date.
- Figure 1 (methodology diagram) was seen only as an image caption. Its contents were not read.
- §2 refers to "Figure 2.1" for CRISP-ML(Q), but the HTML contains only Figure 1. This is a source inconsistency, not an extraction error.

## Paper B

**Citation (from Crossref, DBLP, and the reprint's title page; all three agree):** Remmel, H., Paech, B., Engwer, C., & Bastian, P. (2014). A Case Study on a Quality Assurance Process for a Scientific Framework. *Computing in Science & Engineering, 16*(3), 58–66. https://doi.org/10.1109/MCSE.2014.57

| URL | Method | Result |
| --- | --- | --- |
| https://www.researchgate.net/publication/264590956 | Web fetch | **Abstract only**. Author list on that page is incomplete (first author only) |
| ResearchGate PDF guess `.../links/54d488f00cf246475805ffde/...pdf` | HTTP GET | 404 |
| https://doi.org/10.1109/mcse.2014.57 and https://ieeexplore.ieee.org/document/6834717 | Web fetch / browser | Timeout or 403; no publisher HTML |
| https://www.computer.org/csdl/magazine/cs/2014/03/mcs2014030058/13rRUwInvtD | IDE browser | Paywall / sign-in; no full text |
| https://api.crossref.org/works/10.1109/mcse.2014.57 | HTTP GET | Metadata: four authors (Remmel, Paech, Engwer, Bastian), vol. 16, issue 3, pp. 58–66, May 2014, IEEE |
| https://dblp1.uni-trier.de/rec/journals/cse/RemmelPEB14.txt | Web fetch | Same four authors |
| https://se-paech.ifi.uni-heidelberg.de/people/hanna_remmel.html | Web fetch | Author publication list. Links a download for the 2013 precursor, not this 2014 article |
| https://se-paech.ifi.uni-heidelberg.de/fileadmin/pdf/2014_Remmel__Paech__Engwer__Bastian_A_Case.pdf | HTTP GET with TLS verification **disabled** (server certificate expired). File kept only in OS temp, not in this repo | **Full text (author-posted IEEE reprint)**. 515,176 bytes, SHA-256 `45d3f2dc56b34cf06056f2a5749d37b6514fb3ab911dc02a5fa27a73af1c9c1f`. Text extracted with `pdftotext` in temp and read in this session. Cover notice: posted with permission of the IEEE. Journal pagination 58–66 |

**Access level obtained:** full text (author-posted reprint). Not the IEEE Xplore HTML.

**Locator and extraction limits:**
- Page locators come from the printed journal page numbers in the reprint (`CISE-16-03-Remmel.indd 58` … `66`). They have not been checked against IEEE Xplore [unverified against publisher copy].
- This session re-read the reprint including the page 58 body after the standfirst (Dune context, SPLE rationale, and the case-study objective).
- Source wording noted during reading: "GCM" for the goal-question-metric approach (p. 60); "F_RQ_DS1" on p. 64 where Table 1 uses "F_RQ_DC1".
- The expired certificate means transport authenticity was not verified. Title, authors, volume, issue, and pages match Crossref and DBLP.

## Not used

The precursor paper by the same authors (Remmel et al., SE-CSE 2013, doi:10.1109/SECSE.2013.6615100) was not read. No criterion draws on it, per the brief's restriction to Papers A and B.
