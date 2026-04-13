from __future__ import annotations

from pathlib import Path

from docx import Document


def extract_docx_text(path: Path) -> str:
    document = Document(path)
    paragraphs = [paragraph.text.strip() for paragraph in document.paragraphs if paragraph.text.strip()]
    return "\n\n".join(paragraphs)
