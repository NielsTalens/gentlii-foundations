## Core Principles
Prioritize reducing the cognitive load for product professionals by producing concise, high-quality product definitions users can trust, and by emphasizing outcomes over output.

**Confidence:** High  
**Evidence:** “reducing cognitive load of product professionals”; “need a very concise product definition”; “rely on the quality of this product definition”; “Defining outcomes is very important. More important than output.”  
**Contradictions:** No contradictory content found.

## Product Boundaries
Gentlii is not an additional standalone app requiring an account and UI, and it is not an agile backlog tool. It should avoid being “visible” where possible by integrating into existing tools/workflows.

**Confidence:** High  
**Evidence:** “it should not be an additional app with an UI that needs an account and so on”; “The product is not another agile backlog product tool.”; “Wherever possible the product should integrate within existing tools and workflows.”; “Wherever we can make the product invisible we will do that.”  
**Contradictions:** No contradictory content found.

## Behavioral Rules
- Integrate into existing tools and workflows where possible; make the product “invisible” where possible.  
- Create an opinionated product definition by extracting meaning from available data/files.  
- Maintain/guard alignment across generated “product description” documents.  
- Validate feature requests (and ideas) against the product description/product definition.

**Confidence:** High  
**Evidence:** “Wherever possible the product should integrate within existing tools and workflows.”; “Wherever we can make the product invisible we will do that.”; “We will capture this in a opinionated product definition.”; “created by extracting the meaning from all available data.”; “The product will guard alignment between all mentioned output documents”; “provide a way for them to check whether any idea aligns with the product definition”; “The product will validate feature requests against the product description.”  
**Contradictions:** No contradictory content found.

## Decision-Making Rules
When evaluating work/requests, prioritize outcome definition and alignment to the product definition over producing output, and reject/flag items that do not align with the product definition/product description.

**Confidence:** Medium  
**Evidence:** “Defining outcomes is very important. More important than output.”; “provide a way for them to check whether any idea aligns with the product definition”; “validate feature requests against the product description.”  
**Contradictions:** No contradictory content found.

## Product Character
The product should feel low-friction and lightweight (“invisible”), reducing cognitive load by being concise and requiring minimal/no user action to trust quality.

**Confidence:** Medium  
**Evidence:** “reducing cognitive load”; “not be an additional app with an UI that needs an account”; “Wherever we can make the product invisible we will do that.”; “rely on the quality of this product definition without any required action”; “very concise product definition.”  
**Contradictions:** No contradictory content found.

## Language and Tone
Content should be concise (users do not need extensive descriptions).

**Confidence:** High  
**Evidence:** “The users do not need very extensive descriptions but need a very concise product definition.”  
**Contradictions:** No contradictory content found.

## Evolution Constraints
Avoid evolving into a standalone UI-heavy account-based app; continue to integrate within existing tools and workflows; avoid becoming an agile backlog tool.

**Confidence:** Medium  
**Evidence:** “should not be an additional app with an UI that needs an account”; “Wherever possible the product should integrate within existing tools and workflows.”; “not another agile backlog product tool.”  
**Contradictions:** No contradictory content found.

## Integrity Checks
- Ensure the quality of the product definition without requiring user action.  
- Guard alignment between generated documents in the “product description.”  
- Validate feature requests and ideas against the product description/product definition.  
- Detect changes in product input files (implied trigger for re-guarding/re-generation).

**Confidence:** Medium  
**Evidence:** “making sure they can rely on the quality of this product definition without any required action”; “The product will guard alignment between all mentioned output documents”; “validate feature requests against the product description”; “If there is any change (crud) detected in product input files”  
**Contradictions:** No contradictory content found.

### Completeness

Partial

### Strength

Medium

## Suggestion
- Define explicit pass/fail criteria for “quality of the product definition” (e.g., required sections, evidence traceability, freshness thresholds).
- Add clear trade-off rules (e.g., conciseness vs completeness; when to ask the user vs auto-decide).
- Specify how alignment conflicts between documents are detected and resolved (source-of-truth order, escalation behavior).
- Provide explicit tone/style guidelines beyond “concise” (e.g., voice, reading level, formatting conventions).
- Clarify the “change detected” behavior (what triggers regeneration, what is versioned, and how users are notified in an “invisible” product).