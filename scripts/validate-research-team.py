"""Small dependency-free check for the research agent team files."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROLES = ("coordinator", "literature-researcher", "statistical-analyst", "writer", "qa")
SKILLS = (
    "research-coordination",
    "evidence-research",
    "quantitative-analysis",
    "research-writing",
    "research-quality-review",
)


def main() -> None:
    for role in ROLES:
        path = ROOT / ".agents" / "agents" / f"{role}.md"
        assert path.is_file() and path.read_text(encoding="utf-8").strip(), path
    assert (ROOT / ".agents" / "agents" / "README.md").is_file()
    for skill in SKILLS:
        folder = ROOT / ".agents" / "skills" / skill
        manifest = folder / "SKILL.md"
        text = manifest.read_text(encoding="utf-8")
        assert text.startswith("---\n"), manifest
        frontmatter = text.split("---\n", 2)[1]
        assert f"name: {skill}\n" in frontmatter, manifest
        assert "description:" in frontmatter, manifest
        cases = json.loads((folder / "evals" / "evals.json").read_text(encoding="utf-8"))
        assert cases["skill_name"] == skill and len(cases["evals"]) >= 2, skill
    print("Five profiles, usage guide, skills, and evaluation manifests are valid.")


if __name__ == "__main__":
    main()
