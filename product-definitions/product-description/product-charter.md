## Core Principles

- Outcome over output; spec-driven development has “its own place and time” and should not replace upstream product context and thinking.
- Reduce cognitive load for product professionals by providing concise product definitions and minimizing required user actions.
- Stakeholders should be able to rely on the quality of the product definition “without any required action.”
- “Defining outcomes is very important. More important than output.”

### Confidence

Medium

**Evidence:** “reducing cognitive load of product professionals”; “The users do not need very extensive descriptions but need a very concise product definition.”; “making sure they can rely on the quality of this product definition without any required action”; “Output over outcome while is must be the other way around.”; “Defining outcomes is very important. More important than output.”; “Spec driven is a great tool but has its own place and time.”

### Contradictions

No contradictory content found.

## Product Boundaries

- Not an additional app with a UI that needs an account.
- Not another agile backlog product tool.
- Avoid “start building too early without enough product context” (implied boundary against jumping straight to specs/building without context).

### Confidence

High

**Evidence:** “it should not be an additional app with an UI that needs an account and so on.”; “The product is not another agile backlog product tool.”; “start building too early without enough product context.”

### Contradictions

No contradictory content found.

## Behavioral Rules

- Integrate within existing tools and workflows wherever possible.
- Make the product “invisible” wherever possible.
- Create core documents (strategy, product vision, business case, product charter) by extracting meaning from “all available data” uploaded by users.
- Guard alignment between the produced documents (“product description” set).
- Validate feature requests against the product description.
- When changes (CRUD) are detected in product input files, trigger “product description guarding” (behavior implied but incomplete).

### Confidence

Medium

**Evidence:** “Wherever possible the product should integrate within existing tools and workflows.”; “Wherever we can make the product invisible we will do that.”; “created by extracting the meaning from all available data.”; “A user uploads all types of files…”; “The product will guard alignment between all mentioned output documents”; “The product will validate feature requests against the product description.”; “If there is any change (crud) detected in product input files”

### Contradictions

No contradictory content found.

## Making Rules

Not found

### Confidence

Low

**Evidence:** No supporting evidence found

### Contradictions

No contradictory content found.

## Product Character

- Invisible, low-friction, integrated into existing workflows.
- Concise rather than extensive.

### Confidence

High

**Evidence:** “Wherever we can make the product invisible we will do that.”; “integrate within existing tools and workflows.”; “very concise product definition.”

### Contradictions

No contradictory content found.

## Language and Tone

- Documents should be concise (implies a preference for brevity in generated artifacts).

### Confidence

Medium

**Evidence:** “The users do not need very extensive descriptions but need a very concise product definition.”

### Contradictions

No contradictory content found.

## Evolution Constraints

- Favor improvements “with less code” (directional constraint on how the product evolves/gets better).
- Continue to avoid becoming a standalone UI/account-based app as it grows (constraint implied by explicit boundary).

### Confidence

Low

**Evidence:** “It will improve the product with less code. Better features with less code…”; “should not be an additional app with an UI that needs an account…”

### Contradictions

No contradictory content found.

## Integrity Checks

- Ensure/guard alignment across generated documents before accepting/using them as the product description.
- Validate feature requests against the product description to prevent misaligned work.

### Confidence

Medium

**Evidence:** “The product will guard alignment between all mentioned output documents”; “The product will validate feature requests against the product description.”

### Contradictions

No contradictory content found.

### Completeness

Partial

### Strength

Medium

## Suggestion

- Define explicit decision rules for trade-offs (e.g., “integration over new UI,” “conciseness over completeness,” and when exceptions are allowed).
- Specify concrete integrity checks and pass/fail criteria (e.g., alignment rules, consistency thresholds, source traceability requirements, and what happens on failure).
- Clarify “product description guarding” workflow: triggers, review/approval requirements (if any), and how changes propagate to the generated documents.
- Add enforceable language/tone guidance for generated artifacts (e.g., required structure, maximum length, audience level).
- Make evolution constraints testable (e.g., measurable limits on new UI surfaces, account requirements, or code/ops cost targets tied to releases).