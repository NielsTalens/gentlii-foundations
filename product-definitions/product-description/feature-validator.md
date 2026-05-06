# Feature Request: Email forwarding to create/update contact info
### Decision
Revise
### Alignment score
4/5
### Confidence
High

## Strategic alignment
### Confidence
High

**Evidence:** Strategy emphasizes “Automation by default” and removing “dashboards/navigation and manual updating,” aiming for “automatic capture/logging.” The feature enables input via an existing daily tool (email) “instead of having to go to the CRM system (and possibly login).”

### Contradictions
No contradictory content found.

## Business Case alignment
### Confidence
Medium

**Evidence:** Business case targets “daily usage/adoption,” “minimizes training/onboarding,” and reducing “manual/admin overhead.” Email forwarding reduces friction and avoids “after work” CRM updates by capturing contact info without logging into CRM.

### Contradictions
No contradictory content found.

## Product Vision fit
### Confidence
High

**Evidence:** Vision includes “automatic activity capture/logging (emails, calls)” and “automation by default: zero/near-zero data entry.” Extracting “contact info from mail senders” is consistent with automatic capture from email.

### Contradictions
No contradictory content found.

## Product Charter compliance
### Confidence
Medium

**Evidence:** Charter says “conversation-first interface as the default/primary mode” and “One interface (chat).” Email forwarding introduces an additional interaction surface outside chat, even if it reduces friction. Charter also says “system should capture and update data without asking the user to do manual entry,” which this supports (forwarding is a lightweight action, not field-filling).

### Contradictions
No contradictory content found.

## Risks introduced
### Confidence
High

**Evidence:** Not explicitly covered in artifacts; risks inferred from the request’s mechanism and charter boundaries.
- Creates a second “interface” pattern (email ingestion) that may dilute “one interface (chat)” and lead to sprawl (“use the tools they already use” could expand beyond email).
- Potential for increased user choice/ambiguity (“forward an email that contains specific info”)—users must remember formatting/what to forward, which can increase cognitive load.
- Could become a manual workaround rather than “invisible” automation if forwarding is required frequently.

### Contradictions
No contradictory content found.

## Missing justification
### Confidence
High

**Evidence:** The request lacks details needed to confirm it reduces cognitive load and stays within boundaries:
- Not found: how this remains conversation-first (e.g., confirmation/next action delivered via chat).
- Not found: how the system ensures “minimal thinking required” (format rules, parsing reliability).
- Not found: how it leads to “immediate user action/execution” beyond data capture (charter making rule).
- Not found: explicit scope limits (it says “existing tools,” but only first version email contact info—needs boundary to prevent drift).

### Contradictions
No contradictory content found.

## Minimal change to make this valid
### Confidence
High

**Evidence:** Based on charter decision rules and vision features (conversation-first, actions, automation).
- Reframe as **automation-first email capture** (auto-detect new contacts from connected inbox) with **email forwarding only as a fallback**, not the primary workflow.  
  **Evidence:** “Automation by default… system should just capture stuff, not ask”; “CRM becomes ‘invisible’… stays out of the way.”
- Ensure the user experience remains **chat-centered**: after ingestion, surface a concise chat message with a single recommended next action (e.g., “Add contact + schedule follow-up?”).  
  **Evidence:** “One interface (chat) / One output (next action)”; “execute actions quickly via chat commands.”
- Add explicit scope guardrails: “Only contact creation/enrichment from sender metadata in v1; no custom parsing/templates; no multi-tool ingestion yet.”  
  **Evidence:** “Scope discipline: ‘Not trying to boil the ocean here’”; “reduce choices.”

### Contradictions
No contradictory content found.