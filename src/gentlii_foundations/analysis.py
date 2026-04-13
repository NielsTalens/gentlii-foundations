from __future__ import annotations

from gentlii_foundations.models import ArtifactName, ExtractedDocument, GeneratedArtifact
from gentlii_foundations.prompts import build_artifact_prompt


def target_artifacts() -> list[str]:
    return [artifact.value for artifact in ArtifactName]


def generate_artifacts(documents: list[ExtractedDocument], client) -> list[GeneratedArtifact]:
    source_text = "\n\n".join(f"# Source: {document.title}\n{document.text}" for document in documents)
    artifacts: list[GeneratedArtifact] = []
    for artifact_name in target_artifacts():
        prompt = build_artifact_prompt(artifact_name, source_text)
        markdown = client.generate_markdown(prompt)
        artifacts.append(GeneratedArtifact(name=artifact_name, markdown=markdown))
    return artifacts
