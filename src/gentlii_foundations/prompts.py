from __future__ import annotations


ARTIFACT_INSTRUCTIONS = {
    "strategy": "Extract the product strategy, value proposition, strategic goals, and long-term direction.",
    "business-case": "Extract the business rationale, expected value, assumptions, and measurable business outcomes.",
    "product-vision": "Extract target groups, needs, core features, business goals, and differentiators.",
    "jtbd": "Extract jobs to be done, user problems, desired outcomes, and supporting journey context.",
    "product-charter": "Extract principles, boundaries, behavioral rules, product character, and decision-making guidance.",
}


def build_artifact_prompt(artifact_name: str, source_text: str) -> str:
    instruction = ARTIFACT_INSTRUCTIONS[artifact_name]
    return (
        f"You are extracting the '{artifact_name}' artifact.\n"
        f"{instruction}\n"
        "Return clean markdown only.\n"
        "Do not invent missing information.\n"
        "If evidence is missing, omit the unsupported claim.\n\n"
        f"Source material:\n{source_text}"
    )
