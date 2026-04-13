from gentlii_foundations.config import load_settings


def test_load_settings_reads_openai_api_key(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    settings = load_settings()
    assert settings.openai_api_key == "test-key"
