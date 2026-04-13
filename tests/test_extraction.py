from pathlib import Path

from gentlii_foundations.extraction import extract_documents


def test_extract_documents_returns_one_result_per_supported_file(monkeypatch, tmp_path: Path):
    docx_path = tmp_path / "sample.docx"
    pdf_path = tmp_path / "sample.pdf"
    docx_path.write_text("placeholder")
    pdf_path.write_text("placeholder")

    monkeypatch.setattr("gentlii_foundations.extraction.extract_docx_text", lambda path: f"docx:{path.name}")
    monkeypatch.setattr("gentlii_foundations.extraction.extract_pdf_text", lambda path: f"pdf:{path.name}")

    results = extract_documents([docx_path, pdf_path])

    assert len(results) == 2
    assert results[0].title == "sample.docx"
    assert results[1].title == "sample.pdf"
