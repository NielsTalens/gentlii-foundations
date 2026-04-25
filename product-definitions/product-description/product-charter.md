## Core Principles

- Prioritize reducing cognitive load for product professionals.
- Favor outcome over output; defining outcomes is crucial.
- Start with sufficient product context; avoid building too early based on specs alone.
- Product definitions should be concise and reliable without requiring user effort to ensure quality.

**Confidence:** Medium  
**Evidence:** “This product is about reducing cognitive load of product professionals.” / “Defining outcomes is very important. More important than output.” / “start building too early without enough product context.” / “very concise product definition.” and “rely on the quality… without any required action”  
**Contradictions:** No contradictory content found.

## Product Boundaries

- Not an additional standalone app with a UI requiring accounts.
- Not another agile backlog/product tool.
- Not primarily focused on maximizing AI output at the expense of product quality.

**Confidence:** High  
**Evidence:** “it should not be an additional app with an UI that needs an account” / “The product is not another agile backlog product tool.” / “focus mainly on the amount of output AI can generate… not on how to improve the quality”  
**Contradictions:** No contradictory content found.

## Behavioral Rules

- Integrate into existing tools and workflows where possible; make the product “invisible” when possible.
- Extract meaning from “all available data” to generate core product documents (including a product charter).
- Guard alignment between generated “output documents” within the product description.
- Validate feature requests against the product description.
- Detect changes (CRUD) in input files and trigger “product description guarding.”

**Confidence:** Medium  
**Evidence:** “Wherever possible the product should integrate within existing tools and workflows.” / “Wherever we can make the product invisible we will do that.” / “created by extracting the meaning from all available data.” / “guard alignment between all mentioned output documents” / “validate feature requests against the product description.” / “If there is any change (crud) detected in product input files”  
**Contradictions:** No contradictory content found.

## Decision-Making Rules

- Prefer outcomes over output when making trade-offs.
- Prefer conciseness over extensive descriptions for product definition.
- Prefer integration/invisibility over adding new UI surfaces.

**Confidence:** Medium  
**Evidence:** “Defining outcomes is very important. More important than output.” / “do not need very extensive descriptions but need a very concise product definition.” / “should integrate within existing tools… Wherever we can make the product invisible we will do that.”  
**Contradictions:** No contradictory content found.

## Product Character

- Feels lightweight and low-friction (reduces cognitive load; minimal/no standalone UI; “invisible” where possible).
- Feels opinionated (an “opinionated product definition”) and clarity-oriented (quick verification/feedback for stakeholders).

**Confidence:** Medium  
**Evidence:** “reducing cognitive load” / “not… an additional app with an UI” / “make the product invisible” / “capture this in a opinionated product definition.” / “quickly verify… give clarity and quick feedback.”  
**Contradictions:** No contradictory content found.

## Language and Tone

- Product definition should be concise (implying brief, to-the-point language).

**Confidence:** Low  
**Evidence:** “do not need very extensive descriptions but need a very concise product definition.”  
**Contradictions:** No contradictory content found.

## Evolution Constraints

- Growth should favor integrations within existing tools/workflows rather than expanding into a standalone app experience.

**Confidence:** Low  
**Evidence:** “should integrate within existing tools and workflows.” and “should not be an additional app with an UI that needs an account”  
**Contradictions:** No contradictory content found.

## Integrity Checks

- Quality of the product definition should be reliable “without any required action” by users.
- Changes in input files should be detected (CRUD detection) and used for “product description guarding.”
- Feature requests should be checked for alignment/validity against the product description.
- Alignment across generated documents is guarded.

**Confidence:** Medium  
**Evidence:** “rely on the quality… without any required action” / “way for them to check whether any idea aligns with the product definition” / “guard alignment between all mentioned output documents” / “validate feature requests against the product description.” / “If there is any change (crud) detected in product input files”  
**Contradictions:** No contradictory content found.

### Completeness

Partial

### Strength

Medium

## Suggestion

- Define explicit pass/fail integrity tests for “quality” and “alignment” (e.g., required fields, consistency rules, provenance/citations, confidence thresholds).
- Specify decision rules for conflicts in source inputs (e.g., recency vs authority, stakeholder weighting, tie-breakers).
- Add explicit evolution constraints about what new document types/features are allowed vs disallowed (to avoid drifting into a full product management suite).
- Provide concrete language/tone guidelines for generated artifacts (e.g., voice, reading level, maximum length, required structure).
- Clarify what happens when a feature request is “Not good” (workflow, feedback format, and whether alternatives are suggested).