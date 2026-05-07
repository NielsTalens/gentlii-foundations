## Core Principles
- Conversation-first interface: default to chat/language interaction and avoid traditional screens when possible.
- Actions over insights: prioritize telling users what to do next over charts, reporting, or “viewing.”
- Automation by default: the system should capture/log/update in the background; user data entry is treated as a failure state.
- Reduce cognitive load/decisions: minimize choices and thinking required; provide a single clear output (next action).
- “Invisible tool” aspiration: the best experience is that it “disappears” and users just act.

### Confidence
High

**Evidence:** “conversation first, always… everything through chat / language, no screens if we can avoid it”; “actions > insights”; “automation by default… system should just capture stuff, not ask”; “reduce choices, don’t give users 10 options”; “One interface (chat) One output (next action) Minimal thinking required”; “The best tools disappear—they don’t feel like tools.”

### Contradictions
Customer event notes indicate users want “more insights” and “create their own dashboards,” which conflicts with “actions > insights,” “avoid anything that looks like reporting,” and “not a reporting tool / not BI.”

## Product Boundaries
- Not a reporting/BI tool; avoid analytics dashboards (at least initially).
- Not a place for manual data entry (fields), nor manual pipeline management.
- Not endlessly customizable; explicitly “not another version of Salesforce.”
- Not traditional screen/tab/dashboard navigation.

### Confidence
High

**Evidence:** “what we are not… not a reporting tool… not BI… not a place to input data… not something you customize endlessly”; “We’re intentionally not doing: traditional screens; analytics dashboards (at least not upfront); manual pipeline management.”

### Contradictions
Customer event notes: “Users want to have more insights in the process” and “Users want to create their own dashboards,” contradicting “not a reporting tool / not BI” and “analytics dashboards (at least not upfront).”

## Behavioral Rules
- Provide “next best action” and/or proactively suggest actions before being asked; actions should be prioritized/ranked.
- Convert signals/risks into executable actions (not passive insights).
- Execute actions quickly via chat commands (e.g., send follow-up, call, schedule).
- Automatically capture/log emails and calls; generate/suggest notes; keep pipeline/deal stage updated in the background.
- Enforce “zero/near-zero data entry”: if users must fill fields, something is wrong.
- When asked “why this?”, provide a short explanation rather than a report.
- Reduce options presented to users; avoid giving many choices.

### Confidence
High

**Evidence:** “tell you your next best action”; “system suggests actions before you ask (ideally)”; “ideally ranked / prioritized so no thinking required”; “converts that into actions, not insights”; “action executes immediately… everything logs automatically in background… pipeline updates itself”; “automatic logging of emails / calls”; “deal stage updated without asking user”; “if user has to fill fields → something went wrong / if user has to type things in fields, we probably failed”; “if you ask ‘why this?’ → short explanation, not a report”; “reduce choices, don’t give users 10 options.”

### Contradictions
Customer event notes request “more insights” and “create their own dashboards,” which conflicts with the behavior of avoiding reporting/insights and focusing outputs on next actions.

## Making Rules
- Prefer removing a screen over adding one.
- Accept features only if they help users take immediate action.
- Prefer reducing user input; additions that increase data entry are suspect.
- If a feature doesn’t lead to action, it likely shouldn’t exist.
- “Training required” is treated as a product failure signal.

### Confidence
High

**Evidence:** “decision rules (gut checks): can we remove a screen instead of adding one”; “does this help someone take action immediately”; “can we reduce input here”; “if it doesn’t lead to action → probably shouldn’t exist”; “If someone needs training, we probably failed.”

### Contradictions
No contradictory content found.

## Product Character
- Should feel focused, direct, calm, and “a bit decisive” (almost telling you what to do).
- Should create an emotional outcome of calm/clear control (not overwhelm, stress, guilt).
- Should not feel analytical, busy/cluttered, gamified, or overly configurable.

### Confidence
High

**Evidence:** “product should feel like: focused; direct; calm; a bit decisive”; “users… want: to feel in control… not feel overwhelmed… ideal state = calm, clear”; “should NOT feel like: analytical tool; busy / cluttered; gamified; overly configurable.”

### Contradictions
No contradictory content found.

## Language and Tone
- Use short, direct language.
- Avoid hype/cheerleading (“you’re crushing it”) and avoid buzzwords.
- Prefer imperative action phrasing (e.g., “call these 3 deals”) over analytics language (e.g., “pipeline health improved”).

### Confidence
High

**Evidence:** “tone / language… short, direct”; “no hype / no ‘you’re crushing it’ type stuff”; “no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’.”

### Contradictions
No contradictory content found.

## Evolution Constraints
- Avoid drifting into traditional CRM patterns; adding tabs/dashboards is a warning sign.
- Analytics dashboards are explicitly deprioritized “at least not upfront.”
- Voice may come later (“maybe voice later”), implying staged expansion but keeping chat primary.

### Confidence
Medium

**Evidence:** “if we start adding tabs + dashboards we’re probably drifting”; “analytics dashboards (at least not upfront)”; “Probably chat based, maybe voice later.”

### Contradictions
Customer event notes request dashboards, which pressures the constraint to avoid dashboards/insights.

## Integrity Checks
- “If user has to fill fields / type things in fields, we probably failed” (treat as a release/change rejection criterion).
- “If it starts looking like a traditional CRM again, we’ve probably lost the plot” (drift check).
- Feature-level gut checks: remove screens vs add; must lead to immediate action; reduce input; otherwise shouldn’t exist.

### Confidence
Medium

**Evidence:** “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “decision rules (gut checks)…”

### Contradictions
Customer desire for dashboards/insights conflicts with the drift checks that warn against tabs/dashboards and reporting-like features.

### Completeness

Partial

### Strength

Medium

## Suggestion
- Define a clear policy for “insights/dashboards” requests (e.g., allowed only when directly tied to an executable next action) to resolve the explicit conflict with customer demand.
- Turn the “gut checks” into a concrete checklist/gate for shipping (e.g., max options shown, max steps to execute an action, zero required fields) with measurable thresholds.
- Specify decision logic expectations for “next best action” (priority rules, explainability baseline, when the system can be decisive vs ask clarifying questions).
- Add explicit data integrity/safety rules for automation (e.g., how to handle uncertainty in auto-logging or stage changes; when to confirm with the user).
- Clarify evolution boundaries around “voice later” and any minimum viable “screens” (what’s permitted vs forbidden) to prevent gradual reintroduction of traditional UI.