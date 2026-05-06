from gentlii_foundations.cli import main


def test_main_exists():
    assert callable(main)


def test_guard_command_dispatches_to_product_guard(monkeypatch, tmp_path):
    root = tmp_path / "product-definitions"
    called = {"root": None}

    monkeypatch.setattr(
        "gentlii_foundations.cli.run_product_guard",
        lambda input_root, report=print: called.__setitem__("root", input_root),
    )

    exit_code = main(["guard", str(root)])

    assert exit_code == 0
    assert called["root"] == root


def test_feature_validate_command_dispatches_to_feature_validator(monkeypatch, tmp_path):
    root = tmp_path / "product-definitions"
    feature_request_file = tmp_path / "feature-request.md"
    called = {"root": None, "feature_request_file": None}

    monkeypatch.setattr(
        "gentlii_foundations.pipeline.run_feature_validator",
        lambda input_root, input_feature_request_file, report=print: called.update(
            root=input_root,
            feature_request_file=input_feature_request_file,
        ),
    )

    exit_code = main(["feature-validate", str(root), str(feature_request_file)])

    assert exit_code == 0
    assert called["root"] == root
    assert called["feature_request_file"] == feature_request_file
