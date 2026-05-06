## Core Principles
- Conversation-first interaction as the default interface; avoid traditional screens where possible.
- Prioritize action/execution over insights/analytics and reduce cognitive load/minimal thinking required.
- Automation by default: the system captures and updates data without asking the user to fill fields.
- The best experience is “invisible” tooling: CRM should “disappear” and “get out of the way.”

### Confidence
High

**Evidence:** “conversation first, always… everything through chat / language, no screens if we can avoid it”; “actions > insights”; “automation by default… system should just capture stuff, not ask”; “We need to to reduce cognitive load”; “The best tools disappear—they don’t feel like tools.”; “CRM should become kind of invisible over time.”

### Contradictions
No contradictory content found.

## Product Boundaries
- Not a reporting/BI/analytics-first tool (especially “not upfront”).
- Not a place for manual data entry; not manual pipeline management.
- Not endlessly configurable; not “another version of Salesforce.”
- Avoid traditional UI paradigms (tabs, dashboards, traditional screens).

### Confidence
High

**Evidence:** “We’re intentionally not doing: traditional screens; analytics dashboards (at least not upfront); manual pipeline management.”; “what we are not… not a reporting tool… not BI… not a place to input data… not something you customize endlessly… basically not another version of Salesforce”; “if we start adding tabs + dashboards we’re probably drifting.”

### Contradictions
No contradictory content found.

## Behavioral Rules
- System provides “next best action” and (ideally) suggests actions proactively before being asked; actions should be prioritized/ranked to reduce thinking.
- Execution should be immediate via chat commands (e.g., send/call/schedule), minimizing steps and context switching.
- Automatic capture/logging of emails and calls; pipeline updates happen in the background/invisible.
- If users must type into fields/manual updates, it indicates failure.
- When asked “why this?”, provide a short explanation (not a report) and reduce choices (don’t give 10 options).

### Confidence
High

**Evidence:** “tell you your next best action”; “system suggests actions before you ask (ideally)”; “get list of actions already prioritized so no thinking required”; “user clicks or replies in chat: ‘send this’ / ‘call now’ / ‘schedule’… action executes immediately”; “everything logs automatically in background… pipeline updates itself”; “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed”; “if you ask ‘why this?’ → short explanation, not a report”; “reduce choices, don’t give users 10 options.”

### Contradictions
No contradictory content found.

## Making Rules
- Prefer removing a screen over adding one; adding tabs/dashboards is a drift signal.
- Features must help someone take action immediately; if it doesn’t lead to action, it “probably shouldn’t exist.”
- Prefer reducing user input; if it requires field-filling, something went wrong.
- Training is an anti-goal; need for training implies failure.

### Confidence
High

**Evidence:** “decision rules (gut checks): can we remove a screen instead of adding one”; “does this help someone take action immediately”; “if it doesn’t lead to action → probably shouldn’t exist”; “can we reduce input here”; “If someone needs training, we probably failed.”

### Contradictions
No contradictory content found.

## Product Character
The product should feel focused, direct, calm, and a bit decisive—almost telling the user what to do. It should help users feel in control, not overwhelmed, and avoid the stress/guilt associated with traditional CRMs.

### Confidence
High

**Evidence:** “product should feel like: focused; direct; calm; a bit decisive”; “users… want: to feel in control… not feel overwhelmed”; “ideal state = calm, clear, just doing the next thing.”

### Contradictions
No contradictory content found.

## Language and Tone
Use short, direct language; avoid hype, buzzwords, and congratulatory/gamified phrasing. Prefer action-imperative phrasing (e.g., “call these 3 deals”) over analytical status statements.

### Confidence
High

**Evidence:** “tone / language… short, direct”; “no hype / no ‘you’re crushing it’ type stuff”; “no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’.”

### Contradictions
No contradictory content found.

## Evolution Constraints
Avoid evolving into a traditional CRM (screens/tabs/dashboards); if it starts looking like one, the product has “lost the plot.” Analytics dashboards are explicitly deprioritized “at least not upfront,” implying sequencing constraints (execution first).

### Confidence
Medium

**Evidence:** “if we start adding tabs + dashboards we’re probably drifting”; “random note: if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “analytics dashboards (at least not upfront).”

### Contradictions
No contradictory content found.

## Integrity Checks
Use the stated “gut checks” as acceptance tests for changes: remove screens vs add; action-immediacy; reduced input; reject features that don’t lead to action. Treat “needs training” and “user has to fill fields/type in fields” as failure conditions.

### Confidence
Medium

**Evidence:** “decision rules (gut checks)…”; “If someone needs training, we probably failed.”; “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed.”

### Contradictions
No contradictory content found.

### Completeness

Complete

### Strength

High

## Suggestion
- Define explicit non-goals around data export/import, integrations, and customization limits (what’s allowed vs “endlessly customizable”) to prevent scope creep.
- Turn the “gut checks” into a concrete pre-ship checklist (e.g., max number of choices shown, max steps to execute an action, “no new screens” rule).
- Add explicit rules for when (if ever) analytics/reporting can appear, to operationalize “not upfront” into a measurable sequencing constraint.
- Specify minimum explanation behavior for “why this?” (length, content, and what must be avoided) to keep it from becoming “a report.”
- Define a small set of measurable integrity thresholds (e.g., % activities auto-logged, % pipeline stages auto-updated, time-to-next-action) to validate “automation by default” and “minimal thinking required.”