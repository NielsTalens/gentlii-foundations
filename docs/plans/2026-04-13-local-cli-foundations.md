# Gentlii Foundations Local CLI Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a local Python CLI that reads `foundations-input`, extracts text from `.docx` and `.pdf`, uses OpenAI to generate clean structured product definition markdown, and writes those files into `product-description`.

**Architecture:** Keep the system as a small pipeline with three explicit stages: document extraction, artifact analysis, and markdown rendering. Expose that pipeline through a single local CLI entry point so Git-triggered automation can later reuse the exact same command without changing core logic.

**Tech Stack:** Python 3.12+, standard library, `openai`, `python-docx`, one conservative PDF text extraction library, `pytest`, `.env` support via a minimal audited dependency or explicit environment variables.

---

### Task 1: Create the project skeleton

**Files:**
- Create: `pyproject.toml`
- Create: `src/gentlii_foundations/__init__.py`
- Create: `src/gentlii_foundations/cli.py`
- Create: `tests/test_cli_smoke.py`
- Modify: `README.md`

**Step 1: Write the failing test**

```python
from gentlii_foundations.cli import main


def test_main_exists():
    assert callable(main)
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_cli_smoke.py -v`
Expected: FAIL with import or module-not-found errors because the package does not exist yet.

**Step 3: Write minimal implementation**

Create a minimal package with:

```python
def main() -> int:
    return 0
```

Define the package metadata and CLI entry point in `pyproject.toml`.

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_cli_smoke.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add pyproject.toml README.md src/gentlii_foundations/__init__.py src/gentlii_foundations/cli.py tests/test_cli_smoke.py
git commit -m "chore: scaffold local foundations cli"
```

### Task 2: Lock down audited dependencies and configuration

**Files:**
- Modify: `pyproject.toml`
- Create: `.env.example`
- Create: `src/gentlii_foundations/config.py`
- Create: `tests/test_config.py`
- Modify: `README.md`

**Step 1: Write the failing test**

```python
import os

from gentlii_foundations.config import load_settings


def test_load_settings_reads_openai_api_key(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    settings = load_settings()
    assert settings.openai_api_key == "test-key"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_config.py -v`
Expected: FAIL because `load_settings` does not exist.

**Step 3: Write minimal implementation**

Add:
- a small settings object for API key and model name
- exact pinned dependencies in `pyproject.toml`
- `.env.example` with required variables only
- configuration loading that prefers environment variables and optionally supports `.env`

Keep dependency count minimal and document why each dependency exists.

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_config.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add pyproject.toml .env.example README.md src/gentlii_foundations/config.py tests/test_config.py
git commit -m "chore: add audited configuration layer"
```

### Task 3: Define the domain model for inputs and outputs

**Files:**
- Create: `src/gentlii_foundations/models.py`
- Create: `tests/test_models.py`

**Step 1: Write the failing test**

```python
from gentlii_foundations.models import ArtifactName, ExtractedDocument


def test_extracted_document_keeps_source_name():
    doc = ExtractedDocument(path="source.pdf", title="source.pdf", text="content")
    assert doc.title == "source.pdf"
    assert ArtifactName.STRATEGY.value == "strategy"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_models.py -v`
Expected: FAIL because the model types do not exist.

**Step 3: Write minimal implementation**

Add typed models for:
- supported artifact names
- extracted document payloads
- product folder paths
- generated markdown artifact results

Use dataclasses and enums from the standard library unless there is a compelling reason not to.

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_models.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/gentlii_foundations/models.py tests/test_models.py
git commit -m "feat: add domain models for foundations pipeline"
```

### Task 4: Resolve the product folder structure

**Files:**
- Create: `src/gentlii_foundations/paths.py`
- Create: `tests/test_paths.py`

**Step 1: Write the failing test**

```python
from pathlib import Path

from gentlii_foundations.paths import resolve_product_paths


def test_resolve_product_paths_points_to_expected_directories(tmp_path: Path):
    root = tmp_path / "product-definitions"
    (root / "foundations-input").mkdir(parents=True)
    (root / "product-description").mkdir()

    paths = resolve_product_paths(root)

    assert paths.input_dir == root / "foundations-input"
    assert paths.output_dir == root / "product-description"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_paths.py -v`
Expected: FAIL because the resolver does not exist.

**Step 3: Write minimal implementation**

Add path resolution and validation logic that:
- accepts a `product-definitions` root path
- checks required subdirectories
- raises clear errors for missing folders

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_paths.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/gentlii_foundations/paths.py tests/test_paths.py
git commit -m "feat: validate product definition folder layout"
```

### Task 5: Implement document discovery with format restrictions

**Files:**
- Create: `src/gentlii_foundations/discovery.py`
- Create: `tests/test_discovery.py`

**Step 1: Write the failing test**

```python
from gentlii_foundations.discovery import discover_source_files


def test_discover_source_files_only_returns_pdf_and_docx(tmp_path):
    (tmp_path / "a.docx").write_text("x")
    (tmp_path / "b.pdf").write_text("x")
    (tmp_path / "c.pptx").write_text("x")

    files = discover_source_files(tmp_path)

    assert [path.name for path in files] == ["a.docx", "b.pdf"]
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_discovery.py -v`
Expected: FAIL because file discovery does not exist.

**Step 3: Write minimal implementation**

Implement discovery that:
- scans `foundations-input`
- includes only `.docx` and `.pdf`
- sorts results deterministically
- ignores unsupported formats for v1

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_discovery.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/gentlii_foundations/discovery.py tests/test_discovery.py
git commit -m "feat: add supported source file discovery"
```

### Task 6: Add DOCX extraction

**Files:**
- Create: `src/gentlii_foundations/extractors/docx.py`
- Create: `tests/extractors/test_docx_extractor.py`

**Step 1: Write the failing test**

```python
from pathlib import Path

from docx import Document

from gentlii_foundations.extractors.docx import extract_docx_text


def test_extract_docx_text_reads_paragraphs(tmp_path: Path):
    path = tmp_path / "sample.docx"
    doc = Document()
    doc.add_paragraph("First line")
    doc.add_paragraph("Second line")
    doc.save(path)

    result = extract_docx_text(path)

    assert "First line" in result
    assert "Second line" in result
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/extractors/test_docx_extractor.py -v`
Expected: FAIL because the extractor does not exist.

**Step 3: Write minimal implementation**

Implement a small DOCX extractor that:
- uses `python-docx`
- concatenates non-empty paragraphs
- returns normalized plain text

**Step 4: Run test to verify it passes**

Run: `pytest tests/extractors/test_docx_extractor.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/gentlii_foundations/extractors/docx.py tests/extractors/test_docx_extractor.py
git commit -m "feat: add docx text extraction"
```

### Task 7: Add PDF extraction

**Files:**
- Create: `src/gentlii_foundations/extractors/pdf.py`
- Create: `tests/extractors/test_pdf_extractor.py`

**Step 1: Write the failing test**

```python
from pathlib import Path

from gentlii_foundations.extractors.pdf import extract_pdf_text


def test_extract_pdf_text_returns_string(tmp_path: Path):
    path = tmp_path / "sample.pdf"
    path.write_bytes(b"%PDF-1.4\n%stub\n")

    try:
        extract_pdf_text(path)
    except Exception as exc:
        assert "sample.pdf" in str(exc)
```
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/extractors/test_pdf_extractor.py -v`
Expected: FAIL because the extractor does not exist.

**Step 3: Write minimal implementation**

Choose one conservative PDF extraction dependency and document the choice in `README.md`.

Implement extraction that:
- reads text from each page
- joins pages with clear separators
- raises a descriptive exception if extraction fails or yields no usable text

Then replace the placeholder test with one that exercises a real tiny fixture PDF once the chosen library and fixture strategy are clear.

**Step 4: Run test to verify it passes**

Run: `pytest tests/extractors/test_pdf_extractor.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add README.md src/gentlii_foundations/extractors/pdf.py tests/extractors/test_pdf_extractor.py
git commit -m "feat: add pdf text extraction"
```

### Task 8: Build the extraction orchestrator

**Files:**
- Create: `src/gentlii_foundations/extraction.py`
- Create: `tests/test_extraction.py`

**Step 1: Write the failing test**

```python
from pathlib import Path

from gentlii_foundations.extraction import extract_documents


def test_extract_documents_returns_one_result_per_supported_file(tmp_path: Path):
    docx_path = tmp_path / "sample.docx"
    pdf_path = tmp_path / "sample.pdf"
    docx_path.write_text("placeholder")
    pdf_path.write_text("placeholder")

    results = extract_documents([docx_path, pdf_path])

    assert len(results) == 2
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_extraction.py -v`
Expected: FAIL because the orchestrator does not exist.

**Step 3: Write minimal implementation**

Implement orchestration that:
- dispatches by file extension
- returns typed `ExtractedDocument` objects
- preserves source filename for later traceability

Patch the test after introducing mocks or stubs for extractor calls so it remains deterministic.

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_extraction.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/gentlii_foundations/extraction.py tests/test_extraction.py
git commit -m "feat: orchestrate source document extraction"
```

### Task 9: Define prompts and artifact contracts

**Files:**
- Create: `src/gentlii_foundations/prompts.py`
- Create: `tests/test_prompts.py`

**Step 1: Write the failing test**

```python
from gentlii_foundations.prompts import build_artifact_prompt


def test_prompt_includes_no_invention_rule():
    prompt = build_artifact_prompt("strategy", "source text")
    assert "Do not invent missing information" in prompt
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_prompts.py -v`
Expected: FAIL because prompt construction does not exist.

**Step 3: Write minimal implementation**

Implement prompt builders that:
- define one contract per artifact
- require clean markdown output only
- explicitly forbid invention
- tell the model to omit unsupported claims rather than guessing

Keep prompts in plain Python constants or functions, not an extra templating layer.

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_prompts.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/gentlii_foundations/prompts.py tests/test_prompts.py
git commit -m "feat: define artifact extraction prompts"
```

### Task 10: Wrap the OpenAI client

**Files:**
- Create: `src/gentlii_foundations/openai_client.py`
- Create: `tests/test_openai_client.py`

**Step 1: Write the failing test**

```python
from gentlii_foundations.openai_client import FoundationsClient


def test_foundations_client_requires_api_key():
    client = FoundationsClient(api_key="test-key", model="gpt-5-mini")
    assert client.model == "gpt-5-mini"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_openai_client.py -v`
Expected: FAIL because the wrapper does not exist.

**Step 3: Write minimal implementation**

Implement a thin wrapper around the official SDK that:
- owns model selection
- sends a prompt and source text
- returns plain markdown text
- centralizes timeout and request settings

Avoid introducing an orchestration framework.

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_openai_client.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/gentlii_foundations/openai_client.py tests/test_openai_client.py
git commit -m "feat: add minimal openai client wrapper"
```

### Task 11: Generate the five foundation artifacts

**Files:**
- Create: `src/gentlii_foundations/analysis.py`
- Create: `tests/test_analysis.py`

**Step 1: Write the failing test**

```python
from gentlii_foundations.analysis import target_artifacts


def test_target_artifacts_match_readme_scope():
    assert target_artifacts() == [
        "strategy",
        "business-case",
        "product-vision",
        "jtbd",
        "product-charter",
    ]
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_analysis.py -v`
Expected: FAIL because analysis logic does not exist.

**Step 3: Write minimal implementation**

Implement analysis that:
- combines extracted source documents into one normalized analysis payload
- iterates over the five target artifacts
- requests one generated markdown result per artifact
- returns typed result objects

Stub the OpenAI client in tests so no network call happens during unit tests.

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_analysis.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/gentlii_foundations/analysis.py tests/test_analysis.py
git commit -m "feat: generate foundation artifacts from extracted text"
```

### Task 12: Render clean markdown files to disk

**Files:**
- Create: `src/gentlii_foundations/render.py`
- Create: `tests/test_render.py`

**Step 1: Write the failing test**

```python
from gentlii_foundations.models import GeneratedArtifact
from gentlii_foundations.render import write_artifacts


def test_write_artifacts_creates_expected_markdown_files(tmp_path):
    artifact = GeneratedArtifact(name="strategy", markdown="# Strategy\n")
    write_artifacts(tmp_path, [artifact])
    assert (tmp_path / "strategy.md").read_text() == "# Strategy\n"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_render.py -v`
Expected: FAIL because rendering does not exist.

**Step 3: Write minimal implementation**

Implement rendering that:
- writes one markdown file per artifact
- overwrites previous generated output deterministically
- uses UTF-8 text output

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_render.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/gentlii_foundations/render.py tests/test_render.py
git commit -m "feat: write generated markdown artifacts"
```

### Task 13: Wire the end-to-end build command

**Files:**
- Modify: `src/gentlii_foundations/cli.py`
- Create: `src/gentlii_foundations/pipeline.py`
- Create: `tests/test_pipeline.py`

**Step 1: Write the failing test**

```python
from pathlib import Path

from gentlii_foundations.pipeline import build_foundations


def test_build_foundations_runs_pipeline(monkeypatch, tmp_path: Path):
    root = tmp_path / "product-definitions"
    (root / "foundations-input").mkdir(parents=True)
    (root / "product-description").mkdir()

    called = {"rendered": False}

    def fake_write_artifacts(*args, **kwargs):
        called["rendered"] = True

    monkeypatch.setattr("gentlii_foundations.pipeline.write_artifacts", fake_write_artifacts)

    build_foundations(root)

    assert called["rendered"] is True
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_pipeline.py -v`
Expected: FAIL because the pipeline entry point does not exist.

**Step 3: Write minimal implementation**

Implement the end-to-end pipeline and update the CLI so a user can run:

```bash
python -m gentlii_foundations.cli build product-definitions
```

or the installed script equivalent from `pyproject.toml`.

Include clear error messages for:
- missing directories
- missing API key
- unsupported or unreadable inputs

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_pipeline.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/gentlii_foundations/cli.py src/gentlii_foundations/pipeline.py tests/test_pipeline.py
git commit -m "feat: add end-to-end local build command"
```

### Task 14: Add a fixture-backed integration test for the sample CRM product

**Files:**
- Create: `tests/integration/test_crm_product.py`
- Modify: `test-products/crm/`

**Step 1: Write the failing test**

```python
from pathlib import Path


def test_crm_fixture_folder_exists():
    root = Path("test-products/crm")
    assert root.exists()
```

**Step 2: Run test to verify it fails or is insufficient**

Run: `pytest tests/integration/test_crm_product.py -v`
Expected: PASS initially, then expand the test until it verifies the local command can process the sample product with mocked OpenAI responses.

**Step 3: Write minimal implementation**

Turn the test into a real integration check that:
- points the pipeline at a fixture-style product folder
- mocks the OpenAI client response per artifact
- verifies the five expected markdown files are written

If needed, create a dedicated test fixture tree separate from the user-owned sample documents.

**Step 4: Run test to verify it passes**

Run: `pytest tests/integration/test_crm_product.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add tests/integration/test_crm_product.py test-products/crm
git commit -m "test: cover sample crm build flow"
```

### Task 15: Document setup, security posture, and local usage

**Files:**
- Modify: `README.md`

**Step 1: Write the failing test**

There is no code test here. Write a short checklist in the task itself and verify each item manually:

```text
- install instructions are explicit
- environment variables are documented
- supported formats are documented
- security/audit dependency policy is documented
- local build command is documented
```

**Step 2: Run verification to show the doc gap**

Run: `rg -n "security|audit|OPENAI_API_KEY|product-description|docx|pdf" README.md`
Expected: Missing or incomplete coverage before the README update.

**Step 3: Write minimal implementation**

Update `README.md` so it explains:
- local-first scope
- the required folder structure
- the exact command to run
- dependency philosophy: simple, boring, audited, pinned
- supported formats for v1
- future Git-triggered automation as a later phase

**Step 4: Run verification to confirm coverage**

Run: `rg -n "security|audit|OPENAI_API_KEY|product-description|docx|pdf" README.md`
Expected: Matching lines for each topic.

**Step 5: Commit**

```bash
git add README.md
git commit -m "docs: describe local foundations workflow and security constraints"
```

### Task 16: Run the full test suite and a manual local build

**Files:**
- Modify: `product-definitions/product-description/` (generated output only)

**Step 1: Run the complete automated test suite**

Run: `pytest -v`
Expected: PASS

**Step 2: Run the CLI manually against the local product folder**

Run: `python -m gentlii_foundations.cli build product-definitions`
Expected: PASS and generate markdown files in `product-definitions/product-description`

**Step 3: Review generated output**

Manually verify:
- all five expected files exist
- files contain clean markdown only
- no confidence, scoring, or unsupported metadata was added

**Step 4: Commit**

```bash
git add product-definitions/product-description
git commit -m "test: verify local foundations build output"
```

### Task 17: Optional dependency audit checkpoint

**Files:**
- Modify: `README.md`
- Create: `docs/dependency-review.md`

**Step 1: Capture the dependency list**

Run: `python -m pip freeze`
Expected: a short list matching the intentionally small dependency set.

**Step 2: Document audit notes**

Write a brief review that records:
- package name
- why it is needed
- whether it is pinned
- why it was preferred over heavier alternatives

**Step 3: Commit**

```bash
git add docs/dependency-review.md README.md
git commit -m "docs: record initial dependency review"
```

