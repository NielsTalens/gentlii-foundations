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

- Core principles
- Product boundaries (what the product is not)
- Behavioral rules (how the product behaves)
- Decision-making rules (how trade-offs are resolved)
- Product character (how the product should feel)
- Language and tone guidance
- Evolution constraints
- Integrity checks or evaluation rules

## Additional Rules

- Do NOT restate strategy or product vision.

---

## Output

For each subject below, use this structure:
- `##` heading for the subject name
- one or more normal paragraphs with extracted content, or `Not found`
- a bold confidence line written as `**Confidence:** High | Medium | Low`
- a bold evidence line written as `**Evidence:** <exact quote, close paraphrase, or "No supporting evidence found">`
- a bold contradictions line written as `**Contradictions:** <contradiction with evidence, or "No contradictory content found.">`

## Core Principles
[Extracted content or "Not found"]

## Product Boundaries
[Extracted content or "Not found"]

## Behavioral Rules
[Extracted content or "Not found"]

## Decision-Making Rules
[Extracted content or "Not found"]

## Product Character
[Extracted content or "Not found"]

## Language and Tone
[Extracted content or "Not found"]

## Evolution Constraints
[Extracted content or "Not found"]

## Integrity Checks
[Extracted content or "Not found"]

---

### Completeness

Assess whether key product charter elements are present:

- Principles
- Boundaries
- Behavioral rules
- Decision-making rules

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
- enforceability of rules
- presence of clear constraints
- usefulness for decision-making
- consistency across elements

Return:
Do NOT return any other output besides the following:
Do NOT return explanatory text like `Complete -> ...` or `High -> ...`.
Return only one of these values on the next line:
- High → clear, enforceable, actionable
- Medium → partially defined, some ambiguity
- Low → vague, generic, or not actionable

---

## Suggestion

Return exactly one normal paragraph under this heading.
If no useful suggestion can be made from the source material, return `Not found`.

Return the final evaluation block in exactly this shape:

### Completeness

Partial

### Strength

Medium

## Suggestion

One normal paragraph here.
