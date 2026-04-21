#### Core Principles
- Conversation first, always; actions > insights; automation by default  
- `Confidence: High`  
- `Evidence:` “conversation first, always”; “actions > insights”; “automation by default”  
- `Contradictions:` No contradictory content found.

#### Product Boundaries
- Not a reporting/BI/analytics/dashboard tool; not a place to input data; not endlessly customizable; not another Salesforce; avoid traditional screens/tabs/dashboards  
- `Confidence: High`  
- `Evidence:` “not a reporting tool”; “not BI”; “not a place to input data”; “not something you customize endlessly”; “basically not another version of Salesforce”; “We’re intentionally not doing: traditional screens; analytics dashboards (at least not upfront); manual pipeline management”; “if we start adding tabs + dashboards we’re probably drifting”  
- `Contradictions:` No contradictory content found.

#### Behavioral Rules
- System tells/suggests next best actions (ideally before you ask) and prioritizes them; user shouldn’t browse—should react; execute actions quickly; everything logs and updates in the background/invisible; reduce choices; avoid/manual data entry is a failure condition; provide short “why” explanations (not reports)  
- `Confidence: High`  
- `Evidence:` “system suggests actions before you ask (ideally)”; “tell you your next best action”; “ideally ranked / prioritized so no thinking required”; “user doesn’t browse anything, just reacts”; “action executes immediately”; “everything logs automatically in background”; “pipeline updates itself”; “everything updates in background, invisible”; “reduce choices, don’t give users 10 options”; “if user has to fill fields → something went wrong”; “If someone needs training, we probably failed”; “if you ask ‘why this?’ → short explanation, not a report”  
- `Contradictions:` No contradictory content found.

#### Decision-Making Rules
- Prefer removing screens over adding; only ship things that lead to immediate action; reduce required user input; if it doesn’t lead to action, it likely shouldn’t exist; “if it starts looking like a traditional CRM again” that’s a failure/drift signal  
- `Confidence: High`  
- `Evidence:` “can we remove a screen instead of adding one”; “does this help someone take action immediately”; “can we reduce input here”; “if it doesn’t lead to action → probably shouldn’t exist”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “if we start adding tabs + dashboards we’re probably drifting”  
- `Contradictions:` No contradictory content found.

#### Product Character
- Should feel focused, direct, calm, and a bit decisive (almost telling you what to do); aim for “calm, clear”; should not feel analytical, busy/cluttered, gamified, overly configurable; reduce stress/guilt and overwhelm; help users feel in control  
- `Confidence: High`  
- `Evidence:` “product should feel like: focused; direct; calm; a bit decisive”; “ideal state = calm, clear, just doing the next thing”; “users… want: to feel in control… not feel overwhelmed”; “should NOT feel like: analytical tool; busy / cluttered; gamified; overly configurable”  
- `Contradictions:` No contradictory content found.

#### Language and Tone
- Short, direct, no hype/praise (“you’re crushing it”), no buzzwords; phrasing should be action-oriented (“call these 3 deals”) rather than metric/report language  
- `Confidence: High`  
- `Evidence:` “tone / language… short, direct”; “no hype / no ‘you’re crushing it’ type stuff”; “no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’”  
- `Contradictions:` No contradictory content found.

#### Evolution Constraints
- Avoid drifting into traditional CRM patterns (tabs, dashboards, screens); analytics dashboards explicitly “not upfront” (implies sequencing constraint); “CRM should become kind of invisible over time” as a directional constraint  
- `Confidence: Medium`  
- `Evidence:` “if we start adding tabs + dashboards we’re probably drifting”; “We’re intentionally not doing… analytics dashboards (at least not upfront)”; “Feels like CRM should become kind of invisible over time… that’s the direction.”  
- `Contradictions:` No contradictory content found.

#### Integrity Checks
- Drift/fitness checks: if users must fill fields/type into fields, something went wrong / “we probably failed”; if it starts looking like a traditional CRM again, “lost the plot”; if a feature doesn’t lead to action, it shouldn’t exist; if someone needs training, “we probably failed”  
- `Confidence: High`  
- `Evidence:` “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed”; “if it doesn’t lead to action → probably shouldn’t exist”; “If someone needs training, we probably failed.”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”  
- `Contradictions:` No contradictory content found.

---

## Completeness
- **Complete**  
  - Principles, boundaries, behavioral rules, and decision-making rules are all clearly present.

## Strength
- **High**  
  - Rules are specific and enforceable (e.g., action-orientation, remove screens, automation-by-default, “no fields,” no dashboards), with multiple “failure/drift” integrity checks.

---

## Suggestion
- Add explicit trade-off resolution for edge cases (e.g., what to do when automation confidence is low, conflicting signals, or missing context): a rule for when to ask the user vs. act automatically.  
- Add explicit boundaries around accuracy/privacy/compliance expectations for automatic logging and background updates (what must never be captured, and how to handle sensitive data).  
- Add a simple checklist rubric (1–2 lines) to score new features against: conversation-first, action-immediate, input-minimizing, screen-reducing, calm/direct tone.