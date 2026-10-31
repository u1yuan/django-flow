#!/usr/bin/env python3
"""Score papers against the abstract-derived rubric. Standard library only."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import OrderedDict
from pathlib import Path

PLAN_DISCLAIMER = (
    "CONSTRAINT: Paper PLAN is a research plan with no results. "
    "Do not call the PLAN framework validated. "
    "Expert validation in PLAN is a planned method only."
)

NA_VALUES = {"", "na", "n/a", "nan", "none", "null"}
TRUE_VALUES = {"1", "true", "yes", "y"}


def pack_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def is_na(row: dict[str, str]) -> bool:
    flag = (row.get("na") or "").strip().lower()
    if flag in TRUE_VALUES:
        return True
    score = (row.get("score") or "").strip().lower()
    return score in NA_VALUES or score == "na"


def parse_score(row: dict[str, str]) -> float | None:
    if is_na(row):
        return None
    raw = (row.get("score") or "").strip()
    try:
        return float(raw)
    except ValueError as exc:
        raise ValueError(
            f"Non-numeric score {raw!r} for {row.get('paper_id')} {row.get('criterion_id')}"
        ) from exc


def index_rubric(rows: list[dict[str, str]]) -> OrderedDict[str, dict[str, str]]:
    indexed: OrderedDict[str, dict[str, str]] = OrderedDict()
    for row in rows:
        cid = (row.get("criterion_id") or "").strip()
        if not cid:
            continue
        indexed[cid] = row
    return indexed


def filter_scores(
    rows: list[dict[str, str]],
    reviewer: str | None = None,
    paper_id: str | None = None,
) -> list[dict[str, str]]:
    out = []
    for row in rows:
        if not (row.get("criterion_id") or "").strip():
            continue
        if reviewer and (row.get("reviewer") or "").strip() != reviewer:
            continue
        if paper_id and (row.get("paper_id") or "").strip() != paper_id:
            continue
        out.append(row)
    return out


def tag_counts(rubric: OrderedDict[str, dict[str, str]]) -> OrderedDict[str, int]:
    counts: OrderedDict[str, int] = OrderedDict(
        [("full-text", 0), ("abstract-only", 0), ("adapted", 0), ("other", 0)]
    )
    for row in rubric.values():
        tag = (row.get("evidence_tag") or "").strip().lower()
        if tag in counts:
            counts[tag] += 1
        else:
            counts["other"] += 1
    return counts


def aggregate(
    scores: list[dict[str, str]],
    rubric: OrderedDict[str, dict[str, str]],
) -> dict:
    papers: OrderedDict[str, dict] = OrderedDict()
    reviewers = []
    for row in scores:
        pid = (row.get("paper_id") or "").strip()
        if not pid:
            continue
        if pid not in papers:
            papers[pid] = {
                "paper_id": pid,
                "title": (row.get("paper_title") or "").strip(),
                "reviewers": [],
                "by_criterion": OrderedDict(),
                "n": 0,
                "n_scored": 0,
                "n_na": 0,
                "total": 0.0,
                "max_possible": 0.0,
                "mean": None,
            }
        rec = papers[pid]
        cid = (row.get("criterion_id") or "").strip()
        reviewer = (row.get("reviewer") or "").strip()
        if reviewer and reviewer not in rec["reviewers"]:
            rec["reviewers"].append(reviewer)
        if reviewer and reviewer not in reviewers:
            reviewers.append(reviewer)
        value = parse_score(row)
        spec = rubric.get(cid, {})
        scale_max = float(spec.get("scale_max") or 2)
        rec["n"] += 1
        rec["by_criterion"][cid] = {
            "score": value,
            "na": value is None,
            "justification": (row.get("justification") or "").strip(),
            "name": spec.get("name") or cid,
            "evidence_tag": spec.get("evidence_tag") or "",
            "scale_max": scale_max,
        }
        if value is None:
            rec["n_na"] += 1
        else:
            rec["n_scored"] += 1
            rec["total"] += value
            rec["max_possible"] += scale_max
    for rec in papers.values():
        if rec["n_scored"]:
            rec["mean"] = rec["total"] / rec["n_scored"]
            rec["pct"] = (
                (rec["total"] / rec["max_possible"] * 100.0)
                if rec["max_possible"]
                else None
            )
        else:
            rec["mean"] = None
            rec["pct"] = None
    return {
        "papers": papers,
        "reviewers": reviewers,
        "tag_counts": tag_counts(rubric),
        "criterion_ids": list(rubric.keys()),
    }


def _fmt_mean(value: float | None) -> str:
    if value is None:
        return "NA"
    return f"{value:.3f}"


def _fmt_pct(value: float | None) -> str:
    if value is None:
        return "NA"
    return f"{value:.1f}%"


def render_report(result: dict, reviewer: str | None) -> str:
    lines: list[str] = []
    lines.append("Paper-evaluation scorer report")
    lines.append("Sources: SYNTHETIC PLAN and SYNTHETIC CASE abstracts only.")
    lines.append("Reviewer filter: " + (reviewer or "(all)"))
    lines.append("Reviewers present: " + (", ".join(result["reviewers"]) or "(none)"))
    lines.append(PLAN_DISCLAIMER)
    lines.append("")
    tags = result["tag_counts"]
    lines.append("Criterion evidence tags:")
    for key, count in tags.items():
        lines.append(f"  {key}: {count}")
    lines.append("")
    papers = result["papers"]
    if not papers:
        lines.append("No score rows matched the filter.")
        return "\n".join(lines) + "\n"
    lines.append("Paper totals")
    lines.append(
        "paper_id\tn_scored\tn_na\ttotal\tmax\tmean\tpct_of_max\ttitle"
    )
    for rec in papers.values():
        lines.append(
            "\t".join(
                [
                    rec["paper_id"],
                    str(rec["n_scored"]),
                    str(rec["n_na"]),
                    f"{rec['total']:.1f}",
                    f"{rec['max_possible']:.1f}",
                    _fmt_mean(rec["mean"]),
                    _fmt_pct(rec["pct"]),
                    rec["title"],
                ]
            )
        )
    lines.append("")
    for rec in papers.values():
        lines.append(f"## {rec['paper_id']}")
        lines.append(f"Title: {rec['title']}")
        lines.append("Reviewers: " + ", ".join(rec["reviewers"]))
        if "PLAN" in rec["paper_id"].upper() or "research plan" in rec["title"].lower():
            lines.append(
                "Note: this paper is a research plan with no results. "
                "Do not call the PLAN framework validated."
            )
        lines.append("criterion_id\ttag\tscore\tname")
        for cid in result["criterion_ids"]:
            cell = rec["by_criterion"].get(cid)
            if not cell:
                lines.append(f"{cid}\t\tMISSING\t")
                continue
            score_txt = "NA" if cell["na"] else f"{cell['score']:.0f}"
            lines.append(
                f"{cid}\t{cell['evidence_tag']}\t{score_txt}\t{cell['name']}"
            )
        lines.append("")
    lines.append("End of report. One reviewer (ai-draft) unless a later human review is added.")
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Aggregate paper-evaluation scores (stdlib only)."
    )
    parser.add_argument("--pack-root", type=Path, default=None)
    parser.add_argument("--rubric", type=Path, default=None)
    parser.add_argument("--scores", type=Path, default=None)
    parser.add_argument("--reviewer", default="ai-draft")
    parser.add_argument("--out", type=Path, default=None)
    return parser


def resolve_paths(args: argparse.Namespace) -> tuple[Path, Path, Path]:
    root = args.pack_root or pack_root_from_script()
    rubric = args.rubric or (root / "rubric.csv")
    scores = args.scores or (root / "scores" / "scores.csv")
    return root, rubric, scores


def run(
    rubric_path: Path,
    scores_path: Path,
    reviewer: str | None,
) -> str:
    rubric = index_rubric(load_csv(rubric_path))
    if not rubric:
        raise ValueError(f"No criteria in {rubric_path}")
    rows = filter_scores(load_csv(scores_path), reviewer=reviewer or None)
    result = aggregate(rows, rubric)
    return render_report(result, reviewer)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    _, rubric_path, scores_path = resolve_paths(args)
    reviewer = args.reviewer
    if reviewer.lower() in {"all", "*"}:
        reviewer = None
    report = run(rubric_path, scores_path, reviewer)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(report, encoding="utf-8")
    sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
