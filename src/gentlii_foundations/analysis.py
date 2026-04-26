from __future__ import annotations

from gentlii_foundations.models import ArtifactName, ExtractedDocument, GeneratedArtifact
from gentlii_foundations.prompts import build_artifact_prompt


def target_artifacts() -> list[str]:
    return [artifact.value for artifact in ArtifactName]


def generate_artifacts(
    documents: list[ExtractedDocument],
    client,
    report=None,
    artifact_names: list[str] | None = None,
) -> list[GeneratedArtifact]:
    # Keep source titles in the prompt payload so the model can separate evidence by document.
    source_text = "\n\n".join(f"# Source: {document.title}\n{document.text}" for document in documents)
    artifacts: list[GeneratedArtifact] = []
    for artifact_name in artifact_names or target_artifacts():
        if report is not None:
            report(f"Generating artifact: {artifact_name}")
        prompt = build_artifact_prompt(artifact_name, source_text)
        markdown = client.generate_markdown(prompt)
        artifacts.append(GeneratedArtifact(name=artifact_name, markdown=markdown))
    return artifacts
