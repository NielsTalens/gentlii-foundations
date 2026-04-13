---
name: shared-extraction-prompt
description: there are some important prompt elements that are applicable for all the extractors
---

Return clean markdown only.
Do not invent missing information.
Do not infer beyond what is reasonably supported by the text.
Only extract information that is backed by explicit or strongly implied evidence.
If information is missing, mark it as "Not found".
If evidence is missing, omit the unsupported claim.
If information is weak or ambiguous, reflect that in the confidence level.
You MAY provide suggestions, but they must be clearly marked as "Suggestion" and must not be mixed with extracted content.
For each extracted section, provide supporting evidence using exact quotes or close paraphrases where possible.
If no evidence is found for a section, omit it or mark it as "No supporting evidence found".

Use this confidence scale:
- High: clear, explicit, consistent evidence
- Medium: partial or indirect evidence
- Low: weak, ambiguous, or minimal evidence

### Suggestions

Provide concrete suggestions to improve the artifact.

- Must be clearly labeled as "Suggestion"
- Must not introduce fabricated facts
- Should focus on missing or weak elements
