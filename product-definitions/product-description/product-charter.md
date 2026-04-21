#### Core Principles
- Conversation-first (always); actions > insights; automation by default; reduce choices; remove searching/updating/deciding and replace with clear next action + immediate execution + no admin overhead  
- `Confidence: High`  
- `Evidence:`  
  - “conversation first, always… everything through chat / language, no screens if we can avoid it”  
  - “actions > insights… avoid anything that looks like reporting”  
  - “automation by default… system should just capture stuff… if user has to fill fields → something went wrong”  
  - “reduce choices, don’t give users 10 options”  
  - “remove searching → remove updating → remove deciding”  
- `Contradictions: No contradictory content found.`

#### Product Boundaries
- Not a reporting/BI tool; not dashboards-first; not a place to input data; not endlessly configurable; not “another version of Salesforce”; avoid traditional screens/tabs/dashboards and manual pipeline management  
- `Confidence: High`  
- `Evidence:`  
  - “what we are not… not a reporting tool… not BI… not a place to input data… not something you customize endlessly… basically not another version of Salesforce”  
  - “We’re intentionally not doing: traditional screens… analytics dashboards (at least not upfront)… manual pipeline management”  
  - “if we start adding tabs + dashboards we’re probably drifting”  
- `Contradictions: No contradictory content found.`

#### Behavioral Rules
- Suggest next actions (ideally before being asked); answer “what should I do now?” with prioritized actions; provide short “why this?” explanations (not reports); keep updates/logging invisible in the background; enable quick execution (“send/call/schedule”) with minimal steps; tie flags/insights to executable actions; avoid forcing field entry  
- `Confidence: High`  
- `Evidence:`  
  - “system suggests actions before you ask (ideally)”  
  - “ability to just ask ‘what should I do now?’” / “it gives you a straight answer”  
  - “ideally ranked / prioritized so no thinking required”  
  - “if you ask ‘why this?’ → short explanation, not a report”  
  - “everything updates in background, invisible”  
  - “action executes immediately… everything logs automatically in background… pipeline updates itself”  
  - “converts that into actions, not insights… always tied to something executable”  
  - “if user has to type things in fields, we probably failed”  
- `Contradictions: No contradictory content found.`

#### Decision-Making Rules
- Prefer removing screens over adding; ship only what leads directly to immediate action; reduce user input; avoid anything that looks like reporting; if feature doesn’t lead to action, it shouldn’t exist; “if it starts looking like a traditional CRM again… lost the plot” (drift check)  
- `Confidence: High`  
- `Evidence:`  
  - “decision rules (gut checks): can we remove a screen instead of adding one”  
  - “does this help someone take action immediately”  
  - “can we reduce input here”  
  - “if it doesn’t lead to action → probably shouldn’t exist”  
  - “avoid anything that looks like reporting”  
  - “if it starts looking like a traditional CRM again, we’ve probably lost the plot”  
- `Contradictions: No contradictory content found.`

#### Product Character
- Should feel focused, direct, calm, and a bit decisive (almost telling you what to do); should create “calm, clear” and “in control,” not overwhelmed; should not feel analytical, busy/cluttered, gamified, or overly configurable  
- `Confidence: High`  
- `Evidence:`  
  - “product should feel like: focused… direct… calm… a bit decisive”  
  - “ideal state = calm, clear, just doing the next thing”  
  - “users… want: to feel in control… not feel overwhelmed”  
  - “should NOT feel like: analytical tool… busy / cluttered… gamified… overly configurable”  
- `Contradictions: No contradictory content found.`

#### Language and Tone
- Short, direct, no hype/praise language, no buzzwords; use action-oriented commands (“call these 3 deals”) rather than status/analytics phrasing  
- `Confidence: High`  
- `Evidence:`  
  - “tone / language… short, direct”  
  - “no hype / no ‘you’re crushing it’ type stuff”  
  - “no buzzwords”  
  - “more like: ‘call these 3 deals’ not: ‘pipeline health improved’”  
- `Contradictions: No contradictory content found.`

#### Evolution Constraints
- Avoid drifting into traditional CRM patterns (tabs/screens/dashboards); dashboards/analytics explicitly deferred “at least not upfront”; intent for CRM to become “invisible over time” (directional constraint)  
- `Confidence: Medium`  
- `Evidence:`  
  - “if we start adding tabs + dashboards we’re probably drifting”  
  - “analytics dashboards (at least not upfront)”  
  - “Feels like CRM should become kind of invisible over time… that’s the direction”  
  - “if it starts looking like a traditional CRM again, we’ve probably lost the plot”  
- `Contradictions: No contradictory content found.`

#### Integrity Checks
- Failure conditions / red flags: if user must fill fields; if training is needed; if product starts looking like traditional CRM (tabs/dashboards); if something doesn’t lead to action; if “why” becomes a report  
- `Confidence: High`  
- `Evidence:`  
  - “if user has to fill fields → something went wrong” / “if user has to type things in fields, we probably failed”  
  - “If someone needs training, we probably failed.”  
  - “if we start adding tabs + dashboards we’re probably drifting”  
  - “if it doesn’t lead to action → probably shouldn’t exist”  
  - “if you ask ‘why this?’ → short explanation, not a report”  
- `Contradictions: No contradictory content found.`

---

## Completeness
- **Complete**  
  - `Confidence: High`  
  - `Evidence:` Principles, boundaries, behavioral rules, and decision rules are all explicitly listed (notably in “early product principles,” “what we are not,” “how it should behave,” and “decision rules (gut checks)”).  
  - `Contradictions: No contradictory content found.`

## Strength
- **High**  
  - `Confidence: High`  
  - `Evidence:` Multiple enforceable “gut checks” and clear failure modes (“if user has to fill fields…,” “If someone needs training…,” drift triggers like “tabs + dashboards”).  
  - `Contradictions: No contradictory content found.`

---

## Suggestion
- Add explicit guidance for edge cases where the “no screens / no dashboards” rule might be challenged (e.g., compliance/audit needs, admin setup, data correction), including an approved minimal pattern that still fits “short explanation, not a report.”  
- Define a small set of measurable integrity metrics (e.g., % actions auto-logged, median time-to-next-action shown, % flows completed without manual data entry) to operationalize “if we failed” checks.