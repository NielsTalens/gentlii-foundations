## Core Principles
- Reduce cognitive load for product professionals.
- Prioritize outcome/quality over output and avoid building too early without enough context.
- Create an “opinionated” product definition that users can trust without needing to take extra actions.

### Confidence
Medium

**Evidence:** “This product is about reducing cognitive load of product professionals.” / “Output over outcome… it must be the other way around.” / “start building too early without enough product context.” / “capture this in a opinionated product definition.” / “rely on the quality of this product definition without any required action”
  
**Contradictions:** No contradictory content found.

## Product Boundaries
- Not an additional standalone app requiring UI/account “and so on.”
- Not another agile backlog product tool.
- Avoid visibility where possible (“invisible” product), favoring integration into existing tools/workflows.

### Confidence
High

**Evidence:** “it should not be an additional app with an UI that needs an account and so on.” / “The product is not another agile backlog product tool.” / “Wherever we can make the product invisible we will do that.” / “integrate within existing tools and workflows.”
  
**Contradictions:** No contradictory content found.

## Behavioral Rules
- Accept uploads of “all types of files” that describe the product/ideas as input.
- Generate a set of documents (“product description”) including: Strategy, Product Vision, Business case, Product charter; output in Markdown and generated HTML.
- Detect CRUD changes in input files and automatically run a “Product Guard” to produce a report.
- Validate feature requests against the product description and rate/score alignment.
- Guard alignment between the generated output documents.

### Confidence
High

**Evidence:** “A user uploads all types of files…” / “Gentlii will use different agent to create: Strategy, Product Vision, Business case, Product charter” / “These are written both in markdown as in a generated html page” / “If there is any change (crud) detected… the Product Guard should run and create a report.” / “Checks features against the product description files and rates whether it is a good idea and scores it.” / “The product will guard alignment between all mentioned output documents”
  
**Contradictions:** No contradictory content found.

## Decision-Making Rules
- Prefer concise product definitions over extensive descriptions.
- Prefer “invisible” integration into existing tools/workflows over introducing a new app UI/account.
- Validate ideas/features by checking alignment with the product definition/product description.

### Confidence
Medium

**Evidence:** “The users do not need very extensive descriptions but need a very concise product definition.” / “Wherever possible… integrate within existing tools and workflows.” / “Wherever we can make the product invisible we will do that.” / “providing a way for them to check whether any idea aligns with the product definition” / “validate feature requests against the product description.”
  
**Contradictions:** No contradictory content found.

## Product Character
- Should feel “invisible” and low-friction (embedded in existing workflows).
- Should provide clarity and quick feedback to stakeholders.

### Confidence
Medium

**Evidence:** “Wherever we can make the product invisible we will do that.” / “give clarity and quick feedback.”
  
**Contradictions:** No contradictory content found.

## Language and Tone
- Outputs should be very concise (not extensive descriptions).

### Confidence
Low

**Evidence:** “The users do not need very extensive descriptions but need a very concise product definition.”
  
**Contradictions:** No contradictory content found.

## Evolution Constraints
- Grow via integration into existing tools/workflows rather than becoming a standalone app with UI/account.
- Maintain/increase “less code” improvements (optimize product improvements with less code).

### Confidence
Low

**Evidence:** “Wherever possible the product should integrate within existing tools and workflows.” / “it should not be an additional app with an UI that needs an account” / “It will improve the product with less code.”
  
**Contradictions:** No contradictory content found.

## Integrity Checks
- On detected CRUD changes to input files, run Product Guard and generate a report (implied as a gating/verification step).
- Check/validate feature requests against the product description and score whether it is a good idea.
- “Guard alignment” across strategy/vision/business case/product charter documents within the product description.

### Confidence
Medium

**Evidence:** “If there is any change (crud) detected… the Product Guard should run and create a report.” / “validate feature requests against the product description.” / “guard alignment between all mentioned output documents”
  
**Contradictions:** No contradictory content found.

### Completeness

Partial

### Strength

Medium

## Suggestion
- Define explicit decision rules for trade-offs (e.g., what wins when “concise” conflicts with “confidently right on all facets”).
- Specify measurable integrity thresholds for “quality” and “alignment” (e.g., required checks, scoring cutoffs, what blocks acceptance).
- Clarify governance of the “opinionated product definition” (who can override, how disputes are resolved, audit trail requirements).
- Add explicit tone/style guidelines for generated artifacts (structure, length limits, terminology, and intended audience per document).
- Define evolution constraints more concretely (what integrations are allowed/required; what “invisible” means operationally).