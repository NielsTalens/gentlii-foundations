## Core Principles
- Conversation-first interface: do everything through chat/language and avoid traditional screens.
- Actions over insights: prioritize telling users what to do next over charts/analytics/reporting.
- Automation by default: the system captures/logs/updates in the background; manual data entry indicates failure.
- Reduce cognitive load and decision burden: “minimal thinking required,” reduce choices, remove searching/updating/deciding.

### Confidence
High

**Evidence:** “conversation first, always… everything through chat / language, no screens if we can avoid it”; “actions > insights”; “automation by default… if user has to fill fields → something went wrong”; “reduce cognitive load”; “One interface (chat) One output (next action) Minimal thinking required”; “remove searching… remove updating… remove deciding”.

### Contradictions
No contradictory content found.

## Product Boundaries
- Not a reporting/BI/analytics dashboard product (especially not upfront).
- Not a manual data-entry system; not a place to input data.
- Not an endlessly customizable CRM; explicitly not “another version of Salesforce.”
- Not traditional CRM screens/tabs/pipelines/dashboards as the primary mode.

### Confidence
High

**Evidence:** “We’re intentionally not doing: traditional screens; analytics dashboards (at least not upfront); manual pipeline management”; “what we are not… not a reporting tool… not BI… not a place to input data… not something you customize endlessly… basically not another version of Salesforce”.

### Contradictions
No contradictory content found.

## Behavioral Rules
- System provides “next best action” and ideally suggests actions before the user asks.
- Actions are ranked/prioritized to reduce thinking.
- Execution is immediate from the conversational interface (e.g., “send this” / “call now” / “schedule”).
- Automatic capture/logging of emails and calls; pipeline updates itself in the background.
- If a user has to type into fields / do “after work,” the design has failed.
- When asked “why this?”, provide a short explanation (not a report).
- Reduce options; avoid giving users many choices.

### Confidence
High

**Evidence:** “system suggests actions before you ask (ideally)”; “tell you your next best action”; “get list of actions already prioritized so no thinking required”; “action executes immediately… everything logs automatically in background… pipeline updates itself… no extra steps, no ‘after work’”; “if user has to type things in fields, we probably failed”; “if you ask ‘why this?’ → short explanation, not a report”; “reduce choices, don’t give users 10 options”.

### Contradictions
No contradictory content found.

## Making Rules
- Prefer removing a screen over adding one.
- A feature should help someone take action immediately; if it doesn’t lead to action, it “probably shouldn’t exist.”
- Prefer reducing required user input; if input is needed, treat it as a problem to eliminate.
- Use “drift checks”: if the product starts adding tabs/dashboards or looks like a traditional CRM, the team is “drifting” / has “lost the plot.”

### Confidence
High

**Evidence:** “decision rules (gut checks) ● can we remove a screen instead of adding one ● does this help someone take action immediately… ● can we reduce input here ● if it doesn’t lead to action → probably shouldn’t exist”; “if we start adding tabs + dashboards we’re probably drifting”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”.

### Contradictions
No contradictory content found.

## Product Character
- Should feel focused, direct, calm, and decisively action-guiding (“almost telling you what to do”).
- Should create an emotional state of “calm, clear” and “in control,” reducing stress/guilt associated with CRM admin.

### Confidence
High

**Evidence:** “product should feel like… focused… direct… calm… a bit decisive (almost telling you what to do)”; “ideal state = calm, clear, just doing the next thing”; “to feel in control… not feel overwhelmed… not feel like they’re doing admin work”.

### Contradictions
No contradictory content found.

## Language and Tone
- Use short, direct language.
- Avoid hype/cheerleading (“no ‘you’re crushing it’”), and avoid buzzwords.
- Prefer action-instruction phrasing (e.g., “call these 3 deals”) over analytic status statements (e.g., “pipeline health improved”).

### Confidence
High

**Evidence:** “tone / language… short, direct ● no hype / no ‘you’re crushing it’… ● no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’”.

### Contradictions
No contradictory content found.

## Evolution Constraints
- Avoid reintroducing traditional CRM elements (tabs, dashboards, traditional screens); treat this as product drift.
- Analytics dashboards are explicitly deferred (“at least not upfront”).
- “Maybe voice later” indicates voice is optional/secondary to chat-first initially.

### Confidence
Medium

**Evidence:** “if we start adding tabs + dashboards we’re probably drifting”; “analytics dashboards (at least not upfront)”; “Probably chat based, maybe voice later”.

### Contradictions
No contradictory content found.

## Integrity Checks
- If users need training, that indicates failure (onboarding should be “nonexistent or very fast”).
- If users must manually fill fields/type data, that indicates failure.
- If a change adds screens/tabs/dashboards or looks like a traditional CRM, that indicates drift/failure against principles.
- If a proposed feature doesn’t directly lead to an executable action, it should be rejected.

### Confidence
High

**Evidence:** “If someone needs training, we probably failed.”; “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed”; “if we start adding tabs + dashboards we’re probably drifting”; “if it doesn’t lead to action → probably shouldn’t exist”.

### Contradictions
No contradictory content found.

### Completeness

Partial

### Strength

High

## Suggestion
- Define explicit exception handling for automation (e.g., when the system is unsure about deal stage/logging, what is the allowed minimal user confirmation flow).
- Add a small set of measurable acceptance tests for “conversation-first” (e.g., maximum number of non-chat screens allowed; rules for when a UI element is permitted).
- Specify decision policy when “fast execution” conflicts with correctness/compliance (e.g., approvals, audit trails for sending messages, data privacy).
- Clarify evolution rules for analytics: what minimal “explanations” are allowed without becoming “reporting,” and when (if ever) dashboards can be introduced.
- Add integrity checks around trust and accuracy (e.g., required confidence thresholds or user-review prompts before auto-updating pipeline stages).