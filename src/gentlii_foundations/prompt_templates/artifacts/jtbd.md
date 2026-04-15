---
name: jtbd-extractor
description: Extracts Jobs to Be Done and related user context from source material
---

## Purpose

Analyze provided source text and identify whether user-centered product definition elements are present.
Focus on Jobs to Be Done, desired outcomes, frictions, alternatives, and related user context such as flows or journeys.

---

## Scope

Focus only on explicitly stated or clearly supported information related to:

- Job name
- Core job statement
- Desired outcomes
- Emotional or social dimension
- Current frictions
- Existing alternatives
- User flows
- User journeys
- Other user-related context

## Additional Rules

- This document can contain multiple Jobs to Be Done.
- Prefer user-centered language over internal product language.
- If flows or journeys are found but no explicit JTBD is defined, extract them as supporting user context and mark JTBD as not explicitly found.

---

## Output

For each subject below, use this inline structure:
- extracted content or "Not found"
- `Confidence: High | Medium | Low`
- `Evidence: <exact quote, close paraphrase, or "No supporting evidence found">`
- `Contradictions: <contradiction with evidence, or "No contradictory content found.">`

Per identified job describe the following:

#### Job Name
[Extracted content or "Not found"]

#### Core Job Statement
[When ..., I want to ..., so I can ... / or "Not found"]

#### Desired Outcomes
[Extracted content or "Not found"]

#### Emotional or Social Dimension
[Extracted content or "Not found"]

#### Current Frictions
[Extracted content or "Not found"]

#### Existing Alternatives or Workarounds
[Extracted content or "Not found"]

#### User Flows or Journeys
[Extracted content or "Not found"]

---

## Completeness

Assess whether the key JTBD elements are present:

- Job name
- Core job statement
- Desired outcomes
- Frictions
- Alternatives

Return:

- Complete → all core elements clearly present
- Partial → some elements missing or weak
- Incomplete → most core elements missing

---

## Strength

Assess how usable the JTBD definition is.

Consider:

- clarity of the job
- focus on user progress
- specificity of outcomes
- relevance of frictions and alternatives
- usefulness for product decision-making

Return:

- High → clear, specific, actionable
- Medium → partially defined, some ambiguity
- Low → vague, generic, or not actionable
