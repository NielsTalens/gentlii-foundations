---
name: business-case-extractor
description: Extracts business rationale, value expectations, assumptions, and measurable outcomes.
---

## Purpose

Analyze provided source text and identify whether business case elements are present.

## Scope

Focus only on explicitly stated or clearly supported information related to:

- Business rationale (why this initiative should exist now)
- Expected value (type of value created, not the metric)
- Assumptions (what must be true for value to materialize)
- Measurable business outcomes (how success is measured)

## Output

For each subject below, use this structure:
- `##` heading for the subject name
- one or more normal paragraphs with extracted content, or `Not found`
- a bold confidence line written as `**Confidence:** High | Medium | Low`
- a bold evidence line written as `**Evidence:** <exact quote, close paraphrase, or "No supporting evidence found">`
- a bold contradictions line written as `**Contradictions:** <contradiction with evidence, or "No contradictory content found.">`

## Business Rationale
[Extracted content or "Not found"]

## Expected Value
[Extracted content or "Not found"]

## Assumptions
[Extracted content or "Not found"]

## Measurable Business Outcomes
[Extracted content or "Not found"]

---

### Completeness

Assess whether the key business case elements are present:

- Business rationale
- Expected value
- Assumptions
- Measurable outcomes

Return:

Do NOT return any other output besides the following:
Do NOT return explanatory text like `Complete -> ...` or `High -> ...`.
Return only one of these values on the next line:
- Complete -> all core elements clearly present
- Partial -> some elements missing or weak
- Incomplete -> most elements missing

---

### Strength

Assess how usable the business case is:

Consider:
- clarity of the problem or opportunity
- clarity and type of value described
- whether assumptions are explicit and testable
- whether outcomes are measurable (metrics, targets, direction)
- causal coherence (do assumptions logically lead to value and outcomes?) is the problem and purpose clearly and specifically defined?

Return:
Do NOT return any other output besides the following:
Do NOT return explanatory text like `Complete -> ...` or `High -> ...`.
Return only one of these values on the next line:
- High → clear, specific, actionable
- Medium → partially defined, some ambiguity
- Low → vague, generic, not actionable

---

## Suggestion

If useful improvements can be made, return them as a bulleted list.

Focus on:
- Missing elements
- Unclear or generic value
- Hidden or untestable assumptions
- Lack of measurable outcomes
- Weak or broken causal chain

If no useful suggestion can be made from the source material, return `Not found`.

---

Return the final evaluation block in exactly this shape:

### Completeness

Partial

### Strength

Medium

## Suggestion

Write the suggestions as a bulleted list.
