## Core Principles
- Conversation-first interaction as the default; avoid traditional screens where possible.
- Actions over insights; prioritize telling users what to do rather than showing charts/reporting.
- Automation by default; the system captures and updates without requiring manual data entry.

**Confidence:** High

**Evidence:** “conversation first, always… everything through chat / language, no screens if we can avoid it”; “actions > insights… avoid anything that looks like reporting”; “automation by default… system should just capture stuff… if user has to fill fields → something went wrong”.

**Contradictions:** No contradictory content found.

## Product Boundaries
The product is explicitly not intended to become a traditional CRM with dashboards, heavy reporting/BI, manual data input, or endless customization.

**Confidence:** High

**Evidence:** “what we are not… not a reporting tool… not BI… not a place to input data… not something you customize endlessly… basically not another version of Salesforce”; “We’re intentionally not doing: traditional screens… analytics dashboards… manual pipeline management”.

**Contradictions:** No contradictory content found.

## Behavioral Rules
- System should suggest next actions (ideally even before the user asks) and provide prioritized actions.
- Keep updates/logging invisible in the background (emails/calls, pipeline updates).
- Reduce choices; avoid presenting many options.
- If asked “why this?”, provide a short explanation rather than a report.
- Zero/near-zero data entry; if the user must type into fields, it indicates failure.

**Confidence:** High

**Evidence:** “system suggests actions before you ask (ideally)”; “everything updates in background, invisible”; “reduce choices, don’t give users 10 options”; “if you ask ‘why this?’ → short explanation, not a report”; “if user has to fill fields → something went wrong”; “emails + calls captured automatically… deal stage updated without asking user… basically zero data entry”.

**Contradictions:** No contradictory content found.

## Decision-Making Rules
Feature/tradeoff gut checks prioritize removing UI and input, and ensuring every element directly drives immediate action.
- Prefer removing a screen instead of adding one.
- Only build things that help someone take action immediately.
- Reduce required user input.
- If it doesn’t lead to action, it likely shouldn’t exist.
- If it starts looking like a traditional CRM again, that indicates drift.

**Confidence:** High

**Evidence:** “decision rules (gut checks): can we remove a screen instead of adding one… does this help someone take action immediately… can we reduce input here… if it doesn’t lead to action → probably shouldn’t exist”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”.

**Contradictions:** No contradictory content found.

## Product Character
Should feel focused, direct, calm, and (slightly) decisive—almost telling you what to do. Target emotional outcome: calm/clear/in-control rather than stressed/guilty.

**Confidence:** High

**Evidence:** “product should feel like… focused… direct… calm… a bit decisive”; “ideal state = calm, clear, just doing the next thing”.

**Contradictions:** No contradictory content found.

## Language and Tone
Use short, direct language; avoid hype/praise and buzzwords. Prefer action phrasing over status/analytics phrasing.

**Confidence:** High

**Evidence:** “tone / language… short, direct… no hype / no ‘you’re crushing it’… no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’”.

**Contradictions:** No contradictory content found.

## Evolution Constraints
Avoid drifting into traditional CRM patterns (tabs, dashboards, traditional screens). Aim for “invisible” CRM over time (present but not cognitively demanding).

**Confidence:** Medium

**Evidence:** “if we start adding tabs + dashboards we’re probably drifting”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “CRM should become kind of invisible over time”.

**Contradictions:** No contradictory content found.

## Integrity Checks
Heuristic/failure conditions are defined:
- If users need training, the product has likely failed.
- If users have to fill fields/type data into fields, something went wrong/they failed the goal.
- If it doesn’t lead to action, it probably shouldn’t exist.
- If it starts resembling a traditional CRM, they’ve “lost the plot.”

**Confidence:** High

**Evidence:** “If someone needs training, we probably failed”; “if user has to fill fields → something went wrong”; “if it doesn’t lead to action → probably shouldn’t exist”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”.

**Contradictions:** No contradictory content found.

### Completeness

Complete → all core elements clearly present

### Strength

High → clear, enforceable, actionable

## Suggestion
- Define explicit exceptions/escape hatches (e.g., when a “screen” is allowed, what minimum “why this” explanation must contain).
- Add a small set of measurable acceptance checks (e.g., max steps to execute an action; % activities auto-captured; max time-to-first-value).
- Clarify how the system behaves under uncertainty (missing data, conflicting signals) while staying “decisive.”
- Specify privacy/security boundaries for “capture automatically” (what sources, what consent model) to protect long-term integrity.
- Document “drift signals” more concretely (e.g., examples of forbidden UI patterns beyond “tabs/dashboards”).