## Core Principles

Conversation-first interaction is the primary principle: the product should route “everything through chat/language” and avoid traditional screens where possible. The product prioritizes action over insight/reporting, and defaults to automation so the system captures and updates information without asking the user to fill fields.

**Confidence:** High

**Evidence:** “conversation first, always… everything through chat / language, no screens if we can avoid it”; “actions > insights”; “automation by default… system should just capture stuff, not ask… if user has to fill fields → something went wrong”; “Everything is more like: → action → next step → done.”

**Contradictions:** No contradictory content found.

## Product Boundaries

The product is explicitly not a reporting/BI tool, not a place for manual data input, and not an endlessly customizable Salesforce-like CRM. It avoids traditional screens/tabs/dashboards (at least initially) and avoids manual pipeline management.

**Confidence:** High

**Evidence:** “what we are not… not a reporting tool… not BI… not a place to input data… not something you customize endlessly… basically not another version of Salesforce”; “We’re intentionally not doing: traditional screens… analytics dashboards (at least not upfront)… manual pipeline management.”

**Contradictions:** No contradictory content found.

## Behavioral Rules

The system should proactively suggest prioritized next actions (ideally before the user asks), provide short explanations when questioned (not full reports), and keep everything updated invisibly in the background. It should reduce choices (avoid presenting many options), enable immediate execution of actions, and ensure activity capture and pipeline updates happen automatically; if users must type into fields, that indicates failure.

**Confidence:** High

**Evidence:** “system suggests actions before you ask (ideally)”; “if you ask ‘why this?’ → short explanation, not a report”; “everything updates in background, invisible”; “reduce choices, don’t give users 10 options”; “action executes immediately… everything logs automatically in background… pipeline updates itself”; “basically zero data entry”; “If someone needs training, we probably failed.”

**Contradictions:** No contradictory content found.

## Decision-Making Rules

Trade-offs should be resolved using “gut checks” that bias toward removing screens, reducing input, and ensuring every feature directly enables immediate action. If something does not lead to an executable action, it likely should not exist; adding tabs/dashboards is a sign of drifting toward a traditional CRM.

**Confidence:** High

**Evidence:** “decision rules (gut checks) ● can we remove a screen instead of adding one ● does this help someone take action immediately ● can we reduce input here ● if it doesn’t lead to action → probably shouldn’t exist”; “if we start adding tabs + dashboards we’re probably drifting.”

**Contradictions:** No contradictory content found.

## Product Character

The product should feel focused, direct, calm, and somewhat decisive (almost telling the user what to do). It should help users feel in control and not overwhelmed; the intended emotional outcome is “calm, clear, just doing the next thing.” It should not feel analytical, busy/cluttered, gamified, or overly configurable.

**Confidence:** High

**Evidence:** “product should feel like… focused… direct… calm… a bit decisive”; “ideal state = calm, clear, just doing the next thing”; “should NOT feel like: analytical tool… busy / cluttered… gamified… overly configurable.”

**Contradictions:** No contradictory content found.

## Language and Tone

Tone should be short and direct, avoiding hype, praise-y coaching language, and buzzwords. Prefer imperative, action-oriented phrasing (e.g., “call these 3 deals”) over status/analytics phrasing (e.g., “pipeline health improved”).

**Confidence:** High

**Evidence:** “tone / language… short, direct ● no hype / no ‘you’re crushing it’ type stuff ● no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’.”

**Contradictions:** No contradictory content found.

## Evolution Constraints

As the product evolves, it should resist becoming a traditional CRM: adding tabs, dashboards, or traditional CRM “screens” is treated as losing direction. There’s also an implied constraint to make the CRM “invisible over time,” minimizing user awareness and interaction overhead, though feasibility is noted as uncertain.

**Confidence:** Medium

**Evidence:** “if we start adding tabs + dashboards we’re probably drifting”; “random note… if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “Feels like CRM should become kind of invisible over time… Not 100% sure how far we can push that but that’s the direction.”

**Contradictions:** No contradictory content found.

## Integrity Checks

The document includes several explicit “failure”/drift signals that can be used as integrity checks: if users have to fill fields or do manual updating, something is wrong; if users need training, the product failed; if the product starts resembling traditional CRM with screens/dashboards/tabs, it has “lost the plot.”

**Confidence:** High

**Evidence:** “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed”; “If someone needs training, we probably failed”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot.”

**Contradictions:** No contradictory content found.

### Completeness

Complete

### Strength

High

## Suggestion

Add a small set of explicit acceptance checks for key experiences (e.g., “morning open,” “post-call,” “follow-up triage”) with measurable thresholds such as maximum steps/taps, maximum time-to-next-action, and a hard rule for when (if ever) limited “screens” are allowed; this would make the existing principles (conversation-first, actions>insights, automation-by-default) more enforceable during implementation and prevent gradual drift into dashboards/configuration.