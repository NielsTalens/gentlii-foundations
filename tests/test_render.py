from gentlii_foundations.models import GeneratedArtifact
from gentlii_foundations.render import write_artifacts


def test_write_artifacts_creates_expected_markdown_files(tmp_path):
    artifact = GeneratedArtifact(name="strategy", markdown="# Strategy\n")
    write_artifacts(tmp_path, [artifact])
    assert (tmp_path / "strategy.md").read_text() == "# Strategy\n"
