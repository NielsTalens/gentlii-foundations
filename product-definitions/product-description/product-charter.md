## Core Principles
- Conversation-first interface as the default/primary mode; avoid traditional screens when possible.
- Actions over insights: prioritize telling the user what to do next over showing analytics or reports.
- Automation by default: the system should capture and update data without asking the user to do manual entry.
- Reduce cognitive load: minimize choices and decision-making required from the user; “minimal thinking required.”
- The product should “disappear”/feel invisible over time (low-friction, not tool-like).

### Confidence
High

**Evidence:** “conversation first, always… everything through chat / language, no screens if we can avoid it”; “actions > insights… avoid anything that looks like reporting”; “automation by default… system should just capture stuff, not ask”; “We need to reduce cognitive load, not just time”; “One interface (chat) / One output (next action) / Minimal thinking required”; “The best tools disappear—they don’t feel like tools.”

### Contradictions
No contradictory content found.

## Product Boundaries
- Not a reporting/BI/analytics-first product (especially not “upfront”).
- Not a place for manual data input/field-filling.
- Not something endlessly customizable; explicitly “not another version of Salesforce.”
- Not traditional CRM navigation patterns: avoid tabs, dashboards, pipelines, and “traditional screens.”

### Confidence
High

**Evidence:** “what we are not… not a reporting tool… not BI… not a place to input data… not something you customize endlessly… basically not another version of Salesforce”; “We’re intentionally not doing: traditional screens; analytics dashboards (at least not upfront); manual pipeline management”; “if we start adding tabs + dashboards we’re probably drifting.”

### Contradictions
No contradictory content found.

## Behavioral Rules
- Provide “next best action” (and ideally suggest actions proactively before the user asks).
- Rank/prioritize actions so “no thinking required.”
- Execute actions quickly via chat commands (e.g., send, call, schedule).
- Auto-log activities (calls/emails) and update pipeline/deal stage in the background.
- If the user must fill fields / do “after work,” that indicates failure.
- When asked “why this?”, give a short explanation, not a report.
- Reduce choices; avoid presenting many options.

### Confidence
High

**Evidence:** “tell you your next best action”; “system suggests actions before you ask (ideally)”; “get list of actions already prioritized”; “user clicks or replies in chat: ‘send this’ / ‘call now’ / ‘schedule’… action executes immediately”; “everything logs automatically in background… pipeline updates itself”; “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed”; “if you ask ‘why this?’ → short explanation, not a report”; “reduce choices, don’t give users 10 options.”

### Contradictions
No contradictory content found.

## Making Rules
- Prefer removing screens over adding them.
- A feature should exist only if it leads directly to immediate user action/execution.
- Prefer reducing user input and manual steps; if it increases data entry or choice overload, it’s likely wrong.
- “If someone needs training, we probably failed” acts as a decision heuristic against complexity.

### Confidence
High

**Evidence:** “decision rules (gut checks): can we remove a screen instead of adding one”; “does this help someone take action immediately”; “can we reduce input here”; “if it doesn’t lead to action → probably shouldn’t exist”; “If someone needs training, we probably failed.”

### Contradictions
No contradictory content found.

## Product Character
- Should feel: focused, direct, calm, and somewhat decisive (“almost telling you what to do”).
- Should create an emotional outcome of calm/clarity and control (reduce stress/guilt associated with CRM).
- Should not feel: analytical, busy/cluttered, gamified, or overly configurable.

### Confidence
High

**Evidence:** “product should feel like… focused… direct… calm… a bit decisive”; “ideal state = calm, clear, just doing the next thing”; “should NOT feel like: analytical tool; busy / cluttered; gamified; overly configurable.”

### Contradictions
No contradictory content found.

## Language and Tone
- Use short, direct language.
- Avoid hype, cheerleading, and buzzwords.
- Prefer action-oriented phrasing (“call these 3 deals”) over status/metrics phrasing (“pipeline health improved”).

### Confidence
High

**Evidence:** “tone / language… short, direct”; “no hype / no ‘you’re crushing it’ type stuff”; “no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’.”

### Contradictions
No contradictory content found.

## Evolution Constraints
- If the product starts resembling traditional CRM (tabs, dashboards, traditional screens), treat it as drift/failure (“lost the plot”).
- Avoid introducing analytics dashboards early (“at least not upfront”).
- Scope discipline: “Not trying to boil the ocean here” (implies constrained initial focus).

### Confidence
Medium

**Evidence:** “if we start adding tabs + dashboards we’re probably drifting”; “random note: if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “analytics dashboards (at least not upfront)”; “Not trying to boil the ocean here.”

### Contradictions
No contradictory content found.

## Integrity Checks
- Change/feature gut-checks: remove screens vs add; leads to immediate action; reduces input; if it doesn’t lead to action it shouldn’t exist.
- Usability check: if users need training, the design failed.
- Data-entry check: if users must fill fields/type into fields, the product failed.

### Confidence
High

**Evidence:** “decision rules (gut checks)… remove a screen… help someone take action immediately… reduce input… if it doesn’t lead to action → probably shouldn’t exist”; “If someone needs training, we probably failed”; “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed.”

### Contradictions
No contradictory content found.

### Completeness

Partial

### Strength

High

## Suggestion
- Define explicit exceptions/escape hatches (e.g., when a “screen” is allowed, what minimal analytics are acceptable, and under what user roles/situations).
- Add concrete integrity tests with measurable thresholds (e.g., max steps/time-to-execute an action; “zero manual entry” definition; allowable number of choices per prompt).
- Specify decision ownership and tie-breakers when principles conflict (e.g., automation vs user control/consent; speed vs accuracy).
- Clarify evolution policy beyond dashboards (e.g., rules for introducing voice, integrations, and configuration without becoming “endlessly customizable”).
- Document minimum explanation standard for “why this?” (what constitutes “short explanation” and what is forbidden “reporting”).