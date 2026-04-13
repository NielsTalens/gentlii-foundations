from gentlii_foundations.discovery import discover_source_files


def test_discover_source_files_only_returns_pdf_and_docx(tmp_path):
    (tmp_path / "a.docx").write_text("x")
    (tmp_path / "b.pdf").write_text("x")
    (tmp_path / "c.pptx").write_text("x")

    files = discover_source_files(tmp_path)

    assert [path.name for path in files] == ["a.docx", "b.pdf"]
