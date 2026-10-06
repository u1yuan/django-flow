"""Package the existing research-team paired outputs for skill-creator review."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".agents" / "evals" / "research-team"
WORKSPACE = ROOT / ".research-team-review" / "iteration-1"

OUTPUTS = {
    "evidence-research": ["evidence-with-1.md", "evidence-with-2.md", "evidence-base-1.md", "evidence-base-2.md"],
    "quantitative-analysis": ["quant-with-1.md", "quant-with-2.md", "quant-base-1.md", "quant-base-2.md"],
    "research-writing": ["writing-with-1.md", "writing-with-2.md", "writing-base-1.md", "writing-base-2.md"],
    "research-quality-review": ["qa-with-1.md", "qa-with-2.md", "qa-base-1.md", "qa-base-2.md"],
    "research-coordination": ["coord-with.md", "coord-with-2.md", "coord-base.md", "coord-base-2.md"],
}


def rubric(skill: str, eval_id: int, text: str) -> list[tuple[str, bool, str]]:
    """Apply transparent, task-specific content checks to each saved answer."""
    t = text.casefold()
    has = lambda *terms: any(term.casefold() in t for term in terms)
    lacks = lambda *terms: not any(term.casefold() in t for term in terms)
    if skill == "evidence-research" and eval_id == 0:
        return [
            ("Records source identifiers or URLs", bool(re.search(r"doi|https?://|literature item|source id", t)), "Looked for an identifier, DOI, URL, or source-item reference."),
            ("Does not present log summaries as source-verified passages", has("unverified", "not source-level verification", "not independently verified") and lacks("citation is verified at source level", "log is verified at source level"), "Checked for explicit unverified status and absence of a claim that the log itself verifies the source."),
            ("Names a concrete source-level verification gap", has("verify", "verification", "resolve the doi", "original source"), "Looked for a specific next verification action."),
        ]
    if skill == "evidence-research":
        return [
            ("Separates relevance leads from verified claims", has("unverified") and has("title", "relevance"), "Looked for explicit unverified status and a relevance screen."),
            ("Does not invent citation metadata", has("unverified") and lacks("correct doi is", "verified doi is"), "Checked that citation identity remains unverified rather than repaired by assertion."),
            ("Reports reproducible screening scope", has("scope", "input:", "screening decision") and has("no browsing", "no full-text", "local proposal"), "Looked for named input/scope and an explicit screening boundary."),
        ]
    if skill == "quantitative-analysis" and eval_id == 0:
        return [
            ("States that the required data are missing or unconfirmed", has("no", "not supplied", "not confirmed") and has("data", "sensor export"), "Looked for an explicit absence/unconfirmed statement about sensor data."),
            ("Does not present fabricated statistics", has("cannot be calculated", "no anomaly", "no statistical result", "no test result"), "Looked for a clear limit on calculated results."),
            ("Lists variables, units, and time/grouping requirements", has("timestamp", "time") and has("unit", "ph", "ec") and has("zone"), "Looked for sensor variables/units and time or zone grouping needs."),
        ]
    if skill == "quantitative-analysis":
        return [
            ("Recomputes 12/80 as 15%", has("15%", "0.15"), "Looked for the correct ratio result."),
            ("Flags the supplied code failure", has("exited with code 1", "runtimeerror", "script failure", "fails"), "Looked for explicit failed execution evidence."),
            ("Does not claim successful execution", lacks("ran successfully", "execution succeeded", "script completed successfully"), "Checked for claims of successful execution."),
        ]
    if skill == "research-writing" and eval_id == 0:
        return [
            ("Provides a claim map", has("claim map")),
            ("Marks citations as unverified", has("unverified")),
            ("Avoids inventing empirical results", has("not establish", "not an empirical", "no empirical", "do not establish")),
        ]
    if skill == "research-writing":
        return [
            ("States that observed sensor analysis is absent", has("no sensor", "no observed", "no sensor records", "not confirmed")),
            ("Preserves proposal-stage or conditional status", has("proposed", "proposal", "conditional")),
            ("Lists unresolved inputs", has("unresolved inputs", "partner identity", "data quality", "operator availability")),
        ]
    if skill == "research-quality-review" and eval_id == 0:
        return [
            ("Flags the unverified citation", has("unverified citation", "unverified bibliography", "not verified")),
            ("Recomputes 12/80 as 15%", has("15%", "0.15")),
            ("Provides severity and a correction", has("critical", "major", "severity") and has("correction", "correct", "replace", "revise")),
        ]
    if skill == "research-quality-review":
        return [
            ("Flags missing sensor data", (has("no", "not") and has("sensor", "dataset", "data")) or has("missing data", "without sensor data", "no dataset")),
            ("Flags the failing code", has("exited with code 1", "runtimeerror", "script failed", "code failure")),
            ("Returns a revision/rejection disposition", has("needs revision", "reject", "rejected", "not acceptable", "hold the empirical claim", "result not validated")),
        ]
    if skill == "research-coordination":
        six_fields = [
            ("research question", "topic"), ("requested output", "deliverable"),
            ("input locations", "inputs"), ("constraints",),
            ("acceptance criteria",), ("data handling restrictions", "data handling"),
        ]
        six_ok = all(any(term in t for term in aliases) for aliases in six_fields)
        if eval_id == 0:
            return [
                ("Uses all six required brief fields", six_ok, "Checked for topic/question, output, inputs, constraints, acceptance criteria, and data-handling restrictions."),
                ("Distinguishes proposal claims from observed data", has("proposal", "target") and has("no", "not observed", "not confirmed"), "Looked for explicit distinction between proposal targets and observations."),
                ("States evidence, limitations, and QA status", has("evidence") and has("limit", "limitation") and has("qa status", "qa:"), "Looked for evidence, limitations, and a QA disposition."),
            ]
        return [
            ("Uses all six required brief fields", six_ok, "Checked for topic/question, output, inputs, constraints, acceptance criteria, and data-handling restrictions."),
            ("Does not claim an empirical anomaly result", has("no", "not") and has("data", "anomaly") and has("empirical", "observed", "measured"), "Looked for an explicit boundary on empirical conclusions."),
            ("Reports QA status and unresolved findings", has("qa status", "qa:", "qa disposition") and has("unresolved", "not verified", "limitations"), "Looked for a QA disposition and remaining open issues."),
        ]
    raise ValueError((skill, eval_id))


def main() -> None:
    runs: list[dict] = []
    eval_catalog: list[dict] = []
    for skill, files in OUTPUTS.items():
        manifest = json.loads((ROOT / ".agents" / "skills" / skill / "evals" / "evals.json").read_text(encoding="utf-8"))
        for eval_id, prompt_spec in enumerate(manifest["evals"]):
            eval_name = f"{skill}-{eval_id + 1}"
            eval_dir = WORKSPACE / f"eval-{len(eval_catalog)}-{eval_name}"
            eval_dir.mkdir(parents=True, exist_ok=True)
            metadata = {"eval_id": len(eval_catalog), "eval_name": eval_name, "prompt": prompt_spec["prompt"], "assertions": prompt_spec["assertions"]}
            (eval_dir / "eval_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
            eval_catalog.append({"eval_id": len(eval_catalog), "eval_name": eval_name, "prompt": prompt_spec["prompt"], "assertions": prompt_spec["assertions"]})
            for config, filename in (("with_skill", files[eval_id]), ("without_skill", files[eval_id + 2])):
                run_dir = eval_dir / config
                out_dir = run_dir / "outputs"
                out_dir.mkdir(parents=True, exist_ok=True)
                answer = (SOURCE / filename).read_text(encoding="utf-8", errors="replace")
                (out_dir / "output.md").write_text(answer, encoding="utf-8")
                checked = rubric(skill, eval_id, answer)
                expectations = []
                for index, item in enumerate(checked):
                    text, passed = item[:2]
                    evidence = item[2] if len(item) > 2 else "Checked directly against the saved output text."
                    if len(checked) == len(prompt_spec["assertions"]):
                        text = prompt_spec["assertions"][index]
                    expectations.append({"text": text, "passed": passed, "evidence": evidence})
                passed = sum(item["passed"] for item in expectations)
                total = len(expectations)
                grading = {"expectations": expectations, "summary": {"passed": passed, "failed": total - passed, "total": total, "pass_rate": passed / total if total else 0}}
                (run_dir / "grading.json").write_text(json.dumps(grading, indent=2) + "\n", encoding="utf-8")
                runs.append({"eval_id": len(eval_catalog) - 1, "eval_name": eval_name, "configuration": config, "run_number": 1, "result": {"pass_rate": grading["summary"]["pass_rate"], "passed": passed, "total": total}, "expectations": expectations, "notes": [f"Output source: {filename}", "No original run timing/token metadata was retained; only content assertions are benchmarked."]})

    summary = {}
    for config in ("with_skill", "without_skill"):
        vals = [run["result"]["pass_rate"] for run in runs if run["configuration"] == config]
        avg = sum(vals) / len(vals)
        summary[config] = {"pass_rate": {"mean": avg, "stddev": (sum((v - avg) ** 2 for v in vals) / len(vals)) ** 0.5, "min": min(vals), "max": max(vals)}}
    delta = summary["with_skill"]["pass_rate"]["mean"] - summary["without_skill"]["pass_rate"]["mean"]
    benchmark = {
        "metadata": {"skill_name": "topic-agnostic-research-team", "timestamp": "2026-09-28T00:00:00Z", "evals_run": [e["eval_name"] for e in eval_catalog], "runs_per_configuration": 1},
        "runs": runs,
        "run_summary": {**summary, "delta": {"pass_rate": f"{delta:+.2f}"}},
        "notes": ["Content assertions were graded against the saved outputs; these are deterministic checks with one existing output per condition.", "No run timing or token metadata was available, so cost metrics are omitted.", "Coordinator output 1 is checked against the requested six-field brief; coordinator output 2 includes a delegated brief."]
    }
    (WORKSPACE / "benchmark.json").write_text(json.dumps(benchmark, indent=2) + "\n", encoding="utf-8")
    (WORKSPACE / "benchmark.md").write_text("# Research-team output benchmark\n\n" + "\n".join(f"- {k}: {v['pass_rate']['mean']:.1%} mean expectation pass rate" for k, v in summary.items()) + f"\n- Difference (with minus without): {delta:+.1%}\n\nScores cover content assertions only; existing run timing and token data were not retained.\n", encoding="utf-8")
    (WORKSPACE / "eval_catalog.json").write_text(json.dumps(eval_catalog, indent=2) + "\n", encoding="utf-8")
    print(f"Packaged {len(runs)} outputs across {len(eval_catalog)} prompts into {WORKSPACE}")
    print(f"Mean assertion pass rate: with={summary['with_skill']['pass_rate']['mean']:.1%}; without={summary['without_skill']['pass_rate']['mean']:.1%}")


if __name__ == "__main__":
    main()
