## Core Principles
- Conversation-first as the default interaction model; avoid traditional screens where possible.
- Prioritize actions/execution over insights/reporting.
- Automation by default; the system should capture/update without user data entry.
- Reduce cognitive load by minimizing choices/decisions and removing “searching/updating/deciding.”

### Confidence
High

**Evidence:** “conversation first, always”; “actions > insights”; “automation by default”; “We need to to reduce cognitive load, not just time”; “remove searching → remove updating → remove deciding.”

### Contradictions
No contradictory content found.

## Product Boundaries
The product is explicitly not meant to be a traditional CRM UX (tabs/screens), not a reporting/BI tool, not a place for manual data input, and not an endlessly customizable platform (i.e., “not another version of Salesforce”).

### Confidence
High

**Evidence:** “We’re intentionally not doing: traditional screens; analytics dashboards (at least not upfront); manual pipeline management”; “not a reporting tool”; “not BI”; “not a place to input data”; “not something you customize endlessly”; “basically not another version of Salesforce.”

### Contradictions
No contradictory content found.

## Behavioral Rules
- The system should tell the user what to do next (ideally proactively), with prioritized actions.
- Actions should be executable immediately from the conversational interface (minimal steps).
- Logging (emails/calls) happens automatically; pipeline updates happen in the background.
- If the user has to fill fields/manual-update, that indicates failure.
- If the user asks “why this?”, provide a short explanation (not a report).
- Reduce choices; don’t offer many options.

### Confidence
High

**Evidence:** “system suggests actions before you ask (ideally)”; “get list of actions already prioritized”; “action executes immediately”; “everything logs automatically in background”; “pipeline updates itself”; “if user has to fill fields → something went wrong”; “if you ask ‘why this?’ → short explanation, not a report”; “reduce choices, don’t give users 10 options.”

### Contradictions
No contradictory content found.

## Making Rules
- Prefer removing screens over adding them.
- Only build features that help someone take action immediately.
- Prefer reducing user input; if it doesn’t lead to action, it probably shouldn’t exist.
- “If someone needs training, we probably failed” (usability is a decision constraint).

### Confidence
High

**Evidence:** “decision rules (gut checks)”; “can we remove a screen instead of adding one”; “does this help someone take action immediately”; “can we reduce input here”; “if it doesn’t lead to action → probably shouldn’t exist”; “If someone needs training, we probably failed.”

### Contradictions
No contradictory content found.

## Product Character
Should feel focused, direct, calm, and a bit decisive (tells you what to do). Should not feel analytical, busy/cluttered, gamified, or overly configurable. Overall aim: “invisible” tool that “disappears.”

### Confidence
High

**Evidence:** “product should feel like: focused; direct; calm; a bit decisive”; “should NOT feel like: analytical tool; busy / cluttered; gamified; overly configurable”; “Feels like CRM should become kind of invisible over time”; “The best tools disappear—they don’t feel like tools.”

### Contradictions
No contradictory content found.

## Language and Tone
Use short, direct language; avoid hype/praise-y tone and buzzwords. Prefer imperative action phrasing (e.g., “call these 3 deals”) over analytical/metric phrasing.

### Confidence
High

**Evidence:** “tone / language… short, direct”; “no hype / no ‘you’re crushing it’ type stuff”; “no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’.”

### Contradictions
No contradictory content found.

## Evolution Constraints
Avoid drifting into traditional CRM patterns; adding tabs/dashboards or looking like a traditional CRM indicates the product is off-course. Analytics dashboards are explicitly deprioritized “at least not upfront.”

### Confidence
Medium

**Evidence:** “if we start adding tabs + dashboards we’re probably drifting”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “analytics dashboards (at least not upfront).”

### Contradictions
No contradictory content found.

## Integrity Checks
Implied “failure conditions” and gut checks are used to validate changes: if a change adds screens, increases manual input, adds non-actionable/reporting features, or requires user training, it violates the charter.

### Confidence
Medium

**Evidence:** “decision rules (gut checks)”; “if user has to fill fields → something went wrong”; “If someone needs training, we probably failed”; “if it doesn’t lead to action → probably shouldn’t exist”; “if we start adding tabs + dashboards we’re probably drifting.”

### Contradictions
No contradictory content found.

### Completeness

Partial

### Strength

Medium

## Suggestion
- Convert the “gut checks” into explicit release/PR acceptance criteria (e.g., checklist that must pass before shipping).
- Define a clear exception policy for when (if ever) screens/dashboards are allowed (“at least not upfront” is ambiguous).
- Add explicit decision rules for conflicts (e.g., speed vs accuracy, automation vs user control, proactive suggestions vs user trust).
- Specify minimal required transparency/explainability for recommendations (beyond “short explanation”) to protect user trust.
- Add measurable integrity metrics tied to charter (e.g., max number of steps per action, % activities auto-logged, zero required fields).