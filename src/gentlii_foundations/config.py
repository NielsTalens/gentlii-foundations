from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os


DEFAULT_MODEL = "gpt-5.2"
ENV_FILE = ".env"


@dataclass(frozen=True)
class Settings:
    openai_api_key: str
    model: str = DEFAULT_MODEL


def load_settings(env_path: Path | None = None) -> Settings:
    env_values = _read_dotenv(env_path or Path(ENV_FILE))

    openai_api_key = os.environ.get("OPENAI_API_KEY") or env_values.get("OPENAI_API_KEY", "")
    model = os.environ.get("GENTLII_MODEL") or env_values.get("GENTLII_MODEL") or DEFAULT_MODEL

    return Settings(openai_api_key=openai_api_key, model=model)


def _read_dotenv(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}

    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip("'").strip('"')
    return values
