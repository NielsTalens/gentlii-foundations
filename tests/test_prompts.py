from pathlib import Path

from gentlii_foundations.prompts import PROMPT_TEMPLATE_DIR, build_artifact_prompt


def test_prompt_includes_no_invention_rule():
    prompt = build_artifact_prompt("strategy", "source text")
    assert "Do not invent missing information" in prompt


def test_prompt_loads_shared_and_artifact_instructions_from_files():
    prompt = build_artifact_prompt("strategy", "source text")
    assert "Return clean markdown only." in prompt
    assert "You are a strategy extractor." in prompt


def test_prompt_template_directory_contains_strategy_prompt_file():
    template_dir = Path(PROMPT_TEMPLATE_DIR)
    assert (template_dir / "shared.md").is_file()
    assert (template_dir / "artifacts" / "strategy.md").is_file()
