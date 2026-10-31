"""Programmatic grader for paper-evaluation skill evals. Standard library only."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RUBRIC_COLS = {
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
}
LEVELS = {"full-text", "abstract-only", "adapted"}


def check(text: str, passed: bool, evidence: str) -> dict:
    return {"text": text, "passed": passed, "evidence": evidence}


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        return raw.decode("utf-16")
    return raw.decode("utf-8", errors="replace")


def grade_build(out: Path) -> list[dict]:
    findings = []
    rubric = out / "rubric.csv"
    if rubric.is_file():
        rows = list(csv.DictReader(rubric.read_text(encoding="utf-8-sig").splitlines()))
        header = set(rows[0].keys()) if rows else set()
        # header from first line if empty rows
        raw_header = rubric.read_text(encoding="utf-8-sig").splitlines()[0].split(",")
        header = set(h.strip() for h in raw_header)
        findings.append(
            check(
                "Output folder contains rubric.csv with the required header columns including support_level",
                RUBRIC_COLS <= header,
                f"header={sorted(header)}",
            )
        )
        levels = {r.get("support_level", "").strip() for r in rows}
        findings.append(
            check(
                "Every rubric support_level is full-text, abstract-only, or adapted",
                bool(rows) and levels <= LEVELS,
                f"levels={sorted(levels)} n={len(rows)}",
            )
        )
        blob = " ".join(
            (r.get("criterion", "") + " " + r.get("guiding_question", "")).lower() for r in rows
        )
        findings.append(
            check(
                "At least one criterion traces to performance reporting or model comparison",
                "compar" in blob or "performance" in blob or "report" in blob,
                blob[:200],
            )
        )
        findings.append(
            check(
                "At least one criterion traces to feasibility and acceptance as separate questions",
                "feasib" in blob and "accept" in blob,
                blob[:200],
            )
        )
    else:
        for t in (
            "Output folder contains rubric.csv with the required header columns including support_level",
            "Every rubric support_level is full-text, abstract-only, or adapted",
            "At least one criterion traces to performance reporting or model comparison",
            "At least one criterion traces to feasibility and acceptance as separate questions",
        ):
            findings.append(check(t, False, f"missing {rubric}"))

    pack_text = ""
    for p in out.rglob("*"):
        if p.suffix.lower() in {".md", ".csv", ".txt"}:
            pack_text += read_text(p).lower() + "\n"
    claims_validated = (
        "framework is validated" in pack_text
        or "framework was validated" in pack_text
        or "guidelines are validated" in pack_text
    )
    findings.append(
        check(
            "The pack does not describe the PLAN paper's framework as validated",
            not claims_validated,
            "scanned pack prose for a positive 'validated' claim",
        )
    )
    pdfs = list(out.rglob("*.pdf"))
    findings.append(check("No PDF file is written in the output folder", not pdfs, str(pdfs)))

    scores = out / "scores" / "scores.csv"
    if not scores.is_file():
        scores = out / "scores.csv"
    if scores.is_file():
        rows = list(csv.DictReader(line for line in scores.read_text(encoding="utf-8-sig").splitlines() if not line.startswith("#")))
        reviewers = {r.get("reviewer", "") for r in rows}
        findings.append(
            check(
                "scores.csv reviewer values are only ai-draft",
                reviewers <= {"ai-draft"} and bool(rows),
                f"reviewers={sorted(reviewers)}",
            )
        )
    else:
        findings.append(check("scores.csv reviewer values are only ai-draft", False, "scores.csv missing"))

    report = out / "run-report.txt"
    summary = out / "scores" / "summary.csv"
    if not summary.is_file():
        summary = out / "summary.csv"
    report_text = read_text(report) if report.is_file() else ""
    ran = "VALIDATION PASSED" in report_text or summary.is_file()
    findings.append(
        check(
            "The scorer or its report is present (summary.csv or a VALIDATION PASSED log)",
            ran,
            f"report={report.is_file()} summary={summary.is_file()}",
        )
    )
    return findings


def grade_kappa(out: Path) -> list[dict]:
    report = out / "run-report.txt"
    summary = out / "summary.csv"
    text = ""
    if report.is_file():
        text += read_text(report)
    if summary.is_file():
        text += "\n" + read_text(summary)
    findings = [
        check("Stdout or a saved report contains VALIDATION PASSED", "VALIDATION PASSED" in text, text[:240]),
        check("The report includes Cohen's kappa for a reviewer pair", "kappa" in text.lower(), text[:240]),
        check(
            "If the shipped two-reviewer fixture was used, S01 kappa is 1.0000 and S02 kappa is 0.6364",
            "1.0000" in text and "0.6364" in text,
            text[:400],
        ),
        check(
            "No reviewer other than syn-rev1 and syn-rev2 is introduced",
            "syn-rev3" not in text and "ai-draft" not in text,
            "scanned report for extra reviewer labels",
        ),
        check("summary.csv is written to the eval outputs folder", summary.is_file(), str(summary)),
    ]
    return findings


def write_grading(run_dir: Path, assertions: list[dict]) -> None:
    passed = sum(1 for a in assertions if a["passed"])
    total = len(assertions)
    payload = {
        "expectations": assertions,
        "summary": {
            "passed": passed,
            "failed": total - passed,
            "total": total,
            "pass_rate": round(passed / total, 4) if total else 0.0,
        },
    }
    text = json.dumps(payload, indent=2) + "\n"
    (run_dir / "grading.json").write_text(text, encoding="utf-8")
    run1 = run_dir / "run-1"
    run1.mkdir(exist_ok=True)
    (run1 / "grading.json").write_text(text, encoding="utf-8")


def main() -> None:
    mapping = {
        "build-pack-from-abstracts": grade_build,
        "score-and-kappa": grade_kappa,
    }
    for eval_name, grader in mapping.items():
        eval_dir = ROOT / eval_name
        for variant in ("with_skill", "without_skill"):
            out = eval_dir / variant / "outputs"
            run_dir = eval_dir / variant
            assertions = grader(out) if out.is_dir() else [check("outputs directory exists", False, str(out))]
            write_grading(run_dir, assertions)
            print(f"{eval_name}/{variant}: {sum(a['passed'] for a in assertions)}/{len(assertions)}")


if __name__ == "__main__":
    main()
