from pathlib import Path

from gentlii_foundations.paths import resolve_product_paths


def test_resolve_product_paths_points_to_expected_directories(tmp_path: Path):
    root = tmp_path / "product-definitions"
    (root / "foundations-input").mkdir(parents=True)
    (tmp_path / "docs").mkdir()

    paths = resolve_product_paths(root)

    assert paths.input_dir == root / "foundations-input"
    assert paths.output_dir == tmp_path / "docs"
