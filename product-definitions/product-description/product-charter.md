## Core Principles
- Prioritize outcomes over output; “defining outcomes is very important” and “more important than output.”
- Reduce cognitive load for product professionals by providing concise, reliable product definitions derived from available data.
- Build the right product definition and allow users to trust its quality “without any required action.”

**Confidence:** Medium

**Evidence:** “This product is about reducing cognitive load of product professionals.” / “The users do not need very extensive descriptions but need a very concise product definition.” / “We should therefore make sure we create the right one and trust that.” / “Defining outcomes is very important. More important than output.” / “making sure they can rely on the quality of this product definition without any required action”

**Contradictions:** No contradictory content found.

## Product Boundaries
- Not an additional standalone app with UI/account overhead.
- Not an agile backlog tool.

**Confidence:** High

**Evidence:** “it should not be an additional app with an UI that needs an account and so on.” / “The product is not another agile backlog product tool.”

**Contradictions:** No contradictory content found.

## Behavioral Rules
- Integrate into existing tools/workflows wherever possible; aim to be “invisible” where possible.
- Generate a “product description” by extracting meaning from all available data (strategy, vision, business case, product charter).
- Guard alignment between generated output documents.
- Validate feature requests against the product description.
- Run a “Product Guard” report when CRUD changes are detected in product input files.

**Confidence:** High

**Evidence:** “Wherever possible the product should integrate within existing tools and workflows.” / “Wherever we can make the product invisible we will do that.” / “The product will create strategic, product vision, product charter documents that are created by extracting the meaning from all available data.” / “The product will guard alignment between all mentioned output documents” / “The product will validate feature requests against the product description.” / “If there is any change (crud) detected in product input files the the Product Guard should run and create a report.”

**Contradictions:** No contradictory content found.

## Decision-Making Rules
- Prefer concision over extensive descriptions.
- Prefer integration/invisibility over adding a new UI/app.
- Prefer outcome-definition quality over AI “output” volume.

**Confidence:** Medium

**Evidence:** “The users do not need very extensive descriptions but need a very concise product definition.” / “Wherever possible the product should integrate within existing tools and workflows.” / “Wherever we can make the product invisible we will do that.” / “Output over outcome while is must be the other way around.”

**Contradictions:** No contradictory content found.

## Product Character
- “Invisible” and low-friction (minimal surface area in user workflow).
- Concise and clarity-focused (quick verification, quick feedback).

**Confidence:** Medium

**Evidence:** “Wherever we can make the product invisible we will do that.” / “need a very concise product definition.” / “quickly verify… →give clarity and quick feedback.”

**Contradictions:** No contradictory content found.

## Language and Tone
- Concise documentation style (avoid extensive descriptions).

**Confidence:** Low

**Evidence:** “The users do not need very extensive descriptions but need a very concise product definition.”

**Contradictions:** No contradictory content found.

## Evolution Constraints
- The product should evolve toward integrations and invisibility rather than becoming a standalone UI/account-based app.

**Confidence:** Medium

**Evidence:** “it should not be an additional app with an UI that needs an account and so on.” / “Wherever possible the product should integrate within existing tools and workflows.” / “Wherever we can make the product invisible we will do that.”

**Contradictions:** No contradictory content found.

## Integrity Checks
- Product Guard runs on detected CRUD changes in product input files and produces a report.
- Feature validation checks features against the product description.
- Guard alignment between all output documents in the product description set.

**Confidence:** Medium

**Evidence:** “If there is any change (crud) detected… the Product Guard should run and create a report.” / “Checks features against the product description files” / “guard alignment between all mentioned output documents”

**Contradictions:** No contradictory content found.

### Completeness

Partial

### Strength

Medium

## Suggestion
- Define explicit pass/fail criteria for “quality” of the product definition (what constitutes “confidently right,” and how it’s measured).
- Specify the decision hierarchy for conflicts (e.g., if extracted Strategy and Product Charter disagree, which wins and why).
- Add explicit integrity gates before accepting changes (e.g., required alignment checks, stakeholder review triggers, data provenance requirements).
- Make “concise” enforceable (e.g., max length, required sections, reading-time target).
- Clarify non-goals beyond “not an app/backlog tool” (e.g., not a project manager, not a requirements generator, not a replacement for discovery).