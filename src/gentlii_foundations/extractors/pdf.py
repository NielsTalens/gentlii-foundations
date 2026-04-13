from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader


class PdfExtractionError(ValueError):
    pass


def extract_pdf_text(path: Path) -> str:
    try:
        reader = PdfReader(str(path))
        pages = [page.extract_text().strip() for page in reader.pages if page.extract_text()]
    except Exception as exc:  # pragma: no cover - library error passthrough
        raise PdfExtractionError(f"Failed to extract text from {path.name}") from exc

    text = "\n\n".join(page for page in pages if page)
    if not text:
        raise PdfExtractionError(f"Failed to extract text from {path.name}")
    return text
