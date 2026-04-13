from pathlib import Path

from docx import Document

from gentlii_foundations.extractors.docx import extract_docx_text


def test_extract_docx_text_reads_paragraphs(tmp_path: Path):
    path = tmp_path / "sample.docx"
    doc = Document()
    doc.add_paragraph("First line")
    doc.add_paragraph("Second line")
    doc.save(path)

    result = extract_docx_text(path)

    assert "First line" in result
    assert "Second line" in result
