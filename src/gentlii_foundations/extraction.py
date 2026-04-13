from __future__ import annotations

from pathlib import Path

from gentlii_foundations.extractors.docx import extract_docx_text
from gentlii_foundations.extractors.pdf import extract_pdf_text
from gentlii_foundations.models import ExtractedDocument


def extract_documents(paths: list[Path]) -> list[ExtractedDocument]:
    documents: list[ExtractedDocument] = []
    for path in paths:
        if path.suffix.lower() == ".docx":
            text = extract_docx_text(path)
        elif path.suffix.lower() == ".pdf":
            text = extract_pdf_text(path)
        else:
            continue
        documents.append(ExtractedDocument(path=path, title=path.name, text=text))
    return documents
