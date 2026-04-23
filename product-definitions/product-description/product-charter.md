## Core Principles

The product is explicitly “conversation first,” prioritizing chat/language as the primary interface and avoiding traditional screens where possible. It prioritizes actions over insights (telling users what to do next rather than showing charts), and defaults to automation (capturing and updating information without asking users to manually enter data). It also emphasizes reducing user choices and cognitive load.

**Confidence:** High

**Evidence:** “conversation first, always”; “actions > insights”; “automation by default”; “reduce choices, don’t give users 10 options”; “remove searching → remove updating → remove deciding and replace it with → clear next action → immediate execution → no admin overhead”

**Contradictions:** No contradictory content found.

## Product Boundaries

The product is explicitly not a reporting/BI/analytics dashboard tool, not a place for manual data input, and not an endlessly customizable Salesforce-like system. It also explicitly avoids traditional CRM paradigms such as tabs, dashboards, and manual pipeline management—at least initially.

**Confidence:** High

**Evidence:** “what we are not… not a reporting tool… not BI… not a place to input data… not something you customize endlessly… basically not another version of Salesforce”; “We’re intentionally not doing: traditional screens; analytics dashboards (at least not upfront); manual pipeline management”

**Contradictions:** No contradictory content found.

## Behavioral Rules

The system should proactively suggest actions (ideally before the user asks), present prioritized “next best actions,” and keep context attached to each recommended action (who + context + suggested message/next step). It should enable fast execution (“send this/call now/schedule”) and automatically log actions and update the pipeline invisibly in the background. If users must fill fields or do “after work,” that is treated as failure. If the user asks “why this?”, the system should provide a short explanation rather than a report.

**Confidence:** High

**Evidence:** “system suggests actions before you ask (ideally)”; “tell you your next best action”; “get list of actions already prioritized”; “each item includes: who; context; suggested message or next step”; “action executes immediately”; “everything logs automatically in background”; “pipeline updates itself”; “everything updates in background, invisible”; “if user has to fill fields → something went wrong”; “If someone needs training, we probably failed.”; “if you ask ‘why this?’ → short explanation, not a report”

**Contradictions:** No contradictory content found.

## Decision-Making Rules

Trade-offs should be resolved using “gut checks” that prefer removing screens over adding them, ensure features directly enable immediate action, reduce required user input, and exclude anything that doesn’t lead to action. Adding tabs/dashboards is treated as drift back toward traditional CRM and a sign the product is “losing the plot.”

**Confidence:** High

**Evidence:** “decision rules (gut checks): can we remove a screen instead of adding one; does this help someone take action immediately; can we reduce input here; if it doesn’t lead to action → probably shouldn’t exist”; “if we start adding tabs + dashboards we’re probably drifting”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”

**Contradictions:** No contradictory content found.

## Product Character

The product should feel focused, direct, calm, and somewhat decisive—almost like it’s telling the user what to do. Emotionally, it should help users feel in control and not overwhelmed, replacing “stress + guilt” with a “calm, clear” experience centered on doing the next thing.

**Confidence:** High

**Evidence:** “product should feel like: focused; direct; calm; a bit decisive (almost telling you what to do)”; “ideal state = calm, clear, just doing the next thing”; “users… want: to feel in control… not feel overwhelmed… not feel like they’re doing admin work”

**Contradictions:** No contradictory content found.

## Language and Tone

Communication should be short and direct, without hype, praise-y encouragement, or buzzwords. Outputs should be phrased as concrete actions (“call these 3 deals”) rather than abstract status/metrics language (“pipeline health improved”).

**Confidence:** High

**Evidence:** “tone / language… short, direct”; “no hype / no ‘you’re crushing it’ type stuff”; “no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’”

**Contradictions:** No contradictory content found.

## Evolution Constraints

The product should avoid evolving into a traditional CRM with screens, tabs, dashboards, and reporting; if it begins to resemble that, it signals drift/failure. “Analytics dashboards” are explicitly deferred “at least not upfront,” implying a constraint on early evolution. There is also a directional constraint toward becoming “invisible over time.”

**Confidence:** Medium

**Evidence:** “if we start adding tabs + dashboards we’re probably drifting”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “analytics dashboards (at least not upfront)”; “Feels like CRM should become kind of invisible over time”

**Contradictions:** No contradictory content found.

## Integrity Checks

The document includes several explicit “failure/drift” checks: if users need training, the product likely failed; if users have to fill fields/type into fields, something went wrong/we failed; and if the product starts looking like a traditional CRM (tabs/dashboards), it has drifted/lost the plot. Decision “gut checks” also function as evaluation criteria (exclude features that don’t lead to action).

**Confidence:** High

**Evidence:** “If someone needs training, we probably failed.”; “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “if it doesn’t lead to action → probably shouldn’t exist”

**Contradictions:** No contradictory content found.

### Completeness

Complete → all core elements clearly present

### Strength

High → clear, enforceable, actionable

## Suggestion

Add a small set of explicit edge-case integrity rules for when automation is uncertain or risky (e.g., confidence thresholds for auto-updating deal stages, when to ask the user for confirmation, and how to correct mistakes), plus a lightweight “exception policy” for the few moments the product is allowed to show structured UI (if ever) so the “no screens” principle remains enforceable as features expand.