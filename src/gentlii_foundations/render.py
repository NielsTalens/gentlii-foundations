from __future__ import annotations

from pathlib import Path

from gentlii_foundations.models import GeneratedArtifact


def write_artifacts(output_dir: Path, artifacts: list[GeneratedArtifact]) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    for artifact in artifacts:
        (output_path / f"{artifact.name}.md").write_text(artifact.markdown, encoding="utf-8")
