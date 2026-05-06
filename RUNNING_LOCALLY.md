# Running Locally

Run all commands from the repository root.

## Recreate the virtual environment

If `.venv` is missing, create it once:

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install pytest setuptools wheel
./.venv/bin/python -m pip install -e . --no-build-isolation
```

## Check the CLI

```bash
./.venv/bin/gentlii-foundations --help
```

## Run the full build

```bash
env -u OPENAI_API_KEY zsh -lc 'set -a; source .env; set +a; ./.venv/bin/gentlii-foundations build product-definitions'
```

This:

- clears any shell-level `OPENAI_API_KEY`
- loads values from `.env`
- reads source files from `product-definitions/foundations-input`
- writes generated artifacts to `product-definitions/product-description`

## Run product guard

Run this after a build has produced or refreshed `product-definitions/product-description`:

```bash
env -u OPENAI_API_KEY zsh -lc 'set -a; source .env; set +a; ./.venv/bin/gentlii-foundations guard product-definitions'
```

This:

- reads generated markdown files from `product-definitions/product-description`
- excludes `product-definitions/product-description/product-guard.md`
- writes `product-definitions/product-description/product-guard.md`
- writes `product-definitions/product-description/product-guard.html`

## Run feature validation

Use the template at `product-definitions/feature-requests/feature-request-template.md` as the starting point for new requests.

```bash
env -u OPENAI_API_KEY zsh -lc 'set -a; source .env; set +a; ./.venv/bin/gentlii-foundations feature-validate product-definitions product-definitions/feature-requests/feature-request-template.md'
```

This:

- reads generated markdown files from `product-definitions/product-description`
- excludes `product-definitions/product-description/product-guard.md`
- excludes `product-definitions/product-description/feature-validator.md`
- reads the feature request markdown file you pass in
- writes `product-definitions/product-description/feature-validator.md`
- writes `product-definitions/product-description/feature-validator.html`

## Render only from existing markdown

This regenerates the static site without calling extraction or OpenAI.

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

This rewrites:

- `product-definitions/product-description/index.html`
- `product-definitions/product-description/styles.css`

## Run tests

Run the full suite:

```bash
./.venv/bin/python -m pytest -q
```

Useful focused runs:

```bash
./.venv/bin/python -m pytest -q tests/test_render.py
./.venv/bin/python -m pytest -q tests/test_pipeline.py
./.venv/bin/python -m pytest -q tests/test_cli_smoke.py
```
