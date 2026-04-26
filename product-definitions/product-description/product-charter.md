## Core Principles
- Reduce cognitive load for product professionals by producing a concise, trusted product definition/product description.
- Prioritize outcomes and product quality over output/specs; avoid building too early without sufficient product context.
- Rely on extracted meaning from “all available data” to form core product documents and maintain alignment.

### Confidence
Medium

**Evidence:** “This product is about reducing cognitive load of product professionals.” / “The users do not need very extensive descriptions but need a very concise product definition.” / “Defining outcomes is very important. More important than output.” / “start building too early without enough product context.” / “documents that are created by extracting the meaning from all available data.”  
**Contradictions:** No contradictory content found.

## Product Boundaries
- Not an additional standalone app with a UI requiring accounts (“not an additional app with an UI that needs an account and so on”).
- Not an agile backlog tool (“not another agile backlog product tool”).
- Avoid visibility/extra surface area when possible (preference to be “invisible”).

### Confidence
High

**Evidence:** “it should not be an additional app with an UI that needs an account and so on.” / “The product is not another agile backlog product tool.” / “Wherever we can make the product invisible we will do that.”  
**Contradictions:** No contradictory content found.

## Behavioral Rules
- Integrate into existing tools/workflows wherever possible.
- Generate a “product description” set of documents (strategy, product vision, business case, product charter) from uploaded input files; output as Markdown and generated HTML.
- Run a “Product Guard” when CRUD changes are detected in input files and produce a report.
- Validate feature requests against the product description and rate whether an idea is good; provide quick clarity/feedback.
- Guard alignment between the produced documents.

### Confidence
High

**Evidence:** “Wherever possible the product should integrate within existing tools and workflows.” / “A user uploads all types of files…” / “Gentlii will use different agent to create: Strategy… Product charter” / “written both in markdown as in a generated html page” / “If there is any change (crud) detected… the Product Guard should run and create a report.” / “The product will validate feature requests against the product description.” / “The product will guard alignment between all mentioned output documents”  
**Contradictions:** No contradictory content found.

## Decision-Making Rules
- Prefer concision over extensive descriptions for the product definition.
- Prefer outcome/quality focus over output/spec-driven activity.

### Confidence
Medium

**Evidence:** “The users do not need very extensive descriptions but need a very concise product definition.” / “Defining outcomes is very important. More important than output.” / “Spec driven is a great tool but has its own place and time.”  
**Contradictions:** No contradictory content found.

## Product Character
- “Invisible” and low-friction (fits into existing workflows; not a new standalone UI/app).
- Confidence-inspiring: users should be able to “rely on the quality” without required action.

### Confidence
Medium

**Evidence:** “Wherever we can make the product invisible we will do that.” / “making sure they can rely on the quality of this product definition without any required action”  
**Contradictions:** No contradictory content found.

## Language and Tone
- Concise documentation rather than extensive descriptions.

### Confidence
Low

**Evidence:** “The users do not need very extensive descriptions but need a very concise product definition.”  
**Contradictions:** No contradictory content found.

## Evolution Constraints
- Continue to avoid becoming a standalone UI/account-based app; instead integrate into existing tools and remain “invisible” where possible.
- Avoid evolving into an agile backlog tool category.

### Confidence
Medium

**Evidence:** “should not be an additional app with an UI that needs an account” / “Wherever possible the product should integrate within existing tools and workflows.” / “The product is not another agile backlog product tool.” / “Wherever we can make the product invisible we will do that.”  
**Contradictions:** No contradictory content found.

## Integrity Checks
- On detected input-file CRUD changes, automatically run “Product Guard” and create a report.
- Validate feature requests against the product description (alignment check).
- Guard alignment between generated output documents.

### Confidence
High

**Evidence:** “If there is any change (crud) detected in product input files the the Product Guard should run and create a report.” / “The product will guard alignment…” / “The product will validate feature requests against the product description.”  
**Contradictions:** No contradictory content found.

### Completeness

Partial

### Strength

Medium

## Suggestion
- Define explicit acceptance criteria for “quality of product definition” (what facets must be present; what thresholds/score constitutes “confidently right”).
- Specify a clear decision policy when evidence conflicts across input files (recency vs source authority vs stakeholder priority).
- Add enforceable rules for concision (e.g., max length per section, required structure for product charter/vision/outcomes).
- Define what the “Product Guard report” must contain (diff summary, impacted sections, confidence changes, recommended actions).
- Clarify integration constraints (which tools/workflows are first-class targets; what “invisible” concretely means in UI/UX terms).