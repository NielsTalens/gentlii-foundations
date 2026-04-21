#### Core Principles
- Conversation first, always; actions > insights; automation by default; reduce searching/updating/deciding in favor of clear next actions and execution.
- Confidence: High
- Evidence: “conversation first, always”; “actions > insights”; “automation by default”; “everything points to: → remove searching → remove updating → remove deciding and replace it with: → clear next action → immediate execution → no admin overhead”
- Contradictions: No contradictory content found.

#### Product Boundaries
- Not a reporting/BI/analytics/dashboard-first tool; not a place to input data; not endlessly customizable; not another Salesforce-like traditional CRM with tabs/screens/manual pipeline management.
- Confidence: High
- Evidence: “what we are not… not a reporting tool ● not BI ● not a place to input data ● not something you customize endlessly basically not another version of Salesforce”; “We’re intentionally not doing: traditional screens; analytics dashboards (at least not upfront); manual pipeline management”
- Contradictions: No contradictory content found.

#### Behavioral Rules
- Provide “next best action” (ideally proactively before being asked), prioritized/ranked; keep everything updated invisibly in the background; execute actions quickly from conversation; auto-capture/log emails/calls; generate/suggest notes; minimize choices; avoid requiring field entry; onboarding should be near-zero.
- Confidence: High
- Evidence: “system suggests actions before you ask (ideally)”; “everything updates in background, invisible”; “reduce choices, don’t give users 10 options”; “tell you your next best action”; “log stuff automatically (calls, emails etc.)”; “keep the pipeline updated without you touching it”; “action executes immediately everything logs automatically in background pipeline updates itself”; “notes generated or at least suggested”; “if user has to fill fields → something went wrong”; “If someone needs training, we probably failed.”
- Contradictions: No contradictory content found.

#### Decision-Making Rules
- Prefer removing screens over adding; ship features only if they enable immediate action; reduce required input; if it doesn’t lead to action, it shouldn’t exist; adding tabs/dashboards indicates drift toward traditional CRM.
- Confidence: High
- Evidence: “decision rules (gut checks) ● can we remove a screen instead of adding one ● does this help someone take action immediately ● can we reduce input here ● if it doesn’t lead to action → probably shouldn’t exist”; “if we start adding tabs + dashboards we’re probably drifting”
- Contradictions: No contradictory content found.

#### Product Character
- Should feel focused, direct, calm, and a bit decisive; should make users feel in control, not overwhelmed; should not feel analytical, busy/cluttered, gamified, or overly configurable.
- Confidence: High
- Evidence: “product should feel like ● focused ● direct ● calm ● a bit decisive”; “ideal state = calm, clear, just doing the next thing”; “should NOT feel like: ● analytical tool ● busy / cluttered ● gamified ● overly configurable”
- Contradictions: No contradictory content found.

#### Language and Tone
- Short and direct; no hype/cheerleading; no buzzwords; use action-oriented phrasing (e.g., “call these 3 deals”).
- Confidence: High
- Evidence: “tone / language… ● short, direct ● no hype / no ‘you’re crushing it’ type stuff ● no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’”
- Contradictions: No contradictory content found.

#### Evolution Constraints
- Avoid drifting into traditional CRM patterns; if it starts looking like traditional CRM again (tabs/dashboards/screens), that’s a failure signal; dashboards/analytics “not upfront”; “maybe voice later” suggests staged modality expansion while keeping conversation-first.
- Confidence: Medium
- Evidence: “if we start adding tabs + dashboards we’re probably drifting”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “analytics dashboards (at least not upfront)”; “Probably chat based, maybe voice later.”
- Contradictions: No contradictory content found.

#### Integrity Checks
- If the user must fill fields / type into fields, something went wrong / “we failed”; if it doesn’t lead to action it shouldn’t exist; if users need training/onboarding, the product failed; drifting into tabs/dashboards/traditional CRM indicates loss of direction.
- Confidence: High
- Evidence: “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed”; “If someone needs training, we probably failed.”; “if it doesn’t lead to action → probably shouldn’t exist”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”
- Contradictions: No contradictory content found.

---

## Completeness
- **Complete**
  - Confidence: High
  - Evidence: Principles (“conversation first…”, “actions > insights”, “automation by default”), clear boundaries (“not a reporting tool… not BI…”), behavioral rules (“suggest actions… background updates… reduce choices…”), decision rules (“gut checks…”).
  - Contradictions: No contradictory content found.

## Strength
- **High**
  - Confidence: High
  - Evidence: Enforceable “gut checks” for trade-offs; explicit “what we are not”; concrete failure conditions (“if user has to fill fields… we failed”, “If someone needs training, we probably failed”); clear tone and feel constraints.
  - Contradictions: No contradictory content found.

---

### Suggestion
- Add explicit **edge-case integrity rules** (e.g., what to do when automation is uncertain: ask a single clarifying question vs. making an assumption; how to handle incorrect auto-logging or wrong pipeline updates).
- Add a **privacy/security integrity principle** (especially since it auto-captures emails/calls) describing what must never happen and what user controls exist.
- Define a **decision rule for “voice later”** to avoid adding modality complexity that reintroduces screens/options (e.g., voice must map to the same action primitives as chat).