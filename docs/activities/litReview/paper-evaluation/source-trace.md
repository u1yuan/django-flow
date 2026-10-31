# Source trace

Track: shared. Access date for every row: 2026-10-31 (UTC+8).

No PDF or full text is stored in this repository. Full texts were read in memory during the session. Only short quotes (25 words or fewer) with section or page locators appear in this folder.

## Paper A

**Citation (from Crossref metadata and the ACM landing page):** Effendy, V., Suyanto, S., Sabariah, M. K., & Utomo, R. G. (2025). A Quality Assurance Framework for Model Building in Machine Learning Workflow – A Research Plan. In *Proceedings of the 2025 8th International Conference on Software Engineering and Information Management (ICSIM '25)*, pp. 63–67. ACM. https://doi.org/10.1145/3725899.3725909

**Status:** research plan. The paper reports no results, and its framework is not validated.

| URL | Method | Result |
| --- | --- | --- |
| https://api.crossref.org/works/10.1145/3725899.3725909 | HTTP GET | Metadata: four authors with affiliations (Telkom University), pp. 63–67, `published-print` 2025-01-10, `published-online` 2025-07-11 |
| https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3725899.3725909 | HTTP GET | Abstract; open-access status "HYBRID", license "CCBY" (Semantic Scholar's claim; license not checked on the publisher page [unverified]) |
| https://dl.acm.org/doi/10.1145/3725899.3725909 | Scripted GET | 403 Forbidden (Cloudflare) |
| https://dl.acm.org/doi/pdf/10.1145/3725899.3725909 | Scripted GET | 403 Forbidden |
| https://dl.acm.org/doi/full/10.1145/3725899.3725909 | IDE browser, after Cloudflare check | **Full text (HTML)**. Labelled "FREE ACCESS". Sections 1–5, Figure 1 caption, and references were read |

**Access level obtained:** full text (HTML).

**Locator limits:**
- The HTML view has no per-page numbers. Locators use section numbers (for example, "§4.2"). Page numbers within 63–67 are [unverified].
- The two date sources disagree. Crossref gives `published-print` 2025-01-10, and the ACM page says "Published: 11 July 2025". The brief's date (2025-01-10) matches the Crossref print date.
- Figure 1 (methodology diagram) was seen only as an image caption. Its contents were not read.
- §2 refers to "Figure 2.1" for CRISP-ML(Q), but the HTML contains only Figure 1. This is a source inconsistency, not an extraction error.

## Paper B

**Citation (from Crossref, OpenAlex, Semantic Scholar, and the reprint's title page; all four agree):** Remmel, H., Paech, B., Engwer, C., & Bastian, P. (2014). A Case Study on a Quality Assurance Process for a Scientific Framework. *Computing in Science & Engineering, 16*(3), 58–66. https://doi.org/10.1109/MCSE.2014.57

| URL | Method | Result |
| --- | --- | --- |
| https://www.researchgate.net/publication/264590956 | Web fetch | **Abstract only** |
| ResearchGate "Download full-text PDF" link (`.../links/54d488f00cf246475805ffde/...pdf`) | IDE browser and scripted GET | Blocked: HTTP 429, then a manual "Security check required" page. Not obtained |
| https://api.crossref.org/works?query.bibliographic=... | HTTP GET | Metadata: DOI 10.1109/MCSE.2014.57, four authors, vol. 16, issue 3, pp. 58–66, May 2014, publisher IEEE |
| https://api.openalex.org/works?search=... | HTTP GET | Same four authors; `oa_status` "closed" |
| https://se-paech.ifi.uni-heidelberg.de/people/barbara_paech/publications.html | HTTP GET | Author group's publication list, which links a PDF for this article |
| https://se-paech.ifi.uni-heidelberg.de/fileadmin/pdf/2014_Remmel__Paech__Engwer__Bastian_A_Case.pdf | HTTP GET with TLS verification **disabled** (the server certificate had expired) | **Full text (author-posted IEEE reprint)**. 515,176 bytes, SHA-256 `45d3f2dc56b34cf06056f2a5749d37b6514fb3ab911dc02a5fa27a73af1c9c1f`. Read in memory and not saved |

**Access level obtained:** full text (author-posted reprint). The cover notice says the reprint is "posted here with permission of the IEEE". It keeps the journal pagination (pp. 58–66).

**Locator and extraction limits:**
- Page locators come from the printed journal page numbers in the reprint. They have not been checked against IEEE Xplore [unverified against publisher copy].
- Text was extracted with a standard-library parser. The extraction dropped ligatures ("fi", "fl", "ff", "Th"). Quotes in this folder restore those letters by hand and should be checked against the PDF.
- Page 58: only the title, the author block, the standfirst, and the first sentence of the body were extracted. The rest of the page 58 body text was not read [unverified].
- Source typos noted during reading: "GCM" for the goal question metric approach (p. 60), and "F_RQ_DS1" where Table 1 uses "F_RQ_DC1" (p. 64).
- The authenticity check is limited to matching the title, authors, volume, issue, and pages against Crossref. The expired certificate means transport authenticity was not verified.

## Not used

The precursor paper by the same authors (Remmel et al., SE-CSE 2013, doi:10.1109/SECSE.2013.6615100) was not read. No criterion draws on it, per the brief's restriction to Papers A and B.
