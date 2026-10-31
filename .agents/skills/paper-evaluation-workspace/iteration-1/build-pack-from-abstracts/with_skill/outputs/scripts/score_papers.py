"""Validate paper-evaluation scores against the rubric, then report totals and Cohen's kappa.

Standard library only. Output is deterministic: rows are sorted, numbers use fixed
precision, and nothing depends on time, randomness, or dictionary insertion order.

Usage (from the paper-evaluation folder):
    python -B scripts/score_papers.py [--rubric rubric.csv] [--scores scores/scores.csv]
                                      [--summary scores/summary.csv]

Exit codes: 0 = valid and summary written; 1 = validation failed (summary not written);
2 = input file missing or unreadable header.
"""

from __future__ import annotations

import argparse
import csv
import io
import sys
from collections import Counter
from pathlib import Path

RUBRIC_COLUMNS = [
    "criterion_id",
    "rubric_version",
    "criterion",
    "guiding_question",
    "score_0_anchor",
    "score_1_anchor",
    "score_2_anchor",
    "source_paper",
    "source_location",
    "support_level",
]
SCORE_COLUMNS = [
    "paper_id",
    "doi",
    "reviewer",
    "rubric_version",
    "criterion_id",
    "score",
    "evidence_location",
    "note",
]
SUMMARY_COLUMNS = [
    "section",
    "paper_id",
    "reviewer",
    "rubric_version",
    "criterion_id",
    "points",
    "max_points",
    "n_scored",
    "n_na",
    "reviewer_pair",
    "n_pairs",
    "observed_agreement",
    "expected_agreement",
    "kappa",
    "status",
]
SUPPORT_LEVELS = {"full-text", "abstract-only", "adapted"}
VALID_SCORES = {"0", "1", "2"}
NA = "NA"
NA_MARKER = "NA allowed if"
MAX_PER_CRITERION = 2


class InputError(Exception):
    pass


def read_csv_rows(path: Path, expected_columns: list[str]) -> list[dict[str, str]]:
    """Read a CSV, skipping leading lines that start with '#', and check the header exactly."""
    try:
        text = path.read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise InputError(f"cannot read {path}: {exc}") from exc
    lines = text.splitlines(keepends=True)
    while lines and lines[0].lstrip().startswith("#"):
        lines.pop(0)
    reader = csv.DictReader(io.StringIO("".join(lines)))
    if reader.fieldnames != expected_columns:
        raise InputError(
            f"{path.name}: header must be {','.join(expected_columns)}; got {','.join(reader.fieldnames or [])}"
        )
    rows = []
    for row in reader:
        if None in row:
            raise InputError(f"{path.name} line {reader.line_num}: more fields than header columns")
        rows.append({k: (v or "").strip() for k, v in row.items()})
    return rows


def validate_rubric(rubric_rows: list[dict[str, str]]) -> list[str]:
    errors = []
    seen = set()
    versions = {r["rubric_version"] for r in rubric_rows}
    if len(versions) != 1:
        errors.append(f"rubric: expected exactly one rubric_version, found {sorted(versions)}")
    for i, r in enumerate(rubric_rows, start=2):
        cid = r["criterion_id"]
        if not cid:
            errors.append(f"rubric row {i}: empty criterion_id")
            continue
        if cid in seen:
            errors.append(f"rubric row {i}: duplicate criterion_id {cid}")
        seen.add(cid)
        for col in RUBRIC_COLUMNS:
            if not r[col]:
                errors.append(f"rubric row {i} ({cid}): empty {col}")
        if r["support_level"] and r["support_level"] not in SUPPORT_LEVELS:
            errors.append(f"rubric row {i} ({cid}): support_level '{r['support_level']}' not in {sorted(SUPPORT_LEVELS)}")
    return errors


def validate_scores(rubric_rows: list[dict[str, str]], score_rows: list[dict[str, str]]) -> list[str]:
    errors = []
    rubric = {r["criterion_id"]: r for r in rubric_rows}
    rubric_versions = {r["rubric_version"] for r in rubric_rows}
    seen = set()
    doi_by_paper: dict[str, str] = {}
    criteria_by_sheet: dict[tuple[str, str], set[str]] = {}
    for i, s in enumerate(score_rows, start=2):
        where = f"scores row {i} ({s['paper_id']}/{s['reviewer']}/{s['criterion_id']})"
        for col in ("paper_id", "doi", "reviewer", "rubric_version", "criterion_id", "score"):
            if not s[col]:
                errors.append(f"{where}: empty {col}")
        cid = s["criterion_id"]
        if cid and cid not in rubric:
            errors.append(f"{where}: unknown criterion_id {cid}")
        if s["rubric_version"] and s["rubric_version"] not in rubric_versions:
            errors.append(f"{where}: rubric_version {s['rubric_version']} does not match rubric {sorted(rubric_versions)}")
        score = s["score"]
        if score and score not in VALID_SCORES and score != NA:
            errors.append(f"{where}: score '{score}' out of range (allowed 0, 1, 2, or NA)")
        if score == NA:
            if cid in rubric and NA_MARKER not in rubric[cid]["guiding_question"]:
                errors.append(f"{where}: NA not allowed for {cid}")
            if not s["note"]:
                errors.append(f"{where}: NA requires a note giving the applicability reason")
        if not s["evidence_location"]:
            errors.append(f"{where}: missing evidence_location")
        key = (s["paper_id"], s["reviewer"], cid)
        if key in seen:
            errors.append(f"{where}: duplicate score for this paper, reviewer, and criterion")
        seen.add(key)
        if s["paper_id"] and s["doi"]:
            prior = doi_by_paper.setdefault(s["paper_id"], s["doi"])
            if prior != s["doi"]:
                errors.append(f"{where}: doi {s['doi']} conflicts with {prior} for the same paper_id")
        criteria_by_sheet.setdefault((s["paper_id"], s["reviewer"]), set()).add(cid)
    for (paper_id, reviewer), cids in sorted(criteria_by_sheet.items()):
        missing = sorted(set(rubric) - cids)
        if missing:
            errors.append(f"scores {paper_id}/{reviewer}: missing criteria {','.join(missing)}")
    return errors


def compute_totals(rubric_rows, score_rows) -> list[dict[str, str]]:
    version = rubric_rows[0]["rubric_version"]
    sheets: dict[tuple[str, str], list[str]] = {}
    for s in score_rows:
        sheets.setdefault((s["paper_id"], s["reviewer"]), []).append(s["score"])
    out = []
    for (paper_id, reviewer), scores in sorted(sheets.items()):
        scored = [int(x) for x in scores if x != NA]
        out.append(
            {
                "section": "total",
                "paper_id": paper_id,
                "reviewer": reviewer,
                "rubric_version": version,
                "points": str(sum(scored)),
                "max_points": str(MAX_PER_CRITERION * len(scored)),
                "n_scored": str(len(scored)),
                "n_na": str(len(scores) - len(scored)),
                "status": "ok",
            }
        )
    return out


def cohen_kappa(pairs: list[tuple[str, str]]) -> tuple[float, float, float | None]:
    """Unweighted Cohen's kappa over categorical labels (0, 1, 2, NA each a category).

    Returns (observed, expected, kappa). kappa is None when expected agreement is 1,
    where the statistic is 0/0 and undefined.
    """
    n = len(pairs)
    observed = sum(1 for a, b in pairs if a == b) / n
    count_a = Counter(a for a, _ in pairs)
    count_b = Counter(b for _, b in pairs)
    expected = sum(count_a[c] * count_b[c] for c in set(count_a) | set(count_b)) / (n * n)
    if expected == 1:
        return observed, expected, None
    return observed, expected, (observed - expected) / (1 - expected)


def compute_kappas(rubric_rows, score_rows) -> list[dict[str, str]]:
    version = rubric_rows[0]["rubric_version"]
    by_key = {(s["paper_id"], s["reviewer"], s["criterion_id"]): s["score"] for s in score_rows}
    reviewers_by_paper: dict[str, set[str]] = {}
    for s in score_rows:
        reviewers_by_paper.setdefault(s["paper_id"], set()).add(s["reviewer"])
    reviewer_pairs = set()
    for reviewers in reviewers_by_paper.values():
        ordered = sorted(reviewers)
        for i in range(len(ordered)):
            for j in range(i + 1, len(ordered)):
                reviewer_pairs.add((ordered[i], ordered[j]))
    out = []
    for ra, rb in sorted(reviewer_pairs):
        shared = sorted(p for p, revs in reviewers_by_paper.items() if ra in revs and rb in revs)
        for cid in sorted(r["criterion_id"] for r in rubric_rows):
            pairs = [(by_key[(p, ra, cid)], by_key[(p, rb, cid)]) for p in shared]
            observed, expected, kappa = cohen_kappa(pairs)
            if kappa is None:
                status = "undefined: expected agreement is 1 (both reviewers used one identical category)"
            elif len(pairs) < 2:
                status = "unstable: fewer than 2 shared papers"
            else:
                status = "ok"
            out.append(
                {
                    "section": "kappa",
                    "rubric_version": version,
                    "criterion_id": cid,
                    "reviewer_pair": f"{ra}|{rb}",
                    "n_pairs": str(len(pairs)),
                    "observed_agreement": f"{observed:.4f}",
                    "expected_agreement": f"{expected:.4f}",
                    "kappa": "" if kappa is None else f"{kappa:.4f}",
                    "status": status,
                }
            )
    return out


def render_summary_csv(rows: list[dict[str, str]]) -> str:
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=SUMMARY_COLUMNS, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({col: row.get(col, "") for col in SUMMARY_COLUMNS})
    return buf.getvalue()


def render_report(totals, kappas) -> str:
    lines = ["Per-paper totals (NA criteria excluded from max_points):"]
    for t in totals:
        lines.append(
            f"  {t['paper_id']} | {t['reviewer']} | v{t['rubric_version']} | "
            f"{t['points']}/{t['max_points']} | scored={t['n_scored']} NA={t['n_na']}"
        )
    if kappas:
        lines.append("Cohen's kappa per criterion (unweighted; 0, 1, 2, NA as categories):")
        for k in kappas:
            value = k["kappa"] or "n/a"
            lines.append(
                f"  {k['criterion_id']} | {k['reviewer_pair']} | n={k['n_pairs']} | "
                f"po={k['observed_agreement']} pe={k['expected_agreement']} kappa={value} | {k['status']}"
            )
    else:
        lines.append("Cohen's kappa: not computed (no paper has scores from two reviewers).")
    return "\n".join(lines) + "\n"


def run(rubric_path: Path, scores_path: Path, summary_path: Path | None, out=sys.stdout) -> int:
    try:
        rubric_rows = read_csv_rows(rubric_path, RUBRIC_COLUMNS)
        score_rows = read_csv_rows(scores_path, SCORE_COLUMNS)
    except InputError as exc:
        out.write(f"INPUT ERROR: {exc}\n")
        return 2
    errors = validate_rubric(rubric_rows)
    if not errors:
        errors = validate_scores(rubric_rows, score_rows)
    if not score_rows and not errors:
        errors = ["scores: no score rows"]
    if errors:
        out.write(f"VALIDATION FAILED ({len(errors)} error(s)); summary not written:\n")
        for e in errors:
            out.write(f"  - {e}\n")
        return 1
    totals = compute_totals(rubric_rows, score_rows)
    kappas = compute_kappas(rubric_rows, score_rows)
    out.write(f"VALIDATION PASSED: {len(rubric_rows)} criteria, {len(score_rows)} score rows.\n")
    out.write(render_report(totals, kappas))
    if summary_path is not None:
        summary_path.write_text(render_summary_csv(totals + kappas), encoding="utf-8", newline="")
        out.write(f"Summary written: {summary_path.parent.name}/{summary_path.name}\n")
    return 0


def main(argv: list[str] | None = None) -> int:
    base = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--rubric", type=Path, default=base / "rubric.csv")
    parser.add_argument("--scores", type=Path, default=base / "scores" / "scores.csv")
    parser.add_argument("--summary", type=Path, default=base / "scores" / "summary.csv")
    args = parser.parse_args(argv)
    return run(args.rubric, args.scores, args.summary)


if __name__ == "__main__":
    sys.exit(main())
