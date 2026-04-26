from pathlib import Path
from types import SimpleNamespace

import pytest

from gentlii_foundations.models import ExtractedDocument, GeneratedArtifact
from gentlii_foundations.pipeline import build_foundations, run_product_guard


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
    assert "Generating 4 foundation artifacts with OpenAI." in messages
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


def test_run_product_guard_reads_generated_markdown_and_excludes_guard(monkeypatch, tmp_path: Path):
    root = tmp_path / "product-definitions"
    output_dir = root / "product-description"
    (root / "foundations-input").mkdir(parents=True)
    output_dir.mkdir()
    (output_dir / "strategy.md").write_text("# Strategy\nAligned direction\n", encoding="utf-8")
    (output_dir / "business-case.md").write_text("# Business Case\nEconomic logic\n", encoding="utf-8")
    (output_dir / "product-guard.md").write_text("# Old Guard\nIgnore me\n", encoding="utf-8")

    captured = {"documents": None, "artifact": None, "artifact_names": None}

    monkeypatch.setattr(
        "gentlii_foundations.pipeline.load_settings",
        lambda: SimpleNamespace(openai_api_key="test-key", model="gpt-5.2"),
    )
    monkeypatch.setattr("gentlii_foundations.pipeline.FoundationsClient", lambda api_key, model: object())

    def fake_generate_artifacts(documents, client, report=None, artifact_names=None):
        captured["documents"] = documents
        captured["artifact_names"] = artifact_names
        return [GeneratedArtifact(name="product-guard", markdown="# Product Guard\nAligned\n")]

    monkeypatch.setattr("gentlii_foundations.pipeline.generate_artifacts", fake_generate_artifacts)
    monkeypatch.setattr(
        "gentlii_foundations.pipeline.write_markdown_artifact",
        lambda output_path, artifact: captured.__setitem__("artifact", (output_path, artifact)),
    )

    run_product_guard(root)

    assert [document.title for document in captured["documents"]] == ["strategy", "business-case"]
    assert all(document.path.name != "product-guard.md" for document in captured["documents"])
    assert captured["artifact_names"] == ["product-guard"]
    assert captured["artifact"] == (
        output_dir / "product-guard.md",
        GeneratedArtifact(name="product-guard", markdown="# Product Guard\nAligned\n"),
    )


def test_run_product_guard_reports_progress(monkeypatch, tmp_path: Path):
    root = tmp_path / "product-definitions"
    output_dir = root / "product-description"
    (root / "foundations-input").mkdir(parents=True)
    output_dir.mkdir()
    (output_dir / "strategy.md").write_text("# Strategy\nAligned direction\n", encoding="utf-8")

    messages: list[str] = []

    monkeypatch.setattr(
        "gentlii_foundations.pipeline.load_settings",
        lambda: SimpleNamespace(openai_api_key="test-key", model="gpt-5.2"),
    )
    monkeypatch.setattr("gentlii_foundations.pipeline.FoundationsClient", lambda api_key, model: object())
    monkeypatch.setattr(
        "gentlii_foundations.pipeline.generate_artifacts",
        lambda documents, client, report=None, artifact_names=None: [
            report("Generating artifact: product-guard") if report else None,
        ] and [GeneratedArtifact(name="product-guard", markdown="# Product Guard\nAligned\n")],
    )
    monkeypatch.setattr("gentlii_foundations.pipeline.write_markdown_artifact", lambda output_path, artifact: None)

    run_product_guard(root, report=messages.append)

    assert f"Running product guard from root: {root}" in messages
    assert f"Using output directory: {output_dir}" in messages
    assert "Found 1 generated markdown artifacts for alignment analysis." in messages
    assert "Generating 1 product guard artifact with OpenAI." in messages
    assert "Generating artifact: product-guard" in messages
    assert f"Wrote guard report to {output_dir / 'product-guard.md'}." in messages


def test_run_product_guard_requires_generated_markdown(tmp_path: Path):
    root = tmp_path / "product-definitions"
    (root / "foundations-input").mkdir(parents=True)
    (root / "product-description").mkdir()

    with pytest.raises(ValueError, match="No generated markdown artifacts found"):
        run_product_guard(root)
