## Core Principles
- Conversation-first (always); run everything through chat/language and avoid screens.
- Actions over insights; prioritize telling users what to do over charts/reporting.
- Automation by default; the system should capture/update without asking the user for manual input.

**Confidence:** High

**Evidence:** “conversation first, always… everything through chat / language, no screens if we can avoid it”; “actions > insights… avoid anything that looks like reporting”; “automation by default… system should just capture stuff, not ask… if user has to fill fields → something went wrong”

**Contradictions:** No contradictory content found.

## Product Boundaries
Not a reporting/BI tool; not a data-entry destination; not endlessly customizable; not another Salesforce; avoid traditional screens, dashboards, and manual pipeline management (especially upfront).

**Confidence:** High

**Evidence:** “what we are not… not a reporting tool… not BI… not a place to input data… not something you customize endlessly… basically not another version of Salesforce”; “We’re intentionally not doing: traditional screens… analytics dashboards (at least not upfront)… manual pipeline management”

**Contradictions:** No contradictory content found.

## Behavioral Rules
- Suggest next actions proactively (ideally before being asked) and prioritize/rank them to reduce user thinking.
- Keep everything updating/logging invisibly in the background; “zero data entry” and no “after work.”
- If the user asks “why,” provide a short explanation (not a report).
- Reduce choices; don’t present many options; emphasize immediate execution.

**Confidence:** High

**Evidence:** “system suggests actions before you ask (ideally)”; “ideally ranked / prioritized so no thinking required”; “everything updates in background, invisible”; “everything logs automatically in background… pipeline updates itself”; “if you ask ‘why this?’ → short explanation, not a report”; “reduce choices, don’t give users 10 options”; “basically zero data entry”

**Contradictions:** No contradictory content found.

## Decision-Making Rules
Use gut-checks that favor removing screens, reducing user input, and ensuring every feature drives immediate action; if it doesn’t lead to action, it likely shouldn’t exist.

**Confidence:** High

**Evidence:** “decision rules (gut checks)… can we remove a screen instead of adding one… does this help someone take action immediately… can we reduce input here… if it doesn’t lead to action → probably shouldn’t exist”

**Contradictions:** No contradictory content found.

## Product Character
Should feel focused, direct, calm, and a bit decisive (almost telling you what to do); aim for an “invisible” CRM that helps users feel in control and not overwhelmed.

**Confidence:** High

**Evidence:** “product should feel like… focused… direct… calm… a bit decisive”; “Feels like CRM should become kind of invisible over time”; “ideal state = calm, clear, just doing the next thing”; “to feel in control of their pipeline… not feel overwhelmed”

**Contradictions:** No contradictory content found.

## Language and Tone
Use short, direct language; avoid hype, buzzwords, and congratulatory/gamified phrasing. Prefer action-oriented directives over analytic status statements.

**Confidence:** High

**Evidence:** “tone / language… short, direct… no hype / no ‘you’re crushing it’… no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’”

**Contradictions:** No contradictory content found.

## Evolution Constraints
Avoid drifting into traditional CRM patterns (tabs, dashboards, traditional screens); if it starts looking like a traditional CRM again, that indicates losing direction.

**Confidence:** High

**Evidence:** “if we start adding tabs + dashboards we’re probably drifting”; “random note… if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “analytics dashboards (at least not upfront)”

**Contradictions:** No contradictory content found.

## Integrity Checks
Treat presence of manual field-filling/data entry as a failure condition; use drift checks (adding screens/dashboards, becoming traditional CRM) as signals the product is off-course.

**Confidence:** High

**Evidence:** “if user has to fill fields → something went wrong”; “If someone needs training, we probably failed”; “if we start adding tabs + dashboards we’re probably drifting”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”

**Contradictions:** No contradictory content found.

### Completeness

Complete → all core elements clearly present

### Strength

High → clear, enforceable, actionable

## Suggestion
- Define explicit exceptions/overrides for “decisive” recommendations (e.g., when to ask the user vs auto-execute) to prevent unsafe or unwanted actions.
- Add a small set of acceptance checks for “actions > insights” (e.g., what minimal context is required with every suggested action).
- Clarify how “short explanation, not a report” should look (max length, allowable data points, and when to link details).
- Specify boundaries for “not configurable endlessly” (what is configurable vs intentionally fixed).
- Add explicit privacy/security integrity rules for automatic logging and background updates (what can/can’t be captured automatically).