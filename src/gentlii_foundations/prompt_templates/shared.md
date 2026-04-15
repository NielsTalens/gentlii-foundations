---
name: shared-extraction-prompt
description: there are some important prompt elements that are applicable for all the extractors
---

Return clean markdown only.
Do not invent missing information.
Do not infer beyond what is reasonably supported by the text.
Only extract information that is backed by explicit or strongly implied evidence.
If information is missing, mark it as "Not found".

### Confidence score
If information is weak or ambiguous, reflect that in the confidence level.
For every subject or section in the Output Structure, include a confidence line immediately below the extracted content and before the supporting evidence.

Use this confidence scale:
- High: clear, explicit, consistent evidence
- Medium: partial or indirect evidence
- Low: weak, ambiguous, or minimal evidence

### Evidence
For every subject or section in the Output Structure, include the related evidence immediately below the extracted content.
If evidence is missing, omit the unsupported claim.
For each extracted section, provide supporting evidence using exact quotes or close paraphrases where possible.
If no evidence is found for a section, omit it or mark it as "No supporting evidence found".

### Suggestions
You MAY provide suggestions, but they must be clearly marked as "Suggestion" and must not be mixed with extracted content.
Provide concrete suggestions to improve the artifact.

- Must be clearly labeled as "Suggestion"
- Must not introduce fabricated facts
- Should focus on missing or weak elements

### Contradictory content
Identify contradictions, inconsistencies, and tensions in the provided content.
Check within the same document.
For every subject or section in the Output Structure, if there are contradictions, include the related evidence immediately below the extracted content.
- Only include contradictions that are explicit or strongly implied by the text
- Do not infer intent or fill gaps
- Do not fabricate conflicts
- If no clear contradiction is found, return: “No contradictory content found.”

Guidance
Pay special attention to:
- Principles vs actual examples or ideas
- Stated constraints vs proposed solutions
- Metrics vs expected behavior
- “Always / never” statements vs exceptions
- Speed vs compliance, automation vs control, simplicity vs completeness
