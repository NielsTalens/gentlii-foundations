from pathlib import Path

from gentlii_foundations.prompts import PROMPT_TEMPLATE_DIR, build_artifact_prompt


def test_prompt_includes_no_invention_rule():
    prompt = build_artifact_prompt("strategy", "source text")
    assert "Do not invent missing information" in prompt


def test_prompt_loads_shared_and_artifact_instructions_from_files():
    prompt = build_artifact_prompt("strategy", "source text")
    assert "Return clean markdown only." in prompt
    assert "You are a strategy extractor." in prompt


def test_business_case_prompt_inherits_common_extraction_rules():
    prompt = build_artifact_prompt("business-case", "source text")
    assert 'If information is missing, mark it as "Not found".' in prompt
    assert "You MAY provide suggestions, but they must be clearly marked as \"Suggestion\"" in prompt


def test_prompt_includes_shared_suggestions_section():
    prompt = build_artifact_prompt("business-case", "source text")
    assert "### Suggestions" in prompt
    assert "Provide concrete suggestions to improve the artifact." in prompt


def test_prompt_template_directory_contains_strategy_prompt_file():
    template_dir = Path(PROMPT_TEMPLATE_DIR)
    assert (template_dir / "shared.md").is_file()
    assert (template_dir / "artifacts" / "strategy.md").is_file()
