## Core Principles
The product is explicitly grounded in being conversation-first (chat/language as the primary interface), prioritizing actions over insights/reporting, and making automation the default so users don’t have to do data entry or maintenance. There is also an implied principle of minimizing friction and cognitive load: remove searching, updating, and deciding, replacing them with clear prioritized next actions and fast execution.

**Confidence:** High  
**Evidence:** “conversation first, always”; “actions > insights”; “automation by default”; “remove searching → remove updating → remove deciding”; “they want to know what to do next, clearly and they want everything to be fast (input + output)”

Contradictions: No contradictory content found.

## Product Boundaries
The product is explicitly not a traditional CRM experience with screens, tabs, dashboards, manual pipeline management, or heavy customization. It is also explicitly not a reporting/analytics/BI tool and not primarily a place for users to input data.

**Confidence:** High  
**Evidence:** “what we are not… not a reporting tool… not BI… not a place to input data… not something you customize endlessly… basically not another version of Salesforce”; “We’re intentionally not doing: traditional screens… analytics dashboards (at least not upfront)… manual pipeline management”

Contradictions: No contradictory content found.

## Behavioral Rules
The system should proactively and/or responsively provide “next best actions,” ideally suggesting actions before the user asks, and presenting them prioritized/ranked to reduce thinking. It should enable immediate execution of actions (send/call/schedule) with minimal steps, and automatically capture/log activity while keeping the pipeline updated “in the background” (invisible). It should reduce choices rather than expand them, and if a user asks “why,” it should give a short explanation rather than a report.

**Confidence:** High  
**Evidence:** “system suggests actions before you ask (ideally)”; “everything updates in background, invisible”; “reduce choices, don’t give users 10 options”; “tell you your next best action”; “log stuff automatically (calls, emails etc.)”; “keep the pipeline updated without you touching it”; “action executes immediately… everything logs automatically in background… pipeline updates itself”; “if you ask ‘why this?’ → short explanation, not a report”

Contradictions: No contradictory content found.

## Decision-Making Rules
Trade-offs should be resolved by preferring removal/avoidance of screens, ensuring features lead directly to immediate action, reducing required user input, and excluding anything that doesn’t produce an actionable next step. There are also “drift” checks: if the product starts accumulating tabs/dashboards or looking like a traditional CRM, it’s a sign of losing direction.

**Confidence:** High  
**Evidence:** “decision rules (gut checks) ● can we remove a screen instead of adding one ● does this help someone take action immediately ● can we reduce input here ● if it doesn’t lead to action → probably shouldn’t exist”; “if we start adding tabs + dashboards we’re probably drifting”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”

Contradictions: No contradictory content found.

## Product Character
The product should feel focused, direct, calm, and somewhat decisive—“almost telling you what to do.” Emotionally, it should reduce stress/guilt and make users feel in control, not overwhelmed, by making the next step clear and removing admin burden.

**Confidence:** High  
**Evidence:** “product should feel like ● focused ● direct ● calm ● a bit decisive (almost telling you what to do)”; “ideal state = calm, clear, just doing the next thing”; “users… want: to feel in control… not feel overwhelmed… not feel like they’re doing admin work”

Contradictions: No contradictory content found.

## Language and Tone
Language should be short and direct, avoiding hype, buzzwords, and congratulatory/gamified language. Outputs should be phrased as concrete actions rather than analytical statements about metrics or “pipeline health.”

**Confidence:** High  
**Evidence:** “tone / language… short, direct ● no hype / no ‘you’re crushing it’ type stuff ● no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’”

Contradictions: No contradictory content found.

## Evolution Constraints
The product should avoid evolving toward traditional CRM patterns (screens, tabs, dashboards, reporting). There is an explicit constraint that if users require training, the product has failed, implying the UX should remain self-explanatory and low-onboarding over time. There is also a directional constraint toward becoming “invisible over time.”

**Confidence:** Medium  
**Evidence:** “if we start adding tabs + dashboards we’re probably drifting”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “If someone needs training, we probably failed.”; “Feels like CRM should become kind of invisible over time”

Contradictions: No contradictory content found.

## Integrity Checks
Integrity is evaluated via “failure/drift” signals: if users have to fill fields/type into fields, something went wrong/they failed; if training is needed, they failed; if it starts looking like a traditional CRM (tabs/dashboards), they’ve “lost the plot.” Additional checks include whether each feature leads to immediate action and whether it reduces screens/input.

**Confidence:** High  
**Evidence:** “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed”; “If someone needs training, we probably failed.”; “if we start adding tabs + dashboards we’re probably drifting”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “if it doesn’t lead to action → probably shouldn’t exist”

Contradictions: No contradictory content found.

---

### Completeness
Complete → all core elements clearly present.

### Strength
High → principles, boundaries, behavioral rules, and decision rules are clear and enforceable, with multiple explicit “drift/failure” checks.

---

### Suggestion
Add explicit rules for edge cases and safety/quality, e.g., what the system should do when it’s uncertain about the “next best action,” how to handle incorrect auto-logging/pipeline updates (user correction flows), and any required privacy/security constraints for capturing emails/calls.