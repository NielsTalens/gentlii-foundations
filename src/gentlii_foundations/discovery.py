from __future__ import annotations

from pathlib import Path


SUPPORTED_EXTENSIONS = {".docx", ".pdf"}


def discover_source_files(input_dir: Path) -> list[Path]:
    return sorted(
        path for path in Path(input_dir).iterdir() if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )
