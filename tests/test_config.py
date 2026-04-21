from gentlii_foundations.config import load_settings


def test_load_settings_reads_openai_api_key(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    settings = load_settings()
    assert settings.openai_api_key == "test-key"


def test_load_settings_requires_openai_api_key(monkeypatch, tmp_path):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    try:
        load_settings(tmp_path / ".env")
    except ValueError as exc:
        assert str(exc) == "OPENAI_API_KEY is required"
    else:
        raise AssertionError("expected missing OPENAI_API_KEY to raise ValueError")
