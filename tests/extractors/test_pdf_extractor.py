from pathlib import Path

import pytest

from gentlii_foundations.extractors.pdf import PdfExtractionError, extract_pdf_text


def test_extract_pdf_text_raises_descriptive_error_for_invalid_pdf(tmp_path: Path):
    path = tmp_path / "sample.pdf"
    path.write_bytes(b"%PDF-1.4\n%stub\n")

    with pytest.raises(PdfExtractionError) as exc_info:
        extract_pdf_text(path)

    assert "sample.pdf" in str(exc_info.value)
