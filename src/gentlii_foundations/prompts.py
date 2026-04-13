from __future__ import annotations

from importlib.resources import files
from pathlib import Path


PROMPT_TEMPLATE_DIR = Path(files("gentlii_foundations").joinpath("prompt_templates"))


def _read_template(relative_path: str) -> str:
    return PROMPT_TEMPLATE_DIR.joinpath(relative_path).read_text(encoding="utf-8").strip()


def build_artifact_prompt(artifact_name: str, source_text: str) -> str:
    shared_rules = _read_template("shared.md")
    instruction = _read_template(f"artifacts/{artifact_name}.md")
    return (
        f"You are extracting the '{artifact_name}' artifact.\n"
        f"{instruction}\n"
        f"{shared_rules}\n\n"
        f"Source material:\n{source_text}"
    )
