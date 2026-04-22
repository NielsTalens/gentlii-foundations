from pathlib import Path


def test_ci_workflow_includes_test_and_security_jobs():
    workflow = Path(".github/workflows/ci.yml").read_text(encoding="utf-8")

    assert "push:" in workflow
    assert "pull_request:" in workflow
    assert "paths-ignore:" in workflow
    assert "product-definitions/**" in workflow
    assert "test:" in workflow
    assert "security:" in workflow
    assert "pytest -v" in workflow
    assert "pip-audit" in workflow


def test_foundations_workflow_deploys_pages_from_generated_site():
    workflow = Path(".github/workflows/foundations.yml").read_text(encoding="utf-8")

    assert "pages: write" in workflow
    assert "id-token: write" in workflow
    assert "Validate generated HTML for publish safety" in workflow
    assert "python -m gentlii_foundations.html_security" in workflow
    assert "actions/configure-pages" in workflow
    assert "actions/upload-pages-artifact" in workflow
    assert "actions/deploy-pages" in workflow
    assert "product-definitions/product-description/index.html" in workflow
    assert "product-definitions/product-description/styles.css" in workflow
