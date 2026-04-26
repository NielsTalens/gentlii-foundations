## Core Principles
- Reduce cognitive load for product professionals by making product definition/alignment work concise, reliable, and low-effort.
- Prioritize outcome/quality of product thinking over generating large amounts of output or starting to build too early.
- Provide a “confidently right” product definition extracted from available data, with minimal user action required.

**Confidence:** Medium  
**Evidence:** “This product is about reducing cognitive load of product professionals.” / “The users do not need very extensive descriptions but need a very concise product definition.” / “making sure they can rely on the quality of this product definition without any required action” / “Output over outcome while is must be the other way around.” / “start building too early without enough product context.”  
**Contradictions:** No contradictory content found.

## Product Boundaries
- Not an additional standalone app with UI/account requirements.
- Not an agile backlog/product tool.
- Not focused on spec-driven development as a default (spec-driven “has its own place and time”).

**Confidence:** High  
**Evidence:** “Therefore it should not be an additional app with an UI that needs an account and so on.” / “The product is not another agile backlog product tool.” / “Spec driven is a great tool but has its own place and time.”  
**Contradictions:** No contradictory content found.

## Behavioral Rules
- Integrate into existing tools and workflows where possible; make the product “invisible” wherever possible.
- Create a set of documents (“product description”) by extracting meaning from “all available data,” including product charter.
- Guard alignment between the produced documents and validate feature requests against the product description.
- Provide stakeholders quick verification and feedback on feature request feasibility/fit.

**Confidence:** Medium  
**Evidence:** “Wherever possible the product should integrate within existing tools and workflows.” / “Wherever we can make the product invisible we will do that.” / “The product will create strategic, product vision, product charter documents… by extracting the meaning from all available data.” / “The product will guard alignment between all mentioned output documents” / “The product will validate feature requests against the product description.” / “provide stakeholders a way to quickly verify a feature requests possibility.→give clarity and quick feedback.”  
**Contradictions:** No contradictory content found.

## Decision-Making Rules
- Prefer concise product definitions over extensive descriptions.
- Prefer outcome over output.
- Prefer quality/context-building before building; avoid building too early without enough product context.
- Prefer integration/invisibility over adding a new standalone UI/app.

**Confidence:** Medium  
**Evidence:** “The users do not need very extensive descriptions but need a very concise product definition.” / “Defining outcomes is very important. More important than output.” / “start building too early without enough product context.” / “Wherever possible the product should integrate…” and “not… an additional app with an UI…”  
**Contradictions:** No contradictory content found.

## Product Character
- Invisible, low-friction, concise, reliable/trustworthy (“confidently right”), clarity-oriented (quick feedback).

**Confidence:** Medium  
**Evidence:** “Wherever we can make the product invisible we will do that.” / “very concise product definition.” / “rely on the quality… without any required action” / “confidently right on all facets.” / “give clarity and quick feedback.”  
**Contradictions:** No contradictory content found.

## Language and Tone
- Documents should be concise rather than extensive.

**Confidence:** Low  
**Evidence:** “The users do not need very extensive descriptions but need a very concise product definition.”  
**Contradictions:** No contradictory content found.

## Evolution Constraints
- Growth should favor integration with existing tools/workflows rather than becoming a separate app with its own UI/account.
- Product improvements should aim for “less code” while improving outcomes/quality.

**Confidence:** Low  
**Evidence:** “should not be an additional app…” / “Wherever possible the product should integrate…” / “It will improve the product with less code.”  
**Contradictions:** No contradictory content found.

## Integrity Checks
- Validate feature requests against the product description.
- Detect changes in product input files (CRUD) to trigger guarding behavior (implied process start).

**Confidence:** Medium  
**Evidence:** “The product will validate feature requests against the product description.” / “If there is any change (crud) detected in product input files”  
**Contradictions:** No contradictory content found.

### Completeness

Partial

### Strength

Medium

## Suggestion
- Define explicit pass/fail integrity criteria for “quality” and “confidently right” (e.g., required sections, evidence traceability, consistency checks across documents).
- Specify concrete decision rules for trade-offs (e.g., conciseness vs completeness, integration vs capability, automation vs human review).
- Add explicit evolution constraints about what new capabilities are allowed (and disallowed) as the product expands (e.g., plugins only, no standalone UI except admin tooling).
- Clarify the “product description guarding” workflow end-to-end (triggers, actions taken, notification behavior, and who approves changes).
- Add tone/style rules for generated artifacts beyond “concise” (e.g., reading level, format conventions, terminology consistency).