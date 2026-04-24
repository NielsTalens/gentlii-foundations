## Core Principles
Prioritize outcomes and strong product context over output/specs, and reduce cognitive load by producing a concise, trustworthy product definition users can rely on.

**Confidence:** Medium  
**Evidence:** “This product is about reducing cognitive load of product professionals.” / “The users do not need very extensive descriptions but need a very concise product definition.” / “Defining outcomes is very important. More important than output.” / “start building too early without enough product context.”

**Contradictions:** No contradictory content found.

## Product Boundaries
Gentlii is not an additional UI-heavy app requiring accounts, and it is not an agile backlog tool. It should integrate into existing tools/workflows and be “invisible” where possible.

**Confidence:** High  
**Evidence:** “it should not be an additional app with an UI that needs an account and so on.” / “The product is not another agile backlog product tool.” / “Wherever possible the product should integrate within existing tools and workflows.” / “Wherever we can make the product invisible we will do that.”

**Contradictions:** No contradictory content found.

## Behavioral Rules
Create an opinionated product definition by extracting meaning from available data, produce a “product description” set of documents (including a product charter), and actively guard/validate alignment and feature requests against the product description. Detect changes in input files to trigger guarding.

**Confidence:** Medium  
**Evidence:** “We will capture this in a opinionated product definition.” / “The product will create strategic, product vision, product charter documents that are created by extracting the meaning from all available data.” / “The product will guard alignment between all mentioned output documents” / “The product will validate feature requests against the product description.” / “If there is any change (crud) detected in product input files”

**Contradictions:** No contradictory content found.

## Decision-Making Rules
When trade-offs arise, prefer outcomes over output; prefer concision over extensive description; prefer integration/invisibility over building a standalone app UI.

**Confidence:** Medium  
**Evidence:** “Defining outcomes is very important. More important than output.” / “The users do not need very extensive descriptions but need a very concise product definition.” / “Wherever possible the product should integrate within existing tools and workflows.” / “Wherever we can make the product invisible we will do that.”

**Contradictions:** No contradictory content found.

## Product Character
Should feel lightweight/low-friction and trustworthy/reliable (users can “rely on the quality… without any required action”), with minimal visible surface area.

**Confidence:** Medium  
**Evidence:** “reducing cognitive load” / “making sure they can rely on the quality of this product definition without any required action” / “make the product invisible”

**Contradictions:** No contradictory content found.

## Language and Tone
Concise documentation style (not extensive descriptions).

**Confidence:** Medium  
**Evidence:** “The users do not need very extensive descriptions but need a very concise product definition.”

**Contradictions:** No contradictory content found.

## Evolution Constraints
Avoid evolving into a standalone UI app requiring accounts; remain integrated with existing tools/workflows; avoid becoming an agile backlog tool.

**Confidence:** Medium  
**Evidence:** “should not be an additional app with an UI that needs an account” / “Wherever possible… integrate within existing tools and workflows.” / “not another agile backlog product tool.”

**Contradictions:** No contradictory content found.

## Integrity Checks
Must ensure quality of the product definition without user effort; guard alignment between produced documents; validate ideas/feature requests against the product definition/product description; monitor for changes in input files.

**Confidence:** Medium  
**Evidence:** “making sure they can rely on the quality of this product definition without any required action” / “providing a way for them to check whether any idea aligns with the product definition” / “guard alignment between all mentioned output documents” / “validate feature requests against the product description” / “If there is any change (crud) detected in product input files”

**Contradictions:** No contradictory content found.

### Completeness

Partial

### Strength

Medium

## Suggestion
- Define explicit acceptance criteria for “quality” of the product definition (e.g., completeness checks, source coverage, conflict handling).
- Specify concrete decision rules for resolving conflicting source inputs (hierarchy of sources, recency vs authority, confidence thresholds).
- Add clear behavioral constraints on when/how the product should ask users for clarification vs auto-decide.
- Define a standard tone/voice guide for generated artifacts beyond “concise” (e.g., formality, audience, terminology).
- Document the “change detected” workflow end-to-end (what triggers re-generation vs incremental update; how alignment violations are reported/blocked).