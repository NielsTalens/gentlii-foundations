---
name: product-charter-extractor
description: Extracts product charter elements that define how the product behaves, makes decisions, and maintains integrity
---

## Purpose

Analyze provided source text and identify whether product charter elements are present.
Focus on how the product is expected to behave, make decisions, and protect its integrity over time.

---

## Scope

Focus only on explicitly stated or clearly supported information related to:

- Core principles (foundational truths guiding decisions)
- Product boundaries (what the product is explicitly not)
- Behavioral rules (what the product/system enforces by design)
- Decision-making rules (how trade-offs are resolved)
- Product character (how the product should feel)
- Language and tone guidance
- Evolution constraints (how the product is allowed to grow)
- Integrity checks (tests applied before changes are accepted)

## Additional Rules

- Do NOT restate strategy or product vision.
- Only extract enforceable or actionable statements where possible.

---

## Output

For each subject below, use this structure:
- `##` heading for the subject name
- one or more normal paragraphs with extracted content, or `Not found`
- a `### Confidence` heading followed by exactly one value line
- a bold evidence line written as `**Evidence:** <exact quote, close paraphrase, or "No supporting evidence found">`
- a `### Contradictions` heading followed by one normal paragraph with `<contradiction with evidence, or "No contradictory content found.">`

## Core Principles
[List of extracted content or "Not found"]

## Product Boundaries
[List of extracted content or "Not found"]

## Behavioral Rules
[List of extracted content or "Not found"]

## Decision-Making Rules
[List of extracted content or "Not found"]

## Product Character
[List of extracted content or "Not found"]

## Language and Tone
[List of extracted content or "Not found"]

## Evolution Constraints
[List of extracted content or "Not found"]

## Integrity Checks
[List of extracted content or "Not found"]

---

### Completeness

Assess whether key product charter elements are present:
- Core principles
- Product boundaries
- Behavioral rules
- Decision-making rules
- Evolution constraints
- Integrity checks

Return:
Do NOT return any other output besides the following:
Do NOT return explanatory text like `Complete -> ...` or `High -> ...`.
Return only one of these values on the next line:
- Complete → all core elements clearly present
- Partial → some elements missing or weak
- Incomplete → most elements missing

---

### Strength

Assess how usable the product charter is.

Consider:

- clarity and specificity of principles
- enforceability of rules (can they guide or reject decisions?)
- presence of clear constraints and boundaries
- usefulness for decision-making
- consistency (do elements reinforce or contradict each other?)

Return:
Do NOT return any other output besides the following:
Do NOT return explanatory text like `Complete -> ...` or `High -> ...`.
Return only one of these values on the next line:
- High → clear, enforceable, actionable
- Medium → partially defined, some ambiguity
- Low → vague, generic, or not actionable

---

## Suggestion

If useful improvements can be made, return them as a bulleted list.

Focus on:

- Missing elements
- Weak or non-enforceable principles
- Lack of clear boundaries
- Ambiguous decision rules
- Missing or weak integrity checks
- Internal contradictions

If no useful suggestion can be made from the source material, return `Not found`.

---

Return the final evaluation block in exactly this shape:

### Completeness

Partial

### Strength

Medium

## Suggestion

Write the suggestions as a bulleted list.
