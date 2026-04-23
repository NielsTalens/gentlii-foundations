## Core Principles

The product is explicitly intended to be conversation-first (chat/language as the primary interface), prioritizing actions over insights (telling users what to do next rather than showing analytics), and automating capture/updates by default so users are not maintaining the system. It also emphasizes reducing cognitive load by removing searching, updating, and deciding wherever possible.

**Confidence:** High

**Evidence:** “conversation first, always”; “actions > insights”; “automation by default”; “remove searching → remove updating → remove deciding”; “system just tells you what to do next.”

**Contradictions:** No contradictory content found.

## Product Boundaries

The product is explicitly not meant to resemble traditional CRMs: not a reporting/BI tool, not dashboard-driven, not a place for manual data input, and not endlessly configurable/customizable. It is also “intentionally not doing” traditional screens and manual pipeline management (at least initially).

**Confidence:** High

**Evidence:** “what we are not… not a reporting tool… not BI… not a place to input data… not something you customize endlessly… basically not another version of Salesforce”; “We’re intentionally not doing: traditional screens; analytics dashboards (at least not upfront); manual pipeline management.”

**Contradictions:** No contradictory content found.

## Behavioral Rules

The system should proactively suggest prioritized next actions (ideally before the user asks), provide brief explanations when challenged (without turning into a report), keep everything updated invisibly in the background, and minimize user choices/options. It should enable immediate execution of actions (send/call/schedule) and automatically log activity and update the pipeline without “after work” or manual field entry; needing training is treated as a failure signal.

**Confidence:** High

**Evidence:** “system suggests actions before you ask (ideally)”; “if you ask ‘why this?’ → short explanation, not a report”; “everything updates in background, invisible”; “reduce choices, don’t give users 10 options”; “action executes immediately”; “everything logs automatically in background”; “pipeline updates itself”; “If someone needs training, we probably failed.”; “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed.”

**Contradictions:** No contradictory content found.

## Decision-Making Rules

Feature and scope trade-offs should be decided by “gut checks” that bias toward removing screens, increasing immediate actionability, and reducing user input. If a proposed element does not lead directly to an executable action, it likely should not exist; adding tabs/dashboards is a warning sign of drifting back to traditional CRM patterns.

**Confidence:** High

**Evidence:** “decision rules (gut checks)”; “can we remove a screen instead of adding one”; “does this help someone take action immediately”; “can we reduce input here”; “if it doesn’t lead to action → probably shouldn’t exist”; “if we start adding tabs + dashboards we’re probably drifting.”

**Contradictions:** No contradictory content found.

## Product Character

The product should feel focused, direct, calm, and somewhat decisive—“almost telling you what to do.” It aims to create an emotional experience of calm and clarity (users feel in control, not overwhelmed), and the system should become “invisible over time” so users can act without thinking about the tool.

**Confidence:** High

**Evidence:** “product should feel like… focused… direct… calm… a bit decisive”; “ideal state = calm, clear, just doing the next thing”; “Feels like CRM should become kind of invisible over time.”

**Contradictions:** No contradictory content found.

## Language and Tone

Language should be short and direct, with no hype/cheerleading and no buzzwords; the interface should phrase outputs as concrete actions rather than abstract metrics.

**Confidence:** High

**Evidence:** “tone / language… short, direct”; “no hype / no ‘you’re crushing it’ type stuff”; “no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’.”

**Contradictions:** No contradictory content found.

## Evolution Constraints

The product should avoid evolving back into a traditional CRM (screens/tabs/dashboards); if it starts resembling a traditional CRM again, that indicates the product has “lost the plot.” Dashboards/analytics are explicitly deprioritized “at least not upfront,” implying sequencing constraints for future expansion.

**Confidence:** Medium

**Evidence:** “if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “analytics dashboards (at least not upfront)”; “not another version of Salesforce.”

**Contradictions:** No contradictory content found.

## Integrity Checks

There are explicit failure/health signals tied to integrity: if users must fill fields or do manual data entry, something went wrong/“we probably failed”; if training is required, that’s also treated as a failure. Drift checks include noticing when tabs/dashboards/screens are being added.

**Confidence:** High

**Evidence:** “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed”; “If someone needs training, we probably failed.”; “if we start adding tabs + dashboards we’re probably drifting.”

**Contradictions:** No contradictory content found.

### Completeness

Complete

### Strength

High

## Suggestion

Add a small set of explicit “non-negotiables” and measurable acceptance checks (e.g., maximum number of user choices presented per step, required percentage of activities auto-captured, maximum time-to-next-action on open, and a rule for when a screen is allowed at all) plus a clear exception policy for edge cases (e.g., compliance-required fields, user corrections to automated pipeline updates) so the charter remains enforceable as features expand.