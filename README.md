# Gentlii Foundations

`gentlii-foundations` is a local Python CLI that turns source documents in a product repository into a structured product-definition package.

It reads source files from `product-definitions/foundations-input`, extracts text, generates artifact markdown with OpenAI, renders a publishable static site in `product-definitions/product-description`, and can run a separate guard pass over the generated markdown artifacts.

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
9. Optionally run the separate product guard command against generated product-description markdown with [pipeline.py](src/gentlii_foundations/pipeline.py)

## Architecture

The codebase is split by responsibility.

- `cli.py`
  Thin command-line wrapper. It parses arguments and calls `build_foundations(...)` or `run_product_guard(...)`.
- `pipeline.py`
  Orchestrates the end-to-end build and the separate product-guard flow. This is the central application flow.
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

Output folder:

- `product-definitions/product-description`

Generated output is deterministic in structure:

- one `.md` file per artifact name
- one `product-guard.md` after running the separate guard command
- one `index.html`
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

There are two workflows in `.github/workflows/`:

- `ci.yml`
  Runs test and dependency-security checks for code changes. It ignores `product-definitions/**`.
- `foundations.yml`
  Runs when `product-definitions/foundations-input/**` changes. It builds the artifacts and commits refreshed generated output when needed.
- `product-guard.yml`
  Trigger: GitHub Actions `workflow_run` for `Foundations`, with `types: [completed]`, and the guard job runs only when that workflow concludes successfully. It then runs `gentlii-foundations guard product-definitions`, evaluates the generated product-description markdown files except `product-guard.md`, and commits a refreshed `product-guard.md` when needed.

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
