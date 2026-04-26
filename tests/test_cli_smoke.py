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
