## Core Principles
- Focus on improving product quality and outcomes over generating output.
- Reduce cognitive load for product professionals by providing concise, trusted product definitions derived from available data.
- Prefer invisibility and integration into existing workflows over adding new UI/account friction.

**Confidence:** High

**Evidence:** “This product is about reducing cognitive load of product professionals.” / “Defining outcomes is very important. More important than output.” / “Wherever possible the product should integrate within existing tools and workflows.” / “Wherever we can make the product invisible we will do that.” / “The users do not need very extensive descriptions but need a very concise product definition.”

**Contradictions:** No contradictory content found.

## Product Boundaries
- Not an additional standalone app with UI/account requirements.
- Not an “agile backlog product tool.”
- Avoid extensive descriptions.

**Confidence:** High

**Evidence:** “Therefore it should not be an additional app with an UI that needs an account and so on.” / “The product is not another agile backlog product tool.” / “The users do not need very extensive descriptions…”

**Contradictions:** No contradictory content found.

## Behavioral Rules
- Create product “description” documents (strategy, product vision, business case, product charter) by extracting meaning from “all available data.”
- Maintain/guard alignment across the generated output documents.
- Validate feature requests against the product description.
- Detect changes in product input files and run a “Product Guard” to create a report.
- Output documents are produced in Markdown and generated HTML.

**Confidence:** High

**Evidence:** “The product will create strategic, product vision, product charter documents that are created by extracting the meaning from all available data.” / “The product will guard alignment between all mentioned output documents (the product description)” / “The product will validate feature requests against the product description.” / “If there is any change (crud) detected in product input files the the Product Guard should run and create a report.” / “These are written both in markdown as in a generated html page”

**Contradictions:** No contradictory content found.

## Decision-Making Rules
- Prefer outcome-focus over output-focus.
- Prefer integration/invisibility over building a new visible app experience.
- Prefer concise product definition over extensive descriptions.

**Confidence:** Medium

**Evidence:** “Defining outcomes is very important. More important than output.” / “Wherever possible the product should integrate within existing tools and workflows.” / “Wherever we can make the product invisible we will do that.” / “The users do not need very extensive descriptions…”

**Contradictions:** No contradictory content found.

## Product Character
- “Invisible” and low-friction.
- Concise and clarity-oriented (quick verification, quick feedback).

**Confidence:** Medium

**Evidence:** “Wherever we can make the product invisible we will do that.” / “very concise product definition.” / “give clarity and quick feedback.”

**Contradictions:** No contradictory content found.

## Language and Tone
Not found

**Confidence:** High

**Evidence:** No supporting evidence found

**Contradictions:** No contradictory content found.

## Evolution Constraints
- Growth should favor integration within existing tools/workflows rather than adding a standalone UI/account-based app.

**Confidence:** Medium

**Evidence:** “Wherever possible the product should integrate within existing tools and workflows.” / “should not be an additional app with an UI that needs an account…”

**Contradictions:** No contradictory content found.

## Integrity Checks
- Run “Product Guard” when CRUD changes are detected in input files and generate a report.
- Ensure/guard alignment between generated documents.
- Validate feature requests against the product description.

**Confidence:** Medium

**Evidence:** “If there is any change (crud) detected in product input files the the Product Guard should run and create a report.” / “The product will guard alignment…” / “validate feature requests against the product description.”

**Contradictions:** No contradictory content found.

### Completeness

Partial

### Strength

Medium

## Suggestion
- Define explicit pass/fail criteria for “guard alignment” (what counts as misalignment; what the report must contain; what actions are blocked or flagged).
- Specify decision trade-offs when sources conflict (“all available data” may be inconsistent): which sources win, and how uncertainty is represented.
- Add explicit tone/style rules for generated artifacts (e.g., concise, non-jargon, target length, formatting standards).
- Add evolution constraints beyond “no extra UI” (e.g., permitted integrations, privacy/security boundaries, data retention limits).
- Define integrity checks for feature validation (required inputs, confidence thresholds, and what happens when confidence is low).