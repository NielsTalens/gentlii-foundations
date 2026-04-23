## Core Principles

The product is explicitly “conversation first,” prioritizes actions over insights, and uses automation by default so the system captures and updates information without asking the user to do data entry. It aims to reduce fragmentation and cognitive load by removing searching, updating, and deciding, replacing these with clear, prioritized next actions and fast execution.

**Confidence:** High

**Evidence:** “conversation first, always”; “actions > insights”; “automation by default”; “remove searching → remove updating → remove deciding”; “system just tells them immediately… ideally ranked / prioritized so no thinking required”; “if user has to fill fields → something went wrong”

**Contradictions:** No contradictory content found.

## Product Boundaries

The product is explicitly not a traditional CRM experience with screens, tabs, dashboards, reporting/BI, or manual pipeline management, and it should not become endlessly configurable like Salesforce. It is also “not a place to input data,” reinforcing that the user should not be responsible for maintaining fields and records.

**Confidence:** High

**Evidence:** “what we are not… not a reporting tool… not BI… not a place to input data… not something you customize endlessly… basically not another version of Salesforce”; “We’re intentionally not doing: traditional screens; analytics dashboards (at least not upfront); manual pipeline management”

**Contradictions:** No contradictory content found.

## Behavioral Rules

The system should proactively suggest actions (ideally before being asked), provide short explanations when questioned (not reports), keep everything updated invisibly in the background, reduce choices rather than offering many options, and convert signals (risk, staleness) into executable actions. It should enable immediate execution via chat commands (“send this” / “call now” / “schedule”) while automatically logging activity and updating the pipeline with “basically zero data entry.”

**Confidence:** High

**Evidence:** “system suggests actions before you ask (ideally)”; “if you ask ‘why this?’ → short explanation, not a report”; “everything updates in background, invisible”; “reduce choices, don’t give users 10 options”; “action executes immediately… everything logs automatically in background… pipeline updates itself”; “deal stage updated without asking user”; “if user has to type things in fields, we probably failed”

**Contradictions:** No contradictory content found.

## Decision-Making Rules

Feature and design trade-offs should be evaluated using “gut checks” that prioritize removing screens, enabling immediate action, reducing user input, and excluding anything that doesn’t lead to action. Adding tabs/dashboards is treated as a drift signal toward a traditional CRM.

**Confidence:** High

**Evidence:** “decision rules (gut checks) ● can we remove a screen instead of adding one ● does this help someone take action immediately ● can we reduce input here ● if it doesn’t lead to action → probably shouldn’t exist”; “if we start adding tabs + dashboards we’re probably drifting”

**Contradictions:** No contradictory content found.

## Product Character

The product should feel focused, direct, calm, and “a bit decisive” (almost telling you what to do). It should help users feel in control and not overwhelmed, moving them from “stress + guilt” to “calm, clear, just doing the next thing.” It should not feel like an analytical tool, busy/cluttered, gamified, or overly configurable.

**Confidence:** High

**Evidence:** “product should feel like: ● focused ● direct ● calm ● a bit decisive”; “ideal state = calm, clear, just doing the next thing”; “should NOT feel like: ● analytical tool ● busy / cluttered ● gamified ● overly configurable”

**Contradictions:** No contradictory content found.

## Language and Tone

Language should be short and direct, with no hype or congratulatory coaching, and no buzzwords. Prefer action-oriented phrasing that tells the user what to do (e.g., “call these 3 deals”) rather than reporting-style language (e.g., “pipeline health improved”).

**Confidence:** High

**Evidence:** “tone / language… short, direct ● no hype / no ‘you’re crushing it’ type stuff ● no buzzwords”; “more like: ‘call these 3 deals’ not: ‘pipeline health improved’”

**Contradictions:** No contradictory content found.

## Evolution Constraints

Avoid evolving toward a traditional CRM: adding tabs, dashboards, traditional screens, or becoming “another version of Salesforce” is explicitly framed as losing direction. Additionally, onboarding should be minimal; if training is needed, that indicates failure.

**Confidence:** Medium

**Evidence:** “if we start adding tabs + dashboards we’re probably drifting”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”; “If someone needs training, we probably failed.”

**Contradictions:** No contradictory content found.

## Integrity Checks

The document provides explicit “failure signals” and ongoing guardrails: if users have to fill fields/type into fields, something went wrong/“we probably failed”; if the product starts resembling a traditional CRM (tabs/dashboards/screens), “we’ve probably lost the plot.” These operate as integrity checks to keep the product aligned over time.

**Confidence:** High

**Evidence:** “if user has to fill fields → something went wrong”; “if user has to type things in fields, we probably failed”; “if it starts looking like a traditional CRM again, we’ve probably lost the plot”

**Contradictions:** No contradictory content found.

### Completeness

Complete → all core elements clearly present

### Strength

High → clear, enforceable, actionable

## Suggestion

Add a small set of explicit priority and safety policies for “next best action” recommendations (e.g., how to rank urgency vs value, how to handle uncertainty, and when to ask the user a clarifying question), plus a lightweight evaluation checklist for releases (e.g., “does this add a screen?”, “does this reduce user input?”, “does every new element produce an executable action?”) to make the existing gut checks consistently enforceable across the team.