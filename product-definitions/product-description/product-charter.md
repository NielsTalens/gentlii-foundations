## Core Principles
- Conversation-first as the primary interface; avoid screens where possible.
- Actions over insights; the product exists to drive immediate execution, not reporting.
- Automation by default; the system captures and updates without asking the user to fill fields.
- Reduce cognitive load by minimizing choices and decisions for the user.
- CRM should become “invisible” over time (feels like it disappears; user just acts).

### Confidence
High

**Evidence:** “conversation first, always… everything through chat / language, no screens if we can avoid it”; “actions > insights”; “automation by default… if user has to fill fields → something went wrong”; “We need to to reduce cognitive load, not just time”; “The best tools disappear—they don’t feel like tools.”; “Feels like CRM should become kind of invisible over time.”

### Contradictions
Customer feedback indicates demand for “more insights” and “create their own dashboards,” which conflicts with the principles of “actions > insights” and “avoid anything that looks like reporting.” **Evidence:** “Users want to have more insights in the process”; “Users want to create their own dashboards” vs “avoid anything that looks like reporting.”

## Product Boundaries
- Not a reporting/BI tool.
- Not a place to input data manually (avoid data entry/field filling).
- Not an endlessly customizable Salesforce-like CRM.
- Not traditional CRM UI patterns (screens/tabs/dashboards/pipeline browsing), at least initially.

### Confidence
High

**Evidence:** “what we are not… not a reporting tool… not BI… not a place to input data… not something you customize endlessly… basically not another version of Salesforce”; “We’re intentionally not doing: traditional screens; analytics dashboards (at least not upfront); manual pipeline management.”

### Contradictions
Customer feedback requesting dashboards conflicts with the “not a reporting tool / not BI” and “analytics dashboards (at least not upfront)” boundary. **Evidence:** “Users want to create their own dashboards” vs “not a reporting tool… not BI” / “analytics dashboards (at least not upfront).”

## Behavioral Rules
- System provides “next best action” and prioritizes actions to remove user decision-making.
- System should suggest actions proactively (ideally before being asked).
- If user asks “why this?”, provide a short explanation (not a report).
- Logging (emails/calls) happens automatically; pipeline updates in the background.
- Minimize choices; don’t present many options (“don’t give users 10 options”).
- If users must do training or fill fields/manual updates, that indicates product failure.

### Confidence
High

**Evidence:** “tell you your next best action”; “system suggests actions before you ask (ideally)”; “if you ask ‘why this?’ → short explanation, not a report”; “log stuff automatically (calls, emails etc.)”; “pipeline updates happening in the background”; “reduce choices, don’t give users 10 options”; “If someone needs training, we probably failed.”; “if user has to type things in fields, we probably failed.”

### Contradictions
No contradictory content found.

## Making Rules
- Prefer removing a screen over adding one.
- Features must enable immediate action; if it doesn’t lead to action, it probably shouldn’t exist.
- Reduce required user input whenever possible.
- Avoid drift toward traditional CRM patterns (tabs/dashboards).

### Confidence
High

**Evidence:** “decision rules (gut checks): can we remove a screen instead of adding one; does this help someone take action immediately; can we reduce input here; if it doesn’t lead to action → probably shouldn’t exist”; “if we start adding tabs + dashboards we’re probably drifting.”

### Contradictions
No contradictory content found.

## Product Character
- Should feel focused, direct, calm, and somewhat decisive (tells you what to do).
- Should make users feel in control, not overwhelmed; reduce stress/guilt associated with CRM.
- Should not feel analytical, busy/cluttered, gamified, or overly configurable.

### Confidence
High

**Evidence:** “product should feel like: focused; direct; calm; a bit decisive”; “ideal state = calm, clear, just doing the next thing”; “should NOT feel like: analytical tool; busy / cluttered; gamified; overly configurable.”

### Contradictions
No contradictory content found.

## Language and Tone
- Short, direct language.
- No hype/cheerleading language; no buzzwords.
- Prefer action-oriented phrasing (e.g., “call these 3 deals”) over metric/report framing.

### Confidence
High

**Evidence:** “tone / language… short, direct”; “no hype / no ‘you’re crushing it’ type stuff”; “no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’.”

### Contradictions
No contradictory content found.

## Evolution Constraints
- Avoid adding traditional screens/tabs/dashboards; adding them indicates “drifting” or “lost the plot.”
- Analytics dashboards are explicitly “not upfront” (implies a phased/limited introduction at most).
- Voice may be added later, but core remains conversation-first.

### Confidence
Medium

**Evidence:** “if we start adding tabs + dashboards we’re probably drifting”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “analytics dashboards (at least not upfront)”; “Probably chat based, maybe voice later.”

### Contradictions
Customer requests for dashboards/insights creates tension with the constraint to avoid dashboards and reporting-like features. **Evidence:** “Users want to create their own dashboards” vs “analytics dashboards (at least not upfront)” / “avoid anything that looks like reporting.”

## Integrity Checks
- “If user has to fill fields / type things in fields, we probably failed” (data-entry avoidance as a pass/fail test).
- “If someone needs training, we probably failed” (onboarding/training as an integrity signal).
- “If it starts looking like a traditional CRM again, we’ve probably lost the plot” (UI/shape drift check).
- “If it doesn’t lead to action → probably shouldn’t exist” (feature acceptance test).

### Confidence
High

**Evidence:** “if user has to fill fields → something went wrong”; “If someone needs training, we probably failed.”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “if it doesn’t lead to action → probably shouldn’t exist.”

### Contradictions
No contradictory content found.

### Completeness

Complete

### Strength

High

## Suggestion
- Define an explicit policy for handling requests for “insights/dashboards” (e.g., only action-converting insights allowed; no custom dashboards; limited “why” explanations).
- Turn “reduce choices” into a measurable rule (e.g., max number of suggested actions/options shown per step).
- Add an explicit trade-off rule for automation vs user control (when to auto-update vs when to ask for confirmation).
- Specify privacy/security boundaries for “automatic logging of emails/calls” (what is captured, stored, and shareable).
- Formalize a lightweight change-review checklist using the existing integrity checks (fields, training, actionability, screen creep).