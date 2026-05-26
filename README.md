[![CI](https://github.com/NielsTalens/gentlii-foundations/actions/workflows/ci.yml/badge.svg)](https://github.com/NielsTalens/gentlii-foundations/actions/workflows/ci.yml)
[![CodeQL](https://github.com/NielsTalens/gentlii-foundations/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/NielsTalens/gentlii-foundations/actions/workflows/github-code-scanning/codeql)
[![Dependabot Updates](https://github.com/NielsTalens/gentlii-foundations/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/NielsTalens/gentlii-foundations/actions/workflows/dependabot/dependabot-updates)
[![Dependency Graph](https://github.com/NielsTalens/gentlii-foundations/actions/workflows/dependabot/update-graph/badge.svg)](https://github.com/NielsTalens/gentlii-foundations/actions/workflows/dependabot/update-graph)
[![Feature Validation](https://github.com/NielsTalens/gentlii-foundations/actions/workflows/feature-validation.yml/badge.svg)](https://github.com/NielsTalens/gentlii-foundations/actions/workflows/feature-validation.yml)
[![Foundations](https://github.com/NielsTalens/gentlii-foundations/actions/workflows/foundations.yml/badge.svg)](https://github.com/NielsTalens/gentlii-foundations/actions/workflows/foundations.yml)


# Product thinking made easy
Product Thinking takes time. Most teams don’t have it. 
Gentlii structures the groundwork and automates validation, so teams can make better decisions with less effort.

## Gentlii Feature Validation
Ideas are often judged by intuition. This leads to inconsistency. 
Gentlii Feature Validation replaces intuition with structured evaluation.

### Fast and complete validation
Fast decisions often reduce quality. Careful decisions often take too long. 
Gentlii Feature Validator removes that trade-off by checking every feature request against the full product definition. Every idea gets the same structured evaluation: clear reasoning, no guesswork.

## Gentlii Product Guard
Product definitions are not static. Without continuous validation, misalignment goes unnoticed and building the wrong things become a great risk.

### Continuous validation
Gentlii Product Guard continuously validates alignment across all product definition elements. It automatically detects gaps, conflicts, and inconsistencies, ensuring the product remains coherent as it evolves.

## Gentlii Foundations
Strong product decisions require strong foundations. In reality, those foundations are often missing, outdated, or fragmented. Without this, every decision becomes a guess.

Gentlii Foundations creates a structured, living product definition. It organizes your product into a fixed set of core documents. Together, these form a coherent system that defines why the product exists, who it serves and what it should do. When these elements are aligned, every new idea can be evaluated with clarity and consistency. This is where Gentlii Feature Validation takes the stage.

### Just drop in your existing documents
Any type of document. Any type of information. Gentlii structures, connects, and highlights gaps.
No invention. Just clarity and structure.

## Works with your existing tools
Gentlii runs entirely within your existing tools. No separate UI, database, or infrastructure.
There’s nothing new to learn or adopt, and Gentlii operates within your existing security and compliance boundaries. Product definitions are created and live in your version control. Feature validation happens where work already happens: creating an issue automatically triggers validation.

# Gentlii

`gentlii-foundations` is a local Python CLI that turns source documents in a product repository into a structured product-definition package.

It reads source files from `product-definitions/foundations-input`, extracts text, generates artifact markdown with OpenAI, renders a publishable static site in `product-definitions/product-description`, and can run separate validation passes over the generated markdown artifacts.

## Index

- [Module Functionality](#module-functionality)
- [Technical Description](#technical-description)
- [What It Produces](#what-it-produces)
- [Repository Structure](#repository-structure)
- [How It Works](#how-it-works)
- [Architecture](#architecture)
- [Input and Output Contract](#input-and-output-contract)
- [Configuration](#configuration)
- [Running Locally](#running-locally)
- [GitHub Actions](#github-actions)
- [Tests](#tests)

## Module Functionality

The CLI exposes three user-facing modules:

- `foundations`
  The `build` command generates the core product foundation set from source documents in `product-definitions/foundations-input`. It produces the four primary artifacts: `strategy.md`, `business-case.md`, `product-vision.md`, and `product-charter.md`, and then renders them into the combined `index.html` site.
- `guard`
  The `guard` command reviews the generated product-description markdown as a system. It checks whether the core foundation artifacts reinforce each other, identifies contradictions or missing links, and writes the result to `product-guard.md` and `product-guard.html`.
- `feature validation`
  The `feature-validate` command evaluates a single feature request against the generated foundations. It uses the existing product artifacts plus a feature request markdown file to produce an alignment decision, risks, missing justification, and revision guidance in `feature-validator.md` and `feature-validator.html`.

## Technical Description

- `foundations`
  Implemented by `build_foundations(...)` in [src/gentlii_foundations/pipeline.py](src/gentlii_foundations/pipeline.py). The flow resolves `foundations-input` and `product-description`, discovers supported files, extracts their text, loads settings, builds one prompt per target artifact, calls the OpenAI client, writes the markdown artifacts, and renders `index.html` plus `styles.css`.
- `guard`
  Implemented by `run_product_guard(...)` in [src/gentlii_foundations/pipeline.py](src/gentlii_foundations/pipeline.py). It does not read source documents again. Instead, it loads generated markdown from `product-description`, excludes any prior `product-guard.md`, sends the remaining artifacts through the same artifact-generation pipeline with the `product-guard` prompt template, and renders a standalone HTML page for the result.
- `feature validation`
  Implemented by `run_feature_validator(...)` in [src/gentlii_foundations/pipeline.py](src/gentlii_foundations/pipeline.py). It loads the generated markdown artifacts from `product-description`, excludes prior validator outputs, appends the requested feature file as an additional `ExtractedDocument`, generates a single `feature-validator` artifact through the OpenAI client, and renders both markdown and a standalone HTML page.

## What It Produces

The pipeline generates one markdown file per artifact:

- `strategy.md`
- `business-case.md`
- `product-vision.md`
- `product-charter.md`

It also generates a combined static HTML view:

- `index.html`
- `styles.css`

That HTML/CSS output is what the repo publishes through GitHub Pages.

## Repository Structure

```text
.
├── product-definitions/
│   ├── foundations-input/        # Source files added by users
│   ├── feature-requests/         # Feature request markdown files for validation
│   └── product-description/      # Generated markdown + static site
├── src/gentlii_foundations/
│   ├── cli.py
│   ├── pipeline.py
│   ├── discovery.py
│   ├── extraction.py
│   ├── analysis.py
│   ├── prompts.py
│   ├── openai_client.py
│   ├── render.py
│   ├── paths.py
│   ├── config.py
│   └── models.py
├── tests/
├── CONTEXT.md
└── RUNNING_LOCALLY.md
```

## How It Works

The main entrypoint is [src/gentlii_foundations/cli.py](src/gentlii_foundations/cli.py), which exposes:

```bash
gentlii-foundations build <root>
gentlii-foundations guard <root>
gentlii-foundations feature-validate <root> <feature-request-file>
```

In practice the command is run against `product-definitions`.

The pipeline in [src/gentlii_foundations/pipeline.py](src/gentlii_foundations/pipeline.py) is intentionally linear:

1. Resolve paths with [paths.py](src/gentlii_foundations/paths.py)
   `foundations-input` must exist. Output is written to `product-description`.
2. Discover supported input files with [discovery.py](src/gentlii_foundations/discovery.py)
3. Extract document text with [extraction.py](src/gentlii_foundations/extraction.py)
4. Load configuration from environment and `.env` with [config.py](src/gentlii_foundations/config.py)
5. Build artifact prompts with [prompts.py](src/gentlii_foundations/prompts.py)
6. Call the OpenAI Responses API via [openai_client.py](src/gentlii_foundations/openai_client.py)
7. Generate one markdown artifact per target area with [analysis.py](src/gentlii_foundations/analysis.py)
8. Write markdown plus combined HTML/CSS with [render.py](src/gentlii_foundations/render.py)
9. Optionally run separate validation commands against generated product-description markdown with [pipeline.py](src/gentlii_foundations/pipeline.py)

## Architecture

The codebase is split by responsibility.

- `cli.py`
  Thin command-line wrapper. It parses arguments and calls `build_foundations(...)`, `run_product_guard(...)`, or `run_feature_validator(...)`.
- `pipeline.py`
  Orchestrates the end-to-end build plus the separate product validation flows. This is the central application flow.
- `paths.py`
  Defines the expected repository layout and validates required directories.
- `discovery.py`
  Finds supported source files in `foundations-input`.
- `extraction.py`
  Converts supported files into plain extracted text.
- `analysis.py`
  Combines extracted documents into prompt payloads and generates markdown artifacts for each target artifact.
- `prompts.py`
  Loads prompt templates from `src/gentlii_foundations/prompt_templates`.
- `openai_client.py`
  Encapsulates the OpenAI API call so model selection and timeout behavior stay out of the pipeline.
- `render.py`
  Writes artifact markdown files and renders the combined static HTML/CSS view.
- `models.py`
  Shared dataclasses and enums used across the pipeline.
- `config.py`
  Loads `.env` values and allows explicit environment variables to override them.

## Input and Output Contract

Input folder:

- `product-definitions/foundations-input`
- `product-definitions/feature-requests`

Output folder:

- `product-definitions/product-description`

Generated output is deterministic in structure:

- one `.md` file per artifact name
- one `product-guard.md` after running the separate guard command
- one `feature-validator.md` after running the separate feature validator command
- one `index.html`
- one `product-guard.html`
- one `feature-validator.html`
- one `styles.css`

The renderer also enforces a small output contract:

- artifact filenames must be slug-safe
- duplicate artifact names are rejected
- combined HTML is built from the generated markdown files

## Configuration

Settings are loaded from `.env` and environment variables.

- `OPENAI_API_KEY` is required
- `GENTLII_MODEL` is optional
- default model is `gpt-5.2`

Environment variables override values from `.env`.

## Running Locally

Full build:

```bash
env -u OPENAI_API_KEY zsh -lc 'set -a; source .env; set +a; ./.venv/bin/gentlii-foundations build product-definitions'
```

This command:

- clears any shell-level `OPENAI_API_KEY`
- loads `.env`
- runs the full extraction, analysis, and rendering pipeline

Run product guard after a build has produced or refreshed product-description markdown:

```bash
env -u OPENAI_API_KEY zsh -lc 'set -a; source .env; set +a; ./.venv/bin/gentlii-foundations guard product-definitions'
```

This command:

- reads markdown files from `product-definitions/product-description`
- excludes `product-definitions/product-description/product-guard.md`
- writes a refreshed `product-definitions/product-description/product-guard.md`
- writes a refreshed `product-definitions/product-description/product-guard.html`

Run feature validation against the generated artifacts plus a feature request file:

```bash
env -u OPENAI_API_KEY zsh -lc 'set -a; source .env; set +a; ./.venv/bin/gentlii-foundations feature-validate product-definitions product-definitions/feature-requests/feature-request-template.md'
```

This command:

- reads markdown files from `product-definitions/product-description`
- excludes `product-definitions/product-description/product-guard.md`
- excludes `product-definitions/product-description/feature-validator.md`
- reads the feature request file from `product-definitions/feature-requests/feature-request-template.md`
- writes a refreshed `product-definitions/product-description/feature-validator.md`
- writes a refreshed `product-definitions/product-description/feature-validator.html`

Use [feature-request-template.md](product-definitions/feature-requests/feature-request-template.md) as the starting point for new requests.

Render only from the existing generated markdown files:

```bash
./.venv/bin/python -c '
from pathlib import Path
from gentlii_foundations.models import GeneratedArtifact
from gentlii_foundations.render import write_artifacts

output_dir = Path("product-definitions/product-description")
artifacts = [
    GeneratedArtifact(name=path.stem, markdown=path.read_text(encoding="utf-8"))
    for path in sorted(output_dir.glob("*.md"))
]
write_artifacts(output_dir, artifacts)
'
```

That render-only path regenerates:

- `product-definitions/product-description/index.html`
- `product-definitions/product-description/styles.css`

It does not call extraction or OpenAI.

## GitHub Actions

There are four workflows in `.github/workflows/`:

- `ci.yml`
  Runs test and dependency-security checks for code changes. It ignores `product-definitions/**`.
- `foundations.yml`
  Runs when `product-definitions/foundations-input/**` changes. It builds the artifacts, runs product guard, stages all generated HTML files, commits refreshed generated output when needed, and then calls the reusable Pages publisher.
- `product-guard.yml`
  Manual-only via `workflow_dispatch`. It runs `gentlii-foundations guard product-definitions`, stages all current HTML output, commits refreshed `product-guard.md` and `product-guard.html` when needed, and then calls the reusable Pages publisher.
- `feature-validation.yml`
  Runs when the label `feature-validation` is added to an issue. It converts the issue into a temporary feature request file, runs `gentlii-foundations feature-validate product-definitions <temp-file>`, comments the generated validator markdown back onto the issue, stages all current HTML output, and then calls the reusable Pages publisher.
- `publish-pages.yml`
  Reusable workflow triggered via `workflow_call`. Caller workflows upload a staged site artifact, and this workflow publishes all staged `*.html` files plus shared assets to GitHub Pages.

## Tests

Run the full test suite:

```bash
./.venv/bin/python -m pytest -q
```

Useful focused test runs:

```bash
./.venv/bin/python -m pytest -q tests/test_render.py
./.venv/bin/python -m pytest -q tests/test_ci_workflow.py
```

## Related Docs

- [CONTEXT.md](CONTEXT.md): broader product context and intent
- [RUNNING_LOCALLY.md](RUNNING_LOCALLY.md): local execution notes
