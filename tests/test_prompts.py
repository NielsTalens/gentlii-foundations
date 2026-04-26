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


def test_prompt_requires_confidence_below_each_output_section():
    prompt = build_artifact_prompt("product-vision", "source text")
    assert (
        "For every subject or section in the Output Structure, include a `### Confidence` heading "
        "immediately below the extracted content and before the supporting evidence."
    ) in prompt
    assert "Write the confidence value directly below `### Confidence` as normal paragraph text" in prompt
    assert "Do not merge the confidence value and `**Evidence:**` onto one line." in prompt


def test_product_guard_prompt_uses_numeric_alignment_and_categorical_risk_signals():
    prompt = build_artifact_prompt("product-guard", "source text")
    assert "### Alignment score" in prompt
    assert "### Confidence" in prompt
    assert "Write the value directly below `### Alignment score` as exactly one of `1/5`, `2/5`, `3/5`, `4/5`, `5/5`." in prompt
    assert "Write the value directly below `### Confidence` as exactly one of `Low`, `Medium`, `High`." in prompt


def test_prompt_includes_shared_suggestions_section():
    prompt = build_artifact_prompt("business-case", "source text")
    assert "### Suggestions" in prompt
    assert "Provide concrete suggestions to improve the artifact." in prompt
    assert "Write suggestions under a `## Suggestion` heading." in prompt


def test_prompt_template_directory_contains_strategy_prompt_file():
    template_dir = Path(PROMPT_TEMPLATE_DIR)
    assert (template_dir / "shared.md").is_file()
    assert (template_dir / "artifacts" / "strategy.md").is_file()


def test_all_artifact_templates_keep_evidence_and_contradictions_inline_per_subject():
    template_dir = Path(PROMPT_TEMPLATE_DIR) / "artifacts"
    artifact_names = [
        "business-case",
        "strategy",
        "product-vision",
        "product-charter",
    ]

    for artifact_name in artifact_names:
        template = (template_dir / f"{artifact_name}.md").read_text(encoding="utf-8")
        assert "## Output" in template
        assert "### Completeness" in template
        assert "### Strength" in template
        assert "## Suggestion" in template
        assert "## Evidence" not in template
        assert "## Contradictions" not in template


def test_artifact_templates_define_output_items_as_h2():
    template_dir = Path(PROMPT_TEMPLATE_DIR) / "artifacts"

    strategy_template = (template_dir / "strategy.md").read_text(encoding="utf-8")

    assert "## Mission" in strategy_template
    assert "## Target Customer" in strategy_template
    assert "## Value Proposition" in strategy_template
    assert "## Strategic Pillars" in strategy_template
    assert "## Success Metrics" in strategy_template
    assert "## Long-term Vision" in strategy_template
    assert "## Product Strategy" not in strategy_template
    assert "## Company Strategy" not in strategy_template
    assert "## Business Rationale" in (template_dir / "business-case.md").read_text(encoding="utf-8")
    assert "## Vision Statement" in (template_dir / "product-vision.md").read_text(encoding="utf-8")
    assert "## Target Groups" in (template_dir / "product-vision.md").read_text(encoding="utf-8")
    assert "## Core Principles" in (template_dir / "product-charter.md").read_text(encoding="utf-8")


def test_shared_prompt_requires_inline_evidence_and_contradictions_per_subject():
    prompt = build_artifact_prompt("business-case", "source text")
    assert (
        "For every subject or section in the Output Structure, include the related evidence "
        "immediately below the extracted content."
    ) in prompt
    assert (
        "For every subject or section in the Output Structure, if there are contradictions, "
        "include the related evidence immediately below the extracted content."
    ) in prompt
    assert "Write evidence as `**Evidence:** <...>`." in prompt
    assert "Write contradictions as `**Contradictions:** <...>`." in prompt


def test_artifact_templates_require_exact_final_section_shape():
    template_dir = Path(PROMPT_TEMPLATE_DIR) / "artifacts"
    strategy_template = (template_dir / "strategy.md").read_text(encoding="utf-8")
    business_case_template = (template_dir / "business-case.md").read_text(encoding="utf-8")
    product_vision_template = (template_dir / "product-vision.md").read_text(encoding="utf-8")
    product_charter_template = (template_dir / "product-charter.md").read_text(encoding="utf-8")

    assert "Do NOT return explanatory text like `Complete -> ...` or `High -> ...`." in strategy_template
    assert "Return only one of these values on the next line:" in strategy_template
    assert "## Suggestion" in strategy_template
    assert "Return exactly one normal paragraph under this heading." not in strategy_template
    assert "Return the final evaluation block in exactly this shape:" in strategy_template
    assert "### Completeness" in strategy_template
    assert "### Strength" in strategy_template

    assert "Do NOT return explanatory text like `Complete -> ...` or `High -> ...`." in business_case_template
    assert "Return only one of these values on the next line:" in business_case_template
    assert "## Suggestion" in business_case_template
    assert "Return exactly one normal paragraph under this heading." not in business_case_template
    assert "Return the final evaluation block in exactly this shape:" in business_case_template
    assert "### Completeness" in business_case_template
    assert "### Strength" in business_case_template

    assert "Do NOT return explanatory text like `Complete -> ...` or `High -> ...`." in product_vision_template
    assert "Return only one of these values on the next line:" in product_vision_template
    assert "## Suggestion" in product_vision_template
    assert "Return exactly one normal paragraph under this heading." not in product_vision_template
    assert "Return the final evaluation block in exactly this shape:" in product_vision_template
    assert "### Completeness" in product_vision_template
    assert "### Strength" in product_vision_template

    assert "Do NOT return explanatory text like `Complete -> ...` or `High -> ...`." in product_charter_template
    assert "Return only one of these values on the next line:" in product_charter_template
    assert "## Suggestion" in product_charter_template
    assert "Return exactly one normal paragraph under this heading." not in product_charter_template
    assert "Return the final evaluation block in exactly this shape:" in product_charter_template
    assert "### Completeness" in product_charter_template
    assert "### Strength" in product_charter_template
