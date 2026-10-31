#!/usr/bin/env python3
"""Unittest for score_papers.py using a SYNTHETIC fixture. Stdlib only."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[1]
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import score_papers  # noqa: E402

FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures"
SYNTHETIC_RUBRIC = FIXTURE_DIR / "SYNTHETIC_rubric.csv"
SYNTHETIC_SCORES = FIXTURE_DIR / "SYNTHETIC_scores.csv"
PACK_ROOT = Path(__file__).resolve().parents[2]


class SyntheticFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.rubric = score_papers.index_rubric(score_papers.load_csv(SYNTHETIC_RUBRIC))
        self.rows = score_papers.filter_scores(
            score_papers.load_csv(SYNTHETIC_SCORES), reviewer="ai-draft"
        )
        self.result = score_papers.aggregate(self.rows, self.rubric)

    def test_fixture_files_are_named_synthetic(self) -> None:
        self.assertTrue(SYNTHETIC_RUBRIC.name.startswith("SYNTHETIC_"))
        self.assertTrue(SYNTHETIC_SCORES.name.startswith("SYNTHETIC_"))

    def test_only_ai_draft_reviewer(self) -> None:
        self.assertEqual(self.result["reviewers"], ["ai-draft"])

    def test_synthetic_a_skips_na_and_totals_three(self) -> None:
        paper = self.result["papers"]["SYNTHETIC_A"]
        self.assertEqual(paper["n_scored"], 2)
        self.assertEqual(paper["n_na"], 1)
        self.assertEqual(paper["total"], 3.0)
        self.assertEqual(paper["max_possible"], 4.0)
        self.assertAlmostEqual(paper["mean"], 1.5)

    def test_synthetic_b_totals_four(self) -> None:
        paper = self.result["papers"]["SYNTHETIC_B"]
        self.assertEqual(paper["n_scored"], 3)
        self.assertEqual(paper["n_na"], 0)
        self.assertEqual(paper["total"], 4.0)
        self.assertEqual(paper["max_possible"], 6.0)

    def test_report_contains_plan_disclaimer(self) -> None:
        report = score_papers.render_report(self.result, "ai-draft")
        self.assertIn("Do not call the PLAN framework validated", report)
        self.assertNotIn("PLAN framework is validated", report)
        self.assertNotIn("the PLAN framework was validated", report.lower())

    def test_run_writes_expected_fixture_report(self) -> None:
        report = score_papers.run(SYNTHETIC_RUBRIC, SYNTHETIC_SCORES, "ai-draft")
        self.assertIn("SYNTHETIC_A", report)
        self.assertIn("SYNTHETIC_B", report)
        self.assertIn("abstract-only", report)
        self.assertIn("adapted", report)


class PackScoresTests(unittest.TestCase):
    def setUp(self) -> None:
        self.rubric_path = PACK_ROOT / "rubric.csv"
        self.scores_path = PACK_ROOT / "scores" / "scores.csv"
        self.rubric = score_papers.index_rubric(score_papers.load_csv(self.rubric_path))
        self.rows = score_papers.filter_scores(
            score_papers.load_csv(self.scores_path), reviewer="ai-draft"
        )
        self.result = score_papers.aggregate(self.rows, self.rubric)

    def test_no_full_text_criteria(self) -> None:
        self.assertEqual(self.result["tag_counts"]["full-text"], 0)
        self.assertEqual(self.result["tag_counts"]["abstract-only"], 13)
        self.assertEqual(self.result["tag_counts"]["adapted"], 2)

    def test_single_reviewer_ai_draft(self) -> None:
        reviewers = {(row.get("reviewer") or "").strip() for row in self.rows}
        self.assertEqual(reviewers, {"ai-draft"})

    def test_plan_total_is_sixteen(self) -> None:
        paper = self.result["papers"]["SYNTHETIC_PLAN"]
        self.assertEqual(paper["n_scored"], 15)
        self.assertEqual(paper["total"], 16.0)
        self.assertEqual(paper["by_criterion"]["C07"]["score"], 0.0)

    def test_case_total_is_nineteen(self) -> None:
        paper = self.result["papers"]["SYNTHETIC_CASE"]
        self.assertEqual(paper["n_scored"], 15)
        self.assertEqual(paper["total"], 19.0)
        self.assertEqual(paper["by_criterion"]["C10"]["score"], 2.0)

    def test_plan_report_does_not_claim_validation(self) -> None:
        report = score_papers.run(self.rubric_path, self.scores_path, "ai-draft")
        self.assertIn("Do not call the PLAN framework validated", report)
        self.assertIn("research plan with no results", report)
        banned = [
            "PLAN framework is validated",
            "PLAN framework was validated",
            "validated PLAN framework",
        ]
        lower = report.lower()
        for phrase in banned:
            self.assertNotIn(phrase.lower(), lower)

    def test_main_writes_out_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "run-report.txt"
            code = score_papers.main(
                [
                    "--rubric",
                    str(self.rubric_path),
                    "--scores",
                    str(self.scores_path),
                    "--reviewer",
                    "ai-draft",
                    "--out",
                    str(out),
                ]
            )
            self.assertEqual(code, 0)
            text = out.read_text(encoding="utf-8")
            self.assertIn("SYNTHETIC_PLAN", text)
            self.assertIn("SYNTHETIC_CASE", text)


if __name__ == "__main__":
    unittest.main()
