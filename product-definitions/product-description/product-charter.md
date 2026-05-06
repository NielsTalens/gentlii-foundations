## Core Principles
- Conversation-first interaction: the primary interface is chat/language, avoiding traditional screens where possible.
- Actions over insights: prioritize telling users what to do next over reporting/analytics.
- Automation by default: the system captures and updates information without asking users to manually enter data.
- Reduce cognitive load and decision burden: minimize choices and thinking required; provide a single “next action” output.

### Confidence
High

**Evidence:** “conversation first, always… everything through chat / language, no screens if we can avoid it”; “actions > insights”; “automation by default”; “reduce cognitive load, not just time”; “One interface (chat) One output (next action) Minimal thinking required”

### Contradictions
No contradictory content found.

## Product Boundaries
The product is explicitly not:
- A reporting/analytics/BI tool (especially “not upfront”).
- A place for manual data input/field-filling.
- An endlessly customizable CRM like Salesforce.
- A traditional CRM with screens, tabs, dashboards, and manual pipeline management.

### Confidence
High

**Evidence:** “We’re intentionally not doing: traditional screens… analytics dashboards (at least not upfront) manual pipeline management”; “what we are not… not a reporting tool… not BI… not a place to input data… not something you customize endlessly… basically not another version of Salesforce”

### Contradictions
No contradictory content found.

## Behavioral Rules
- The system should provide “next best action” (ideally proactively, even before the user asks) and prioritize/rank actions to remove user decision-making.
- Background, invisible updates: automatically log emails/calls, generate/suggest notes, and keep pipeline/deal stages updated without user effort.
- Provide short justifications when asked “why,” but avoid turning explanations into reports.
- Enforce low-friction execution: actions should be executable immediately via chat commands (e.g., send/call/schedule) with “no extra steps” and no “after work.”

### Confidence
High

**Evidence:** “system suggests actions before you ask (ideally)”; “everything updates in background, invisible”; “if you ask ‘why this?’ → short explanation, not a report”; “ideally ranked / prioritized so no thinking required”; “everything logs automatically in background”; “deal stage updated without asking user”; “no extra steps, no ‘after work’”

### Contradictions
No contradictory content found.

## Making Rules
- Prefer removing screens over adding new ones; adding tabs/dashboards is treated as drift.
- Features must directly enable immediate action; if it doesn’t lead to action, it “probably shouldn’t exist.”
- Prefer reducing required user input over adding fields/steps/options.
- Reduce choices rather than expanding configuration/options.

### Confidence
High

**Evidence:** “can we remove a screen instead of adding one”; “if we start adding tabs + dashboards we’re probably drifting”; “does this help someone take action immediately”; “can we reduce input here”; “if it doesn’t lead to action → probably shouldn’t exist”; “reduce choices, don’t give users 10 options”

### Contradictions
No contradictory content found.

## Product Character
The product should feel:
- Focused, direct, calm, and decisively action-guiding (“almost telling you what to do”).
- Invisible / “disappearing” over time (present but not attention-demanding).
It should not feel:
- Like an analytical tool, busy/cluttered, gamified, or overly configurable.

### Confidence
High

**Evidence:** “product should feel like… focused… direct… calm… a bit decisive”; “Feels like CRM should become kind of invisible over time”; “should NOT feel like: analytical tool… busy / cluttered… gamified… overly configurable”

### Contradictions
No contradictory content found.

## Language and Tone
- Use short, direct language.
- Avoid hype, praise-y coaching language, and buzzwords.
- Prefer action-imperative phrasing (“call these 3 deals”) over abstract metrics language (“pipeline health improved”).

### Confidence
High

**Evidence:** “tone / language… short, direct”; “no hype / no ‘you’re crushing it’ type stuff”; “no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’”

### Contradictions
No contradictory content found.

## Evolution Constraints
- Avoid evolving toward a traditional CRM; if it starts resembling traditional CRM (screens/tabs/dashboards), it indicates failure/drift.
- Analytics dashboards are explicitly deferred (“at least not upfront”), implying sequencing constraints on adding analytics/reporting.

### Confidence
Medium

**Evidence:** “if we start adding tabs + dashboards we’re probably drifting”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “analytics dashboards (at least not upfront)”

### Contradictions
No contradictory content found.

## Integrity Checks
- “If someone needs training, we probably failed.”
- “If user has to fill fields / type things in fields, we probably failed.”
- “If it doesn’t lead to action → probably shouldn’t exist.”
- Drift check: adding tabs/dashboards or looking like a traditional CRM indicates losing direction.

### Confidence
High

**Evidence:** “If someone needs training, we probably failed.”; “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed”; “if it doesn’t lead to action → probably shouldn’t exist”; “if we start adding tabs + dashboards we’re probably drifting”

### Contradictions
No contradictory content found.

### Completeness

Complete

### Strength

High

## Suggestion

- Define explicit exceptions/escape hatches for “no screens” (e.g., compliance/export/admin settings) so teams can make consistent calls when edge cases arise.
- Add a concrete prioritization policy for “next action” (e.g., recency, deal stage risk, SLA breaches) to make “ranked/prioritized” enforceable and testable.
- Specify a minimal set of allowed “insight” outputs (if any) that are permitted only when directly tied to an executable action, to prevent analytics creep.
- Document a small set of hard acceptance tests for “invisible automation” (e.g., % of activities auto-captured; zero required fields) to operationalize integrity checks.