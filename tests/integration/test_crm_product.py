from pathlib import Path
from types import SimpleNamespace

from gentlii_foundations.pipeline import build_foundations


def test_crm_style_folder_build_writes_expected_artifacts(monkeypatch, tmp_path: Path):
    root = tmp_path / "product-definitions"
    input_dir = root / "foundations-input"
    output_dir = root / "product-description"
    input_dir.mkdir(parents=True)
    output_dir.mkdir()

    (input_dir / "notes.docx").write_text("placeholder")
    (input_dir / "research.pdf").write_text("placeholder")

    monkeypatch.setattr("gentlii_foundations.pipeline.discover_source_files", lambda path: sorted(input_dir.iterdir()))
    monkeypatch.setattr(
        "gentlii_foundations.pipeline.extract_documents",
        lambda paths: [
            SimpleNamespace(title="notes.docx", text="Docx content"),
            SimpleNamespace(title="research.pdf", text="Pdf content"),
        ],
    )
    monkeypatch.setattr(
        "gentlii_foundations.pipeline.load_settings",
        lambda: SimpleNamespace(openai_api_key="test-key", model="gpt-5.2"),
    )

    class FakeClient:
        def __init__(self, api_key: str, model: str) -> None:
            self.api_key = api_key
            self.model = model

        def generate_markdown(self, prompt: str) -> str:
            if "product-charter" in prompt:
                return "# Product Charter\n"
            if "product-vision" in prompt:
                return "# Product Vision\n"
            if "business-case" in prompt:
                return "# Business Case\n"
            if "strategy" in prompt:
                return "# Strategy\n"
            return "# JTBD\n"

    monkeypatch.setattr("gentlii_foundations.pipeline.FoundationsClient", FakeClient)

    build_foundations(root)

    assert (output_dir / "strategy.md").read_text() == "# Strategy\n"
    assert (output_dir / "business-case.md").read_text() == "# Business Case\n"
    assert (output_dir / "product-vision.md").read_text() == "# Product Vision\n"
    assert (output_dir / "jtbd.md").read_text() == "# JTBD\n"
    assert (output_dir / "product-charter.md").read_text() == "# Product Charter\n"
