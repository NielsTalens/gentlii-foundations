from pathlib import Path


def test_ci_workflow_includes_test_and_security_jobs():
    workflow = Path(".github/workflows/ci.yml").read_text(encoding="utf-8")

    assert "push:" in workflow
    assert "pull_request:" in workflow
    assert "test:" in workflow
    assert "security:" in workflow
    assert "pytest -v" in workflow
    assert "pip-audit" in workflow
