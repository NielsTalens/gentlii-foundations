## Core Principles

De bronnen noemen een set “principles” die vooral draaien om maximale simplificatie en automatisering: liever automatiseren dan documenteren, liever schrappen dan toevoegen, liever prefill dan user input, en het aantal stappen minimaliseren (met de kanttekening dat dit soms botst met de behoefte aan uitleg/compliance). Daarnaast wordt “compliance by design” als constraint/principe genoemd.

**Confidence:** High

**Evidence:** “Principles (half charter, half ideeën) Automatiseren > documenteren; Schrappen > toevoegen; Prefill > input; Minder stappen > meer uitleg (maar conflicteert soms)” en “Compliance moet ‘by design’”.

**Contradictions:** Er worden expliciete spanningen genoemd tussen principes: “Minder stappen > meer uitleg (maar conflicteert soms)”, “Minder stappen > meer uitleg” vs “geen uitleg nodig”?; en “Automation-first… weten we nog niet hoe ver dat kan (ivm regelgeving)”.

## Product Boundaries

Er is een expliciete “wat we NIET zijn”-sectie, maar nog “niet scherp”. Genoemde grenzen: geen complexe zakelijke verzekeraar, geen offline processen, geen maatwerkadvies. Er is ook een expliciete afwijzing van een desktop-first richting (“Geen desktop-first product”), plus mobile-first als uitgangspunt.

**Confidence:** Medium

**Evidence:** “Wat we NIET zijn (maar nog niet scherp) Geen complexe zakelijke verzekeraar; Geen offline processen; Geen maatwerkadvies” en “Mobile-first sowieso, desktop misschien later maar eigenlijk niet nodig.” en “Conflicten: ‘Geen desktop-first product’”.

**Contradictions:** De boundary “Geen maatwerkadvies” botst met twijfel over support: “Misschien wel support nodig → hoe past dat?”; bovendien staat een alternatief voorstel haaks op mobile-first: “In plaats van mobile-first, juist een uitgebreid platform bouwen. Desktop-first interface…”.

## Behavioral Rules

Gedragsverwachtingen zijn vooral geformuleerd als gewenste gebruikerservaring: het product moet snel, rustig, zeker en transparant aanvoelen; en mag niet bureaucratisch, onduidelijk of te speels zijn. Verder wordt “status check (altijd zichtbaar?)” genoemd als (nog open) gedrag/feature, en er is een intentie om claims eenvoudig te laten indienen met foto/video en status-updates via push.

**Confidence:** Medium

**Evidence:** “Experience / gevoel: Moet voelen: Snel, Rustig, Zeker, Transparant. Mag niet voelen: Bureaucratisch, Onduidelijk, Te speels” en “Claim indienen (foto/video)”, “Push notificaties bij status updates”, “Status check (altijd zichtbaar?)”.

**Contradictions:** Expliciete UX-spanning: “‘Rustig’ vs ‘snel’ kan botsen in UI”; ook spanning rond “Te weinig stappen kan ook wantrouwen creëren (‘te makkelijk?’)” en “Sommige gebruikers vinden ‘extra checks’ juist geruststellend”.

## Decision-Making Rules

Er zijn impliciete trade-off regels via de “X > Y”-principes (automatiseren boven documenteren, schrappen boven toevoegen, prefill boven input). Daarnaast worden meerdere trade-offs/open vragen expliciet gemaakt (instant payout vs risico/fraude, geen formulieren vs KYC/compliance, realtime/transparantie vs backend/voorwaardencomplexiteit, volledige automation vs edge cases/human review). Er is echter geen eenduidige beslisregel die deze conflicten oplost; ze worden vooral als “wringen/twijfels” benoemd.

**Confidence:** Medium

**Evidence:** “Automatiseren > documenteren… Schrappen > toevoegen… Prefill > input” en “Twijfels / inconsistenties: ‘Instant payout’ vs risico; ‘Geen formulieren’ vs data nodig; ‘Volledig geautomatiseerd’ vs edge cases; ‘Transparantie’ vs complexiteit van voorwaarden” en “Dingen die wringen: ‘Geen formulieren’ vs wettelijke verplichtingen; ‘Automation first’ vs menselijke review bij fraude”.

**Contradictions:** De principes sturen richting maximale reductie/automation, terwijl constraints uitzonderingen vereisen: “Fraudepreventie vereist waarschijnlijk uitzonderingen op automation” en “Automation first” vs “menselijke review bij fraude”.

## Product Character

De gewenste “character/feel” is expliciet: snel, rustig, zeker, transparant; en expliciet niet bureaucratisch, onduidelijk, te speels. De doelgroep (digital natives/jong 18–35) en “extreem simpel” versterken dit karakter, maar blijven deels tentatief (“18–35?”).

**Confidence:** High

**Evidence:** “Moet voelen: Snel, Rustig, Zeker, Transparant. Mag niet voelen: Bureaucratisch, Onduidelijk, Te speels” en “extreem simpel… Vooral voor jongere mensen (18–35?)”.

**Contradictions:** “Rustig” vs “snel” wordt als mogelijke botsing genoemd: “‘Rustig’ vs ‘snel’ kan botsen in UI”.

## Language and Tone

Er is geen expliciete schrijf-, microcopy-, of tone-of-voice guidance (woordkeuze, stijlregels, do/don’t copy). Alleen high-level “gevoel”-woorden (rustig/zeker/transparant) die indirect iets over tone suggereren.

**Confidence:** Low

**Evidence:** No supporting evidence found

**Contradictions:** No contradictory content found.

## Evolution Constraints

Er zijn meerdere constraints/guardrails voor evolutie genoemd: compliance “by design”, KYC is nodig, fraudepreventie kan uitzonderingen op automation vereisen. Ook wordt de platformrichting betwist (mobile-first nu; desktop mogelijk later; alternatief voorstel voor desktop-first uitgebreid platform). Long-term ideeën (realtime verzekeringen op live data) worden als vaag/futuristisch benoemd.

**Confidence:** Medium

**Evidence:** “Compliance moet ‘by design’”, “KYC nodig (maar hoe zichtbaar?)”, “Fraudepreventie vereist waarschijnlijk uitzonderingen op automation” en “Mobile-first sowieso, desktop misschien later maar eigenlijk niet nodig.” en “Richting (long-term-ish)… realtime verzekeringen op basis van live data… vaag / futuristisch.”

**Contradictions:** Mobile-first uitgangspunt vs desktop-first voorstel: “In plaats van mobile-first… Desktop-first interface…” tegenover “Mobile-first sowieso, desktop misschien later…”.

## Integrity Checks

Er zijn geen expliciete “integrity checks” of evaluatieregels voor consistentie/kwaliteit, behalve losse metric-ideeën en meetpunten (drop-off per stap meten) en ambities (NPS, conversie, % claims automatisch). Deze zijn niet als harde checks geformuleerd en worden als “niet gevalideerd/ambitieus” betwijfeld.

**Confidence:** Low

**Evidence:** “Metrics (ideeën, niet gevalideerd)… Drop-off per stap meten (belangrijk)” en “Conversie >60% (lijkt hoog?)… NPS >50 (ambitieus)”.

**Contradictions:** Metrics/targets worden zelf in twijfel getrokken: “(lijkt hoog?)”, “(ambitieus)”, en “niet gevalideerd”.

### Completeness

Partial

### Strength

Medium

### Suggestion

Leg expliciete beslisregels vast voor de grootste trade-offs die al genoemd worden (bijv. “compliance en frauderisico overrulen ‘minder stappen’ wanneer X”, “wanneer schakelen we van automation naar human review”, en “wat betekent ‘transparant’ minimaal in UI: dekking/voorwaarden/status”), en maak de boundaries concreter (wat is “support” wel/niet; mobile-first als harde constraint of gefaseerde roadmap). Voeg daarnaast toonrichtlijnen toe die “rustig/zeker/transparant” vertalen naar copy-do’s/don’ts, en definieer een klein setje integrity checks (bv. elke flow moet: KYC-compliant zijn, <N schermen, status altijd vindbaar, en een expliciete ‘wat is wel/niet gedekt’ samenvatting bevatten).