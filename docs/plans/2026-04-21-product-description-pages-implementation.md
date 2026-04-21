# Product Description Pages Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Generate a single static HTML page and matching stylesheet from `product-definitions/product-description/*.md`, using the Gentlii app styling so the output can be published through GitHub Pages.

**Architecture:** Extend the existing render pipeline so it still writes markdown artifacts, then add a static site export step that reads those markdown files and emits `index.html` plus `styles.css` into the same output directory. The HTML renderer should use a lightweight markdown-to-HTML conversion path and a small HTML template tailored to long-form reading while reusing the Gentlii app’s visual language.

**Tech Stack:** Python 3.12, existing `gentlii_foundations` CLI/pipeline modules, `pytest`, standard library HTML/file handling, optional existing markdown library if already available in project dependencies.

---

### Task 1: Confirm renderer contract with failing tests

**Files:**
- Modify: `tests/test_render.py`
- Modify: `src/gentlii_foundations/render.py`

**Step 1: Write the failing test**

Add tests that expect:
- markdown files are still written
- `index.html` is generated
- `styles.css` is generated

Example assertions:

```python
def test_write_artifacts_creates_static_site_files(tmp_path):
    artifacts = [
        GeneratedArtifact(name="strategy", markdown="# Strategy\n\nBody text.\n"),
        GeneratedArtifact(name="jtbd", markdown="# JTBD\n\n- First\n- Second\n"),
    ]

    write_artifacts(tmp_path, artifacts)

    assert (tmp_path / "strategy.md").exists()
    assert (tmp_path / "jtbd.md").exists()
    assert (tmp_path / "index.html").exists()
    assert (tmp_path / "styles.css").exists()
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_render.py -v`
Expected: FAIL because `index.html` and `styles.css` are not generated.

**Step 3: Write minimal implementation**

Update `write_artifacts` to preserve the existing markdown output and call helpers that also generate:
- `index.html`
- `styles.css`

Do not fully solve markdown rendering yet. Only create the files so the test can pass.

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_render.py -v`
Expected: PASS for the new file-generation assertions.

**Step 5: Commit**

```bash
git add tests/test_render.py src/gentlii_foundations/render.py
git commit -m "feat: add static site output files"
```

### Task 2: Add HTML rendering for combined markdown content

**Files:**
- Modify: `tests/test_render.py`
- Modify: `src/gentlii_foundations/render.py`

**Step 1: Write the failing test**

Add a test that verifies:
- artifact titles appear in `index.html`
- markdown headings render as HTML headings
- list items render as HTML list items
- section anchors exist

Example assertions:

```python
def test_write_artifacts_renders_combined_html_content(tmp_path):
    artifact = GeneratedArtifact(
        name="product-vision",
        markdown="# Product Vision\n\nIntro paragraph.\n\n- One\n- Two\n",
    )

    write_artifacts(tmp_path, [artifact])
    html = (tmp_path / "index.html").read_text(encoding="utf-8")

    assert "Product Vision" in html
    assert "<li>One</li>" in html
    assert "href=\"#product-vision\"" in html
    assert "id=\"product-vision\"" in html
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_render.py::test_write_artifacts_renders_combined_html_content -v`
Expected: FAIL because the HTML file is still placeholder output.

**Step 3: Write minimal implementation**

In `src/gentlii_foundations/render.py`:
- add a helper to turn markdown into HTML
- prefer a small library already present in dependencies if available
- otherwise implement only the subset needed by current artifacts and tests:
  - `#` headings
  - paragraphs
  - bullet lists
- build a deterministic combined page from the artifacts list instead of rescanning the directory

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_render.py -v`
Expected: PASS for combined content rendering.

**Step 5: Commit**

```bash
git add tests/test_render.py src/gentlii_foundations/render.py
git commit -m "feat: render combined product description html"
```

### Task 3: Port Gentlii app styling into generated stylesheet

**Files:**
- Modify: `tests/test_render.py`
- Modify: `src/gentlii_foundations/render.py`
- Reference: `../gentlii/public/styles.css`

**Step 1: Write the failing test**

Add tests that assert `styles.css` contains core Gentlii app design markers and page-specific classes needed by the export.

Example assertions:

```python
def test_write_artifacts_generates_gentlii_based_stylesheet(tmp_path):
    write_artifacts(tmp_path, [GeneratedArtifact(name="strategy", markdown="# Strategy\n")])
    css = (tmp_path / "styles.css").read_text(encoding="utf-8")

    assert "--bg:" in css
    assert ".app-shell" in css
    assert ".page-header" in css
    assert ".doc-nav" in css
    assert ".doc-card" in css
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_render.py::test_write_artifacts_generates_gentlii_based_stylesheet -v`
Expected: FAIL because the generated stylesheet lacks the expected structure.

**Step 3: Write minimal implementation**

Update the stylesheet generator to:
- embed or derive the Gentlii app base tokens and layout rules
- add the export-specific classes:
  - `.doc-nav`
  - `.doc-nav-list`
  - `.doc-card`
  - `.doc-content`
- keep rules self-contained so the output works on GitHub Pages without referencing sibling repo files

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_render.py -v`
Expected: PASS with stylesheet assertions.

**Step 5: Commit**

```bash
git add tests/test_render.py src/gentlii_foundations/render.py
git commit -m "feat: apply gentlii app styling to static export"
```

### Task 4: Verify pipeline integration

**Files:**
- Modify: `tests/test_pipeline.py`
- Reference: `src/gentlii_foundations/pipeline.py`

**Step 1: Write the failing test**

Add or adjust a pipeline test to assert that a normal build still calls `write_artifacts` once with generated artifacts and therefore implicitly creates the static export.

Example pattern:

```python
def test_build_foundations_writes_generated_outputs(monkeypatch, tmp_path):
    captured = {}

    def fake_write_artifacts(output_dir, artifacts):
        captured["output_dir"] = output_dir
        captured["artifacts"] = artifacts

    monkeypatch.setattr("gentlii_foundations.pipeline.write_artifacts", fake_write_artifacts)
```

**Step 2: Run test to verify it fails only if behavior drift exists**

Run: `pytest tests/test_pipeline.py -v`
Expected: PASS if current integration is already correct, otherwise FAIL and reveal the gap.

**Step 3: Write minimal implementation**

Only if needed, adjust pipeline code so the render step is still invoked exactly once with the generated artifacts list.

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_pipeline.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add tests/test_pipeline.py src/gentlii_foundations/pipeline.py
git commit -m "test: confirm pipeline drives static export"
```

### Task 5: Document GitHub Pages publishing contract

**Files:**
- Modify: `README.md`
- Optional: create `.github/workflows/<pages-workflow>.yml`
- Test: `tests/test_ci_workflow.py`

**Step 1: Write the failing test**

If a Pages workflow is added, write or extend a workflow test that asserts the publish job points at the generated product-description folder or uploads the correct Pages artifact.

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_ci_workflow.py -v`
Expected: FAIL only if workflow verification is introduced and not yet implemented.

**Step 3: Write minimal implementation**

Document or implement the publishing flow:
- build foundations output
- publish `product-definitions/product-description/`

Prefer the smallest viable change. If workflow addition is too broad for this iteration, document the contract clearly in `README.md` instead.

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_ci_workflow.py -v`
Expected: PASS if workflow tests were changed; otherwise run the full suite section relevant to docs and rendering.

**Step 5: Commit**

```bash
git add README.md .github/workflows tests/test_ci_workflow.py
git commit -m "docs: document github pages publishing flow"
```

### Task 6: Final verification

**Files:**
- Verify: `src/gentlii_foundations/render.py`
- Verify: `tests/test_render.py`
- Verify: `tests/test_pipeline.py`
- Verify: `README.md`

**Step 1: Run targeted tests**

Run: `pytest tests/test_render.py tests/test_pipeline.py -v`
Expected: PASS.

**Step 2: Run broader regression tests**

Run: `pytest -v`
Expected: PASS, or any unrelated pre-existing failures clearly identified.

**Step 3: Perform a manual smoke check**

Run: `python -m gentlii_foundations.cli build product-definitions`
Expected:
- markdown files generated in `product-definitions/product-description/`
- `index.html` generated
- `styles.css` generated

**Step 4: Inspect output**

Run: `rg -n \"Product Vision|Strategy|JTBD\" product-definitions/product-description/index.html`
Expected: content and anchors present in the rendered page.

**Step 5: Commit**

```bash
git add src/gentlii_foundations/render.py tests/test_render.py tests/test_pipeline.py README.md
git commit -m "feat: publish product descriptions as static html"
```
