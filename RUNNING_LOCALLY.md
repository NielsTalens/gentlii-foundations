# Running Locally

From the repository root:

```bash
cd /home/nelis/Dev/gentlii-foundations
```

## Run the application

If `.venv` already exists, run:

```bash
env -u OPENAI_API_KEY zsh -lc 'set -a; source .env; set +a; ./.venv/bin/gentlii-foundations build /home/nelis/Dev/gentlii-foundations/product-definitions'
```

This clears any shell-level `OPENAI_API_KEY`, loads the values from `.env`, and runs the local CLI against `product-definitions`.

## Check the CLI

```bash
.venv/bin/gentlii-foundations --help
```

## Run tests

```bash
.venv/bin/python -m pytest -v
```

## Recreate the virtual environment

If `.venv` is missing, create it once:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install pytest setuptools wheel
.venv/bin/python -m pip install -e . --no-build-isolation
```
