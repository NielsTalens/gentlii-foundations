from __future__ import annotations

from openai import OpenAI


class FoundationsClient:
    def __init__(self, api_key: str, model: str, timeout: float = 60.0) -> None:
        self.model = model
        self._client = OpenAI(api_key=api_key, timeout=timeout)

    def generate_markdown(self, prompt: str) -> str:
        response = self._client.responses.create(
            model=self.model,
            input=prompt,
        )
        return response.output_text.strip()
