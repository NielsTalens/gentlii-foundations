## Core Principles
- Reduce product professionals’ cognitive load by providing a concise, “confidently right” product definition derived from available data.
- Prioritize outcomes over output when defining and evaluating product work.
- Avoid building too early by ensuring sufficient product context before specs and implementation.
- Integrate into existing tools/workflows and be “invisible” where possible (minimize additional UI/account overhead).

### Confidence
High

**Evidence:** “This product is about reducing cognitive load of product professionals.” / “The users do not need very extensive descriptions but need a very concise product definition.” / “Defining outcomes is very important. More important than output.” / “start building too early without enough product context.” / “Wherever possible the product should integrate within existing tools and workflows.” / “Wherever we can make the product invisible we will do that.”

### Contradictions
No contradictory content found.

## Product Boundaries
- Not an additional standalone app/UI that requires accounts (“should not be an additional app with an UI that needs an account and so on”).
- Not an agile backlog tool.
- Not focused on spec-driven work as the primary mode; specs have “place and time” but shouldn’t replace earlier product context work.

### Confidence
High

**Evidence:** “it should not be an additional app with an UI that needs an account and so on.” / “The product is not another agile backlog product tool.” / “Spec driven is a great tool but has its own place and time.”

### Contradictions
No contradictory content found.

## Behavioral Rules
- Extract meaning from “all available data” to generate key product documents (strategy, vision, business case, product charter) as a unified “product description.”
- Ensure users can “rely on the quality” of the product definition “without any required action.”
- Guard alignment across the generated output documents.
- Validate feature requests against the product description.
- Detect changes (CRUD) in product input files and perform “product description guarding.”
- Produce outputs in both Markdown and generated HTML.

### Confidence
Medium

**Evidence:** “The product will create strategic, product vision, product charter documents that are created by extracting the meaning from all available data.” / “making sure they can rely on the quality of this product definition without any required action” / “The product will guard alignment between all mentioned output documents” / “The product will validate feature requests against the product description.” / “If there is any change (crud) detected in product input files” / “These are written both in markdown as in a generated html page”

### Contradictions
No contradictory content found.

## Making Rules
- Resolve trade-offs in favor of outcome definition over output generation.
- Prefer integration/invisibility over building a new standalone UI/app experience.
- Prefer concise product definitions over extensive descriptions.

### Confidence
Medium

**Evidence:** “Defining outcomes is very important. More important than output.” / “Wherever possible the product should integrate within existing tools and workflows.” / “Wherever we can make the product invisible we will do that.” / “need a very concise product definition.”

### Contradictions
No contradictory content found.

## Product Character
- “Invisible” and low-friction (fits existing workflows; minimal UI/account burden).
- Concise, clarity-oriented, and confidence-building (quick verification/feedback for stakeholders; reliable quality).

### Confidence
Medium

**Evidence:** “Wherever we can make the product invisible we will do that.” / “provide stakeholders a way to quickly verify a feature requests possibility.→give clarity and quick feedback.” / “rely on the quality of this product definition”

### Contradictions
No contradictory content found.

## Language and Tone
Not found

### Confidence
High

**Evidence:** No supporting evidence found

### Contradictions
No contradictory content found.

## Evolution Constraints
- Growth should favor integration with existing tools/workflows rather than expanding into a standalone app with accounts/UI.
- Product should remain oriented to improving quality/context and outcomes (vs drifting to “output” or purely spec-driven workflows).

### Confidence
Low

**Evidence:** “should not be an additional app with an UI that needs an account” / “Wherever possible the product should integrate within existing tools and workflows.” / “Output over outcome… it must be the other way around.” / “Spec driven is a great tool but has its own place and time.”

### Contradictions
No contradictory content found.

## Integrity Checks
- Check whether an idea/feature request aligns with the product definition (validation against product description).
- Guard alignment across generated documents (consistency check implied).

### Confidence
Medium

**Evidence:** “providing a way for them to check whether any idea aligns with the product definition” / “The product will guard alignment between all mentioned output documents” / “The product will validate feature requests against the product description.”

### Contradictions
No contradictory content found.

### Completeness

Partial

### Strength

Medium

## Suggestion
- Define explicit decision rules for conflicts (e.g., what wins when source files contradict, recency vs authority, stakeholder priority).
- Specify concrete integrity checks and acceptance criteria (e.g., consistency rules across strategy/vision/charter, required fields, confidence thresholds, audit trail).
- Add explicit language/tone standards for generated documents (concise length limits, reading level, voice, terminology).
- Clarify evolution constraints as enforceable guardrails (e.g., “no standalone UI/login,” “must be embeddable,” “must reduce cognitive load,” measurable UX constraints).
- Define behavioral rules for change detection workflows (what triggers regeneration, what is incremental vs full rebuild, notification/approval requirements).