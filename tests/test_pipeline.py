from pathlib import Path
from types import SimpleNamespace

from gentlii_foundations.pipeline import build_foundations


def test_build_foundations_runs_pipeline(monkeypatch, tmp_path: Path):
    root = tmp_path / "product-definitions"
    (root / "foundations-input").mkdir(parents=True)
    (root / "product-description").mkdir()

    called = {"rendered": False}

    monkeypatch.setattr("gentlii_foundations.pipeline.write_artifacts", lambda *args, **kwargs: called.__setitem__("rendered", True))
    monkeypatch.setattr("gentlii_foundations.pipeline.discover_source_files", lambda path: [])
    monkeypatch.setattr("gentlii_foundations.pipeline.extract_documents", lambda paths: [])
    monkeypatch.setattr(
        "gentlii_foundations.pipeline.load_settings",
        lambda: SimpleNamespace(openai_api_key="test-key", model="gpt-5.2"),
    )
    monkeypatch.setattr("gentlii_foundations.pipeline.FoundationsClient", lambda api_key, model: object())
    monkeypatch.setattr("gentlii_foundations.pipeline.generate_artifacts", lambda documents, client: [])

    build_foundations(root)

    assert called["rendered"] is True
