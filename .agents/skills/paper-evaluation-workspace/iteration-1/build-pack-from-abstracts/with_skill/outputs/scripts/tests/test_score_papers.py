"""Tests for the bundled scorer. Fixtures named SYNTHETIC_ are invented data only.

    python -B -m unittest discover -s scripts/tests -v
"""

import io
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
SCRIPTS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPTS))

import score_papers as sp  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"
SYN_RUBRIC = FIXTURES / "SYNTHETIC_rubric.csv"
SYN_SCORES = FIXTURES / "SYNTHETIC_scores_two_reviewers.csv"
SYN_INVALID = FIXTURES / "SYNTHETIC_scores_invalid.csv"


def load(rubric_path, scores_path):
    return (
        sp.read_csv_rows(rubric_path, sp.RUBRIC_COLUMNS),
        sp.read_csv_rows(scores_path, sp.SCORE_COLUMNS),
    )


class FixtureLabelling(unittest.TestCase):
    def test_fixtures_are_labelled_synthetic_in_name_and_header(self):
        files = sorted(FIXTURES.glob("*.csv"))
        self.assertTrue(files)
        for f in files:
            self.assertTrue(f.name.startswith("SYNTHETIC_"), f.name)
            first_line = f.read_text(encoding="utf-8").splitlines()[0]
            self.assertTrue(first_line.startswith("# SYNTHETIC"), f.name)


class ValidScores(unittest.TestCase):
    def setUp(self):
        self.rubric, self.scores = load(SYN_RUBRIC, SYN_SCORES)

    def test_synthetic_inputs_validate(self):
        self.assertEqual(sp.validate_rubric(self.rubric), [])
        self.assertEqual(sp.validate_scores(self.rubric, self.scores), [])

    def test_totals_match_hand_computation(self):
        totals = {
            (t["paper_id"], t["reviewer"]): (t["points"], t["max_points"], t["n_na"])
            for t in sp.compute_totals(self.rubric, self.scores)
        }
        self.assertEqual(
            totals,
            {
                ("SYN-P1", "syn-rev1"): ("5", "6", "0"),
                ("SYN-P1", "syn-rev2"): ("5", "6", "0"),
                ("SYN-P2", "syn-rev1"): ("4", "6", "0"),
                ("SYN-P2", "syn-rev2"): ("3", "6", "0"),
                ("SYN-P3", "syn-rev1"): ("2", "6", "0"),
                ("SYN-P3", "syn-rev2"): ("1", "6", "0"),
                ("SYN-P4", "syn-rev1"): ("2", "4", "1"),
                ("SYN-P4", "syn-rev2"): ("2", "4", "1"),
            },
        )

    def test_kappa_matches_hand_computation(self):
        kappas = {k["criterion_id"]: k for k in sp.compute_kappas(self.rubric, self.scores)}
        self.assertEqual(kappas["S01"]["kappa"], "1.0000")
        self.assertEqual(kappas["S02"]["kappa"], "0.6364")
        self.assertEqual(kappas["S02"]["expected_agreement"], "0.3125")
        self.assertEqual(kappas["S03"]["kappa"], "0.5556")
        self.assertEqual({k["n_pairs"] for k in kappas.values()}, {"4"})
        self.assertEqual({k["reviewer_pair"] for k in kappas.values()}, {"syn-rev1|syn-rev2"})

    def test_kappa_undefined_when_one_identical_category(self):
        observed, expected, kappa = sp.cohen_kappa([("1", "1"), ("1", "1"), ("1", "1")])
        self.assertEqual((observed, expected, kappa), (1.0, 1.0, None))

    def test_no_kappa_with_single_reviewer(self):
        single = [s for s in self.scores if s["reviewer"] == "syn-rev1"]
        self.assertEqual(sp.compute_kappas(self.rubric, single), [])

    def test_output_is_deterministic(self):
        def render(rows):
            return sp.render_summary_csv(sp.compute_totals(self.rubric, rows) + sp.compute_kappas(self.rubric, rows))

        self.assertEqual(render(self.scores), render(list(reversed(self.scores))))

    def test_run_returns_zero_and_prints_report(self):
        out = io.StringIO()
        self.assertEqual(sp.run(SYN_RUBRIC, SYN_SCORES, None, out=out), 0)
        self.assertIn("VALIDATION PASSED: 3 criteria, 24 score rows.", out.getvalue())
        self.assertIn("SYN-P4 | syn-rev1 | vsynthetic-0 | 2/4 | scored=2 NA=1", out.getvalue())


class InvalidScores(unittest.TestCase):
    def test_each_error_class_is_reported(self):
        rubric, scores = load(SYN_RUBRIC, SYN_INVALID)
        errors = "\n".join(sp.validate_scores(rubric, scores))
        for expected in (
            "score '3' out of range",
            "missing evidence_location",
            "unknown criterion_id S99",
            "NA not allowed for S02",
            "duplicate score",
            "rubric_version synthetic-9 does not match",
            "NA requires a note",
            "conflicts with 10.0000/synthetic.bad",
            "SYN-BAD/syn-rev2: missing criteria S02,S03",
        ):
            self.assertIn(expected, errors)

    def test_run_returns_one_and_does_not_write_summary(self):
        out = io.StringIO()
        self.assertEqual(sp.run(SYN_RUBRIC, SYN_INVALID, None, out=out), 1)
        self.assertIn("VALIDATION FAILED", out.getvalue())
        self.assertIn("summary not written", out.getvalue())

    def test_bad_header_is_an_input_error(self):
        out = io.StringIO()
        self.assertEqual(sp.run(SYN_SCORES, SYN_SCORES, None, out=out), 2)
        self.assertIn("INPUT ERROR", out.getvalue())


if __name__ == "__main__":
    unittest.main()
