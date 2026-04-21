# Foundations Workflow Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a path-triggered GitHub workflow that runs the Foundations CLI when `product-definitions/foundations-input` changes, replaces managed output files in `product-definitions/product-description`, and commits those generated files back to the same branch only when output changed.

**Architecture:** Keep the GitHub Actions workflow thin and reusable by calling a single CLI command from the repository root. Move output ownership rules into the Python pipeline so managed artifacts are replaced deterministically while unrelated files in `product-description` remain untouched.

**Tech Stack:** Python 3.12, `pytest`, GitHub Actions YAML, existing Gentlii Foundations CLI and pipeline modules.

---

### Task 1: Lock down managed artifact write behavior

**Files:**
- Modify: `src/gentlii_foundations/pipeline.py`
- Modify: `src/gentlii_foundations/render.py`
- Modify: `src/gentlii_foundations/models.py` if artifact metadata needs to be clarified
- Test: `tests/test_pipeline.py`

**Step 1: Write the failing test**

Add a test that creates:
- one existing managed artifact file in `product-description`
- one unrelated manual file in `product-description`
- generated artifact results for the managed set

Assert that running the write/render pipeline:
- fully replaces the managed artifact file contents
- leaves the unrelated manual file unchanged

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_pipeline.py -v`
Expected: FAIL because current behavior does not explicitly guarantee managed replacement plus unrelated-file preservation.

**Step 3: Write minimal implementation**

Update the pipeline/render path so it writes only known artifact targets, replacing their contents atomically or by deterministic overwrite. Do not scan and delete unrelated files in `product-description`.

Keep the managed artifact list explicit and derived from the domain model rather than filesystem heuristics.

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_pipeline.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/gentlii_foundations/pipeline.py src/gentlii_foundations/render.py src/gentlii_foundations/models.py tests/test_pipeline.py
git commit -m "feat: preserve unmanaged product description files"
```

### Task 2: Expose a stable automation CLI command

**Files:**
- Modify: `src/gentlii_foundations/cli.py`
- Modify: `README.md`
- Test: `tests/test_cli_smoke.py`

**Step 1: Write the failing test**

Add a CLI-focused test that invokes the intended automation command shape, for example a command that accepts the `product-definitions` root and runs the full pipeline.

Assert:
- the command is callable through the CLI entry point
- the command exits successfully on a valid repo layout

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_cli_smoke.py -v`
Expected: FAIL because the automation-oriented command contract is not fully defined or covered.

**Step 3: Write minimal implementation**

Add or tighten a single stable CLI command for workflow use. The command should:
- accept the `product-definitions` root
- run discovery, extraction, analysis, and rendering
- exit non-zero on failure

Document the exact command in `README.md` so both GitHub Actions and future Azure DevOps pipelines use the same interface.

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_cli_smoke.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/gentlii_foundations/cli.py README.md tests/test_cli_smoke.py
git commit -m "feat: define workflow automation cli command"
```

### Task 3: Add a GitHub workflow that writes back generated artifacts

**Files:**
- Modify: `.github/workflows/ci.yml` or split into a dedicated workflow such as `.github/workflows/foundations.yml`
- Modify: `README.md`

**Step 1: Write the failing test**

There is no practical YAML unit test in this repo, so the first verification step is behavioral. Define the intended workflow behavior in `README.md` before editing the YAML:
- trigger only on `product-definitions/foundations-input/**`
- run the CLI command
- stage only `product-definitions/product-description`
- commit only when there is a diff

**Step 2: Run verification to confirm current workflow does not meet the requirement**

Inspect: `.github/workflows/ci.yml`
Expected: Current workflow runs tests and security checks only; it does not trigger on `foundations-input` or commit generated output.

**Step 3: Write minimal implementation**

Implement a workflow that:
- triggers on pushes affecting `product-definitions/foundations-input/**`
- grants the minimum required permissions, including write access if needed for committing
- checks out the repo with credentials suitable for pushing
- sets up Python 3.12
- installs the project
- runs the stable CLI command
- configures a bot git identity
- stages only `product-definitions/product-description`
- exits cleanly when there is no diff
- commits and pushes when there is a diff

Avoid adding workflow logic that duplicates Python behavior.

**Step 4: Run validation to verify it is structurally correct**

Run:
```bash
python - <<'PY'
from pathlib import Path
print(Path(".github/workflows").read_text() if False else "skip")
PY
```

Then run the relevant local test suite:
`pytest -v`

Expected:
- Python tests still pass
- Workflow YAML references the documented CLI command and scoped paths

**Step 5: Commit**

```bash
git add .github/workflows/ci.yml README.md
git commit -m "feat: automate foundations generation workflow"
```

### Task 4: Verify end-to-end repository behavior

**Files:**
- Modify: `tests/integration/test_crm_product.py` if an end-to-end artifact write assertion is missing
- Optionally modify: `tests/conftest.py`

**Step 1: Write the failing test**

Add or extend an integration test that runs the pipeline against a product fixture and asserts:
- expected managed artifact files are produced in `product-description`
- existing unmanaged files remain untouched

**Step 2: Run test to verify it fails**

Run: `pytest tests/integration/test_crm_product.py -v`
Expected: FAIL until the end-to-end write behavior matches the workflow contract.

**Step 3: Write minimal implementation**

Adjust integration setup or pipeline behavior as needed to satisfy the contract without widening scope beyond managed artifact replacement.

**Step 4: Run test to verify it passes**

Run: `pytest tests/integration/test_crm_product.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add tests/integration/test_crm_product.py tests/conftest.py src/gentlii_foundations/pipeline.py src/gentlii_foundations/render.py
git commit -m "test: cover workflow artifact writeback contract"
```

### Task 5: Final verification and docs pass

**Files:**
- Modify: `README.md` if verification reveals missing operational docs

**Step 1: Run focused verification**

Run:
```bash
pytest tests/test_cli_smoke.py tests/test_pipeline.py tests/integration/test_crm_product.py -v
```

Expected: PASS

**Step 2: Run full verification**

Run:
```bash
pytest -v
```

Expected: PASS

**Step 3: Review git diff**

Run:
```bash
git diff -- .github/workflows README.md src/gentlii_foundations tests
```

Confirm:
- workflow path trigger is limited to `foundations-input`
- only `product-description` is staged in the workflow
- docs describe the automation command and write-back behavior

**Step 4: Commit any final doc cleanup**

```bash
git add README.md
git commit -m "docs: document foundations workflow automation"
```
