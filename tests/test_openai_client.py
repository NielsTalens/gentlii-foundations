from gentlii_foundations.openai_client import FoundationsClient


def test_foundations_client_requires_api_key():
    client = FoundationsClient(api_key="test-key", model="gpt-5-mini")
    assert client.model == "gpt-5-mini"
