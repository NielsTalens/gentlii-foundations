from pathlib import Path

from gentlii_foundations.models import ArtifactName, ExtractedDocument


def test_extracted_document_keeps_source_name():
    doc = ExtractedDocument(path=Path("source.pdf"), title="source.pdf", text="content")
    assert doc.title == "source.pdf"
    assert ArtifactName.STRATEGY.value == "strategy"
