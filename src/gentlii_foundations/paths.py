from __future__ import annotations

from pathlib import Path

from gentlii_foundations.models import ProductPaths


class ProductPathError(ValueError):
    pass


def resolve_product_paths(root: Path) -> ProductPaths:
    root_dir = Path(root)
    input_dir = root_dir / "foundations-input"
    output_dir = root_dir / "product-description"

    missing = [str(path) for path in (input_dir, output_dir) if not path.is_dir()]
    if missing:
        raise ProductPathError(f"Missing required directories: {', '.join(missing)}")

    return ProductPaths(root_dir=root_dir, input_dir=input_dir, output_dir=output_dir)
