from gentlii_foundations.analysis import target_artifacts


def test_target_artifacts_match_readme_scope():
    assert target_artifacts() == [
        "strategy",
        "business-case",
        "product-vision",
        "jtbd",
        "product-charter",
    ]
