from __future__ import annotations

from pathlib import Path

from gentlii_foundations.analysis import generate_artifacts
from gentlii_foundations.config import load_settings
from gentlii_foundations.discovery import discover_source_files
from gentlii_foundations.extraction import extract_documents
from gentlii_foundations.openai_client import FoundationsClient
from gentlii_foundations.paths import resolve_product_paths
from gentlii_foundations.render import write_artifacts


def build_foundations(root: Path, report=None) -> None:
    paths = resolve_product_paths(Path(root))
    source_files = discover_source_files(paths.input_dir)
    _report(report, f"Found {len(source_files)} supported source files.")
    documents = extract_documents(source_files)
    _report(report, f"Extracted {len(documents)} source documents.")
    settings = load_settings()
    # The pipeline stays linear on purpose so the later Git-triggered entry point can reuse it unchanged.
    client = FoundationsClient(api_key=settings.openai_api_key, model=settings.model)
    _report(report, "Generating foundation artifacts with OpenAI.")
    artifacts = generate_artifacts(documents, client)
    write_artifacts(paths.output_dir, artifacts)
    _report(report, f"Wrote {len(artifacts)} artifact files.")


def _report(report, message: str) -> None:
    if report is not None:
        report(message)
