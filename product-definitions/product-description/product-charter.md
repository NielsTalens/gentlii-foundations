## Core Principles

Het product stuurt op extreme eenvoud en automatisering: liever automatiseren dan documenteren, liever schrappen dan toevoegen, en liever prefill dan dat de gebruiker veel moet invullen. Daarnaast is “minder stappen” een leidend principe, met de kanttekening dat dit soms botst met de behoefte aan uitleg/zekerheid en met compliance.

**Confidence:** High

**Evidence:** “Automatiseren > documenteren”, “Schrappen > toevoegen”, “Prefill > input”, “Minder stappen > meer uitleg (maar conflicteert soms)”, en “We willen iets bouwen rondom verzekeringen maar dan extreem simpel.”

**Contradictions:** Er wordt expliciet spanning genoemd tussen principes/ambities: “Minder stappen > meer uitleg (maar conflicteert soms)”, “Te weinig stappen kan ook wantrouwen creëren (‘te makkelijk?’)”, en “Minder stappen > meer uitleg” maar ook “geen uitleg nodig”?


## Product Boundaries

Het product positioneert zich expliciet niet als een complexe zakelijke verzekeraar, zonder offline processen, en zonder maatwerkadvies. Mobile-first wordt als uitgangspunt genoemd; een desktop-first “uitgebreid platform” wordt als conflicterend met de beoogde richting neergezet.

**Confidence:** Medium

**Evidence:** “Wat we NIET zijn… Geen complexe zakelijke verzekeraar / Geen offline processen / Geen maatwerkadvies”; “Mobile-first sowieso, desktop misschien later maar eigenlijk niet nodig.”; “Conflicten: ‘Geen desktop-first product’”.

**Contradictions:** Er is onzekerheid over support en platformrichting: “Misschien wel support nodig → hoe past dat?” en het alternatief “Desktop-first interface met uitgebreide dashboards…” tegenover “Mobile-first sowieso, desktop misschien later maar eigenlijk niet nodig.”


## Behavioral Rules

De gewenste productgedragingen draaien om frictie minimaliseren (korte flows, weinig stappen, prefill), snelle feedback/status, en waar mogelijk geautomatiseerde claimafhandeling (incl. foto/video) en mogelijk instant payout. Compliance en fraudepreventie worden genoemd als randvoorwaarden die uitzonderingen op volledige automation kunnen vereisen.

**Confidence:** Medium

**Evidence:** “Afsluiten verzekering (happy path extreem kort)”, “Claim indienen (foto/video)”, “Status check (altijd zichtbaar?)”, “API-based prefill…”, “Foto/video claims”, “AI schadebeoordeling”, “Instant payout (indien mogelijk)”, “Compliance moet ‘by design’”, “Fraudepreventie vereist waarschijnlijk uitzonderingen op automation”.

**Contradictions:** “Volledig geautomatiseerd” botst met uitzonderingen/edge cases: “ ‘Volledig geautomatiseerd’ vs edge cases” en “ ‘Automation first’ vs menselijke review bij fraude”; ook “ ‘Geen formulieren’ vs data nodig / KYC vereist wel iets…”.


## Decision-Making Rules

Trade-offs worden impliciet gestuurd door de voorkeurshiërarchieën in de principes (automatiseren/schrappen/prefill/minder stappen). Daarnaast wordt compliance “by design” als harde constraint genoemd, en frauderisico als limiter voor “instant payout” en volledige automatisering. Er is ook een expliciete spanning tussen “snel” en “rustig/zeker” die bij UI-keuzes trade-offs afdwingt.

**Confidence:** Medium

**Evidence:** “Automatiseren > documenteren”, “Schrappen > toevoegen”, “Prefill > input”, “Minder stappen > meer uitleg (maar conflicteert soms)”; “Compliance moet ‘by design’”; “ ‘Instant payout’ vs risico”; “ ‘Rustig’ vs ‘snel’ kan botsen in UI”.

**Contradictions:** Beslisregels zijn niet eenduidig door meerdere genoemde spanningen: “ ‘Realtime alles’ vs backend complexiteit”, “ ‘Transparantie’ vs complexiteit van voorwaarden”, en “Minder stappen… maar ook ‘geen uitleg nodig’?”


## Product Character

Het product moet aanvoelen als snel, rustig, zeker en transparant; en expliciet niet bureaucratisch, onduidelijk of te speels.

**Confidence:** High

**Evidence:** “Moet voelen: Snel / Rustig / Zeker / Transparant” en “Mag niet voelen: Bureaucratisch / Onduidelijk / Te speels”.

**Contradictions:** “ ‘Rustig’ vs ‘snel’ kan botsen in UI”.


## Language and Tone

Er is alleen karaktertaal (hoe het moet “voelen”), maar geen concrete richtlijnen voor copy/taalgebruik, vocabulaire, foutmeldingen, of tone-of-voice regels.

**Confidence:** Low

**Evidence:** “Moet voelen… Transparant… Mag niet voelen… Te speels”.

**Contradictions:** No contradictory content found.


## Evolution Constraints

Mobile-first wordt als uitgangspunt genoemd met desktop “misschien later”; daarnaast wordt genoemd dat de mate van automation beperkt kan worden door regelgeving en dat “compliance by design” een structurele constraint is. Er is ook een hint naar mogelijke latere verbreding van doelgroep en een futuristische long-term richting (live data), maar dit is expliciet vaag.

**Confidence:** Medium

**Evidence:** “Mobile-first sowieso, desktop misschien later maar eigenlijk niet nodig.”; “Er zit iets in automation-first, maar tegelijk weten we nog niet hoe ver dat kan (ivm regelgeving).”; “Compliance moet ‘by design’”; “mogelijk ook breder toepasbaar later”; “Maar dat voelt ook nog vaag / futuristisch.”

**Contradictions:** Alternatieve koers “Desktop-first… uitgebreid platform” botst met mobile-first/doelgroep: “Conflicten: ‘Geen desktop-first product’ … Target group (digital natives, mobiel)”.


## Integrity Checks

Er staan ideeën voor meetbare doelen en enkele evaluatiepunten (drop-off per stap meten), plus impliciete checks rondom compliance/KYC/fraudepreventie. Er is geen uitgewerkt evaluatiekader (bijv. release-gates, kwaliteitscriteria, auditability), maar er zijn wel duidelijke risicogebieden die als checks fungeren.

**Confidence:** Medium

**Evidence:** “Metrics (ideeën…): Conversie >60%… <3 min tot polis… 70% claims automatisch… NPS >50… Drop-off per stap meten (belangrijk)”; “Compliance moet ‘by design’”; “KYC nodig”; “Fraudepreventie vereist waarschijnlijk uitzonderingen op automation”.

**Contradictions:** De metrics/ambities worden zelf betwijfeld: “(lijkt hoog?)”, “(ambitieus)”, en “ ‘Binnen minuten verzekerd…’ — maar niet zeker of dit te ambitieus is (zeker met compliance).”


### Completeness

Partial

### Strength

Medium

### Suggestion

Leg expliciete beslisregels vast voor de belangrijkste spanningen die nu al genoemd worden (bijv. “compliance by design wint altijd”, wanneer je extra stappen/‘checks’ toevoegt om vertrouwen te verhogen, wanneer menselijke review verplicht is, en onder welke voorwaarden ‘instant payout’ mag), en vertaal het gewenste gevoel (“snel/rustig/zeker/transparant”) naar concrete gedrags- en copy-richtlijnen (status-communicatie, uitleg-niveau, foutmeldingen, en wanneer/hoe support wordt aangeboden) zodat teams consistent kunnen ontwerpen zonder telkens dezelfde trade-offs opnieuw te bediscussiëren.