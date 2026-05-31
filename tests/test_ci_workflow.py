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


def test_foundations_workflow_builds_and_commits_generated_site():
    workflow = Path(".github/workflows/foundations.yml").read_text(encoding="utf-8")

    assert "Validate generated HTML for publish safety" not in workflow
    assert "python -m gentlii_foundations.html_security" not in workflow
    assert "pages: write" in workflow
    assert "id-token: write" in workflow
    assert "actions/configure-pages" not in workflow
    assert "actions/upload-pages-artifact" not in workflow
    assert "actions/deploy-pages" not in workflow
    assert "gentlii-foundations build product-definitions" in workflow
    assert "gentlii-foundations guard product-definitions" in workflow
    assert "cp product-definitions/product-description/*.html pages-source/" in workflow
    assert "uses: ./.github/workflows/publish-pages.yml" in workflow
    assert 'git commit -m "chore: refresh generated product description and guard"' in workflow


def test_product_guard_workflow_runs_after_foundations_and_deploys_pages():
    workflow = Path(".github/workflows/product-guard.yml").read_text(encoding="utf-8")

    assert "workflow_run:" not in workflow
    assert "workflow_dispatch:" in workflow
    assert "github.event.workflow_run.conclusion == 'success'" not in workflow
    assert "pages: write" in workflow
    assert "id-token: write" in workflow
    assert "gentlii-foundations guard product-definitions" in workflow
    assert "python -m gentlii_foundations.html_security" not in workflow
    assert "github.event.workflow_run.head_branch" not in workflow
    assert "github.event.workflow_run.head_sha" not in workflow
    assert "uses: ./.github/workflows/publish-pages.yml" in workflow
    assert "actions/configure-pages" not in workflow
    assert "actions/upload-pages-artifact" not in workflow
    assert "actions/deploy-pages" not in workflow
    assert "cp product-definitions/product-description/*.html pages-source/" in workflow
    assert "git add product-definitions/product-description/product-guard.md" in workflow
    assert "git add product-definitions/product-description/product-guard.html" in workflow
    assert 'git commit -m "chore: refresh product guard"' in workflow


def test_feature_validation_workflow_runs_on_feature_validation_label_and_comments_result():
    workflow = Path(".github/workflows/feature-validation.yml").read_text(encoding="utf-8")

    assert "issues:" in workflow
    assert "types: [labeled]" in workflow
    assert "github.event.label.name == 'feature-validation'" in workflow
    assert "issues: write" in workflow
    assert "actions/checkout@v5" in workflow
    assert "actions/setup-python@v6" in workflow
    assert "python -m pip install -e . --no-build-isolation" in workflow
    assert 'issue_title: ${{ github.event.issue.title }}' in workflow
    assert 'issue_body: ${{ github.event.issue.body }}' in workflow
    assert 'issue_url: ${{ github.event.issue.html_url }}' in workflow
    assert "feature-request.md" in workflow
    assert "gentlii-foundations feature-validate product-definitions" in workflow
    assert "product-definitions/product-description/feature-validator.md" in workflow
    assert "gh issue comment" in workflow
    assert "Label issue with alignment score" in workflow
    assert "alignment: 1/5" in workflow
    assert "alignment: 5/5" in workflow
    assert "gh label create" in workflow
    assert "gh issue edit" in workflow
    assert "uses: ./.github/workflows/publish-pages.yml" in workflow
    assert "cp product-definitions/product-description/*.html pages-source/" in workflow


def test_publish_pages_workflow_is_reusable_and_tolerates_missing_html_files():
    workflow = Path(".github/workflows/publish-pages.yml").read_text(encoding="utf-8")

    assert "workflow_call:" in workflow
    assert "artifact_name:" in workflow
    assert "page_files:" not in workflow
    assert "pages: write" in workflow
    assert "id-token: write" in workflow
    assert "actions/configure-pages" in workflow
    assert "actions/upload-pages-artifact" in workflow
    assert "actions/deploy-pages" in workflow
    assert "site-source/styles.css" in workflow
    assert "logo.png" in workflow
    assert "cp site-source/*.html _site/" in workflow
