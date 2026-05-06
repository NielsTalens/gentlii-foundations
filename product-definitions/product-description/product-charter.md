## Core Principles
- Conversation-first interaction as the default, avoiding traditional UI where possible.
- Prioritize execution/action over insights/reporting; the primary value is telling the user what to do next.
- Automation-by-default: the system should capture and update in the background, minimizing user input and cognitive load.
- Reduce choices/decision burden for users; the system should simplify by design.

### Confidence
High

**Evidence:** “conversation first, always”; “actions > insights”; “automation by default”; “reduce choices, don’t give users 10 options”; “reduce cognitive load, not just time”; “One interface (chat) One output (next action) Minimal thinking required”

### Contradictions
No contradictory content found.

## Product Boundaries
- Not a reporting/BI/analytics-first product (especially not upfront).
- Not a traditional CRM with screens, tabs, dashboards, or manual pipeline management.
- Not a place for manual data input; if users must fill fields, that indicates failure.
- Not something “you customize endlessly” / not “another version of Salesforce.”

### Confidence
High

**Evidence:** “We’re intentionally not doing: traditional screens; analytics dashboards (at least not upfront); manual pipeline management”; “what we are not… not a reporting tool… not BI… not a place to input data… not something you customize endlessly… basically not another version of Salesforce”; “if user has to fill fields → something went wrong”

### Contradictions
No contradictory content found.

## Behavioral Rules
- The system should provide (and ideally proactively suggest) prioritized “next best actions,” minimizing browsing and searching.
- Actions should be immediately executable from the conversational interface (e.g., send/call/schedule).
- Activity logging (emails/calls) should happen automatically; pipeline updates should occur invisibly in the background.
- When asked “why this?”, provide a short explanation rather than a report.
- Design should remove searching, updating, and deciding, replacing them with clear next actions and immediate execution.

### Confidence
High

**Evidence:** “system suggests actions before you ask (ideally)”; “tell you your next best action”; “automatic logging of emails / calls”; “pipeline updates happening in the background”; “everything updates in background, invisible”; “if you ask ‘why this?’ → short explanation, not a report”; “remove searching… remove updating… remove deciding… replace it with… clear next action… immediate execution… no admin overhead”

### Contradictions
No contradictory content found.

## Making Rules
- Prefer removing a screen over adding one; adding tabs/dashboards is a sign of drift.
- Features must help a user take immediate action; if it doesn’t lead to action, it likely shouldn’t exist.
- Prefer reducing required user input; if users need training, the product has failed.

### Confidence
High

**Evidence:** “can we remove a screen instead of adding one”; “if we start adding tabs + dashboards we’re probably drifting”; “does this help someone take action immediately”; “if it doesn’t lead to action → probably shouldn’t exist”; “If someone needs training, we probably failed.”

### Contradictions
No contradictory content found.

## Product Character
The product should feel focused, direct, calm, and “a bit decisive” (almost telling the user what to do). It should feel invisible over time—more like a system that manages the work than a tool to manage.

It should not feel analytical, busy/cluttered, gamified, or overly configurable.

### Confidence
High

**Evidence:** “product should feel like: focused… direct… calm… a bit decisive”; “The best tools disappear—they don’t feel like tools.”; “CRM should become kind of invisible over time”; “should NOT feel like: analytical tool… busy / cluttered… gamified… overly configurable”

### Contradictions
No contradictory content found.

## Language and Tone
Use short, direct language with no hype, buzzwords, or cheerleading. Prefer imperative, action-oriented phrasing (e.g., “call these 3 deals”) over abstract status/analytics language.

### Confidence
High

**Evidence:** “tone / language… short, direct”; “no hype / no ‘you’re crushing it’ type stuff”; “no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’”

### Contradictions
No contradictory content found.

## Evolution Constraints
- Avoid drifting into a traditional CRM shape (screens/tabs/dashboards); if it starts looking like a traditional CRM, “we’ve probably lost the plot.”
- Analytics dashboards are explicitly deprioritized “at least not upfront.”
- Voice may be added later, but core remains conversation-first.

### Confidence
Medium

**Evidence:** “if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “analytics dashboards (at least not upfront)”; “Probably chat based, maybe voice later.”

### Contradictions
No contradictory content found.

## Integrity Checks
- “If someone needs training, we probably failed.”
- “if user has to fill fields → something went wrong” / “if user has to type things in fields, we probably failed.”
- Gut-check criteria before adding/building: remove screens, reduce input, ensure immediate action, avoid non-actionable features.

### Confidence
High

**Evidence:** “If someone needs training, we probably failed.”; “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed”; “decision rules (gut checks)…”

### Contradictions
No contradictory content found.

### Completeness

Complete → all core elements clearly present

### Strength

High → clear, enforceable, actionable

## Suggestion
- Define explicit thresholds for “minimal thinking required” (e.g., max number of suggested actions shown; when to ask clarifying questions vs decide).
- Add a clear policy for when (if ever) analytics/reporting is allowed later, so “not upfront” doesn’t become scope creep.
- Specify non-negotiable privacy/security boundaries for “automatic logging” and “invisible” background updates (what is captured, from where, and with what consent).
- Define a concrete acceptance checklist for new features (e.g., must eliminate a screen, must reduce user input, must be directly executable from chat).