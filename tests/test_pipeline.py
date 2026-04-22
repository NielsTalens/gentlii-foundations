from pathlib import Path
from types import SimpleNamespace

from gentlii_foundations.models import GeneratedArtifact
from gentlii_foundations.pipeline import build_foundations


def test_build_foundations_runs_pipeline(monkeypatch, tmp_path: Path):
    root = tmp_path / "product-definitions"
    (root / "foundations-input").mkdir(parents=True)
    (root / "product-description").mkdir()

    captured = {"output_dir": None}

    monkeypatch.setattr(
        "gentlii_foundations.pipeline.write_artifacts",
        lambda output_dir, artifacts: captured.__setitem__("output_dir", output_dir),
    )
    monkeypatch.setattr("gentlii_foundations.pipeline.discover_source_files", lambda path: [])
    monkeypatch.setattr("gentlii_foundations.pipeline.extract_documents", lambda paths: [])
    monkeypatch.setattr(
        "gentlii_foundations.pipeline.load_settings",
        lambda: SimpleNamespace(openai_api_key="test-key", model="gpt-5.2"),
    )
    monkeypatch.setattr("gentlii_foundations.pipeline.FoundationsClient", lambda api_key, model: object())
    monkeypatch.setattr("gentlii_foundations.pipeline.generate_artifacts", lambda documents, client, report=None: [])

    build_foundations(root)

    assert captured["output_dir"] == root / "product-description"


def test_build_foundations_reports_progress(monkeypatch, tmp_path: Path):
    root = tmp_path / "product-definitions"
    (root / "foundations-input").mkdir(parents=True)
    (root / "product-description").mkdir()

    messages: list[str] = []

    monkeypatch.setattr(
        "gentlii_foundations.pipeline.discover_source_files",
        lambda path: [root / "foundations-input" / "a.docx", root / "foundations-input" / "b.pdf"],
    )
    monkeypatch.setattr("gentlii_foundations.pipeline.extract_documents", lambda paths: [])
    monkeypatch.setattr(
        "gentlii_foundations.pipeline.load_settings",
        lambda: SimpleNamespace(openai_api_key="test-key", model="gpt-5.2"),
    )
    monkeypatch.setattr("gentlii_foundations.pipeline.FoundationsClient", lambda api_key, model: object())
    monkeypatch.setattr(
        "gentlii_foundations.pipeline.generate_artifacts",
        lambda documents, client, report=None: [
            report("Generating artifact: strategy") if report else None,
            report("Generating artifact: business-case") if report else None,
        ] and [],
    )
    monkeypatch.setattr("gentlii_foundations.pipeline.write_artifacts", lambda output_dir, artifacts: None)

    build_foundations(root, report=messages.append)

    assert f"Building foundations from root: {root}" in messages
    assert f"Using input directory: {root / 'foundations-input'}" in messages
    assert f"Using output directory: {root / 'product-description'}" in messages
    assert "Found 2 supported source files." in messages
    assert "Extracted 0 source documents." in messages
    assert "Generating 5 foundation artifacts with OpenAI." in messages
    assert "Generating artifact: strategy" in messages
    assert "Generating artifact: business-case" in messages
    assert "Rendering markdown and static site output." in messages
    assert "Wrote 0 artifact files plus index.html and styles.css." in messages


def test_build_foundations_reports_each_artifact_generation(monkeypatch, tmp_path: Path):
    root = tmp_path / "product-definitions"
    (root / "foundations-input").mkdir(parents=True)
    (root / "product-description").mkdir()

    messages: list[str] = []

    monkeypatch.setattr("gentlii_foundations.pipeline.discover_source_files", lambda path: [])
    monkeypatch.setattr("gentlii_foundations.pipeline.extract_documents", lambda paths: [])
    monkeypatch.setattr(
        "gentlii_foundations.pipeline.load_settings",
        lambda: SimpleNamespace(openai_api_key="test-key", model="gpt-5.2"),
    )
    monkeypatch.setattr("gentlii_foundations.pipeline.FoundationsClient", lambda api_key, model: object())

    def fake_generate_artifacts(documents, client, report=None):
        if report is not None:
            report("Generating artifact: strategy")
            report("Generating artifact: business-case")
        return [
            GeneratedArtifact(name="strategy", markdown="# Strategy\n"),
            GeneratedArtifact(name="business-case", markdown="# Business Case\n"),
        ]

    monkeypatch.setattr("gentlii_foundations.pipeline.generate_artifacts", fake_generate_artifacts)
    monkeypatch.setattr("gentlii_foundations.pipeline.write_artifacts", lambda output_dir, artifacts: None)

    build_foundations(root, report=messages.append)

    assert "Generating artifact: strategy" in messages
    assert "Generating artifact: business-case" in messages
    assert "Wrote 2 artifact files plus index.html and styles.css." in messages
