from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class ArtifactName(str, Enum):
    STRATEGY = "strategy"
    BUSINESS_CASE = "business-case"
    PRODUCT_VISION = "product-vision"
    JTBD = "jtbd"
    PRODUCT_CHARTER = "product-charter"


@dataclass(frozen=True)
class ProductPaths:
    root_dir: Path
    input_dir: Path
    output_dir: Path


@dataclass(frozen=True)
class ExtractedDocument:
    path: Path
    title: str
    text: str


@dataclass(frozen=True)
class GeneratedArtifact:
    name: str
    markdown: str
