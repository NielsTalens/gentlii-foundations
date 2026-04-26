from __future__ import annotations

from pathlib import Path

from gentlii_foundations.analysis import generate_artifacts, target_artifacts
from gentlii_foundations.config import load_settings
from gentlii_foundations.discovery import discover_source_files
from gentlii_foundations.extraction import extract_documents
from gentlii_foundations.models import ExtractedDocument
from gentlii_foundations.openai_client import FoundationsClient
from gentlii_foundations.paths import resolve_product_paths
from gentlii_foundations.render import write_artifacts, write_markdown_artifact


def build_foundations(root: Path, report=None) -> None:
    paths = resolve_product_paths(Path(root))
    _report(report, f"Building foundations from root: {paths.root_dir}")
    _report(report, f"Using input directory: {paths.input_dir}")
    _report(report, f"Using output directory: {paths.output_dir}")
    source_files = discover_source_files(paths.input_dir)
    _report(report, f"Found {len(source_files)} supported source files.")
    documents = extract_documents(source_files)
    _report(report, f"Extracted {len(documents)} source documents.")
    settings = load_settings()
    # The pipeline stays linear on purpose so the later Git-triggered entry point can reuse it unchanged.
    client = FoundationsClient(api_key=settings.openai_api_key, model=settings.model)
    _report(report, "Generating 4 foundation artifacts with OpenAI.")
    artifacts = generate_artifacts(documents, client, report=report)
    _report(report, "Rendering markdown and static site output.")
    write_artifacts(paths.output_dir, artifacts)
    _report(report, f"Wrote {len(artifacts)} artifact files plus index.html and styles.css.")


def run_product_guard(root: Path, report=None) -> None:
    paths = resolve_product_paths(Path(root))
    _report(report, f"Running product guard from root: {paths.root_dir}")
    _report(report, f"Using output directory: {paths.output_dir}")
    documents = _discover_generated_markdown_documents(paths.output_dir)
    if not documents:
        raise ValueError(f"No generated markdown artifacts found in {paths.output_dir}")
    _report(report, f"Found {len(documents)} generated markdown artifacts for alignment analysis.")
    settings = load_settings()
    client = FoundationsClient(api_key=settings.openai_api_key, model=settings.model)
    _report(report, "Generating 1 product guard artifact with OpenAI.")
    artifacts = generate_artifacts(documents, client, report=report, artifact_names=["product-guard"])
    artifact = next(artifact for artifact in artifacts if artifact.name == "product-guard")
    output_path = paths.output_dir / "product-guard.md"
    write_markdown_artifact(output_path, artifact)
    _report(report, f"Wrote guard report to {output_path}.")


def _discover_generated_markdown_documents(output_dir: Path) -> list[ExtractedDocument]:
    ordered_paths = {name: Path(output_dir) / f"{name}.md" for name in target_artifacts()}
    documents: list[ExtractedDocument] = []
    for path in ordered_paths.values():
        if not path.is_file():
            continue
        documents.append(
            ExtractedDocument(
                path=path,
                title=path.stem,
                text=path.read_text(encoding="utf-8"),
            )
        )
    extra_paths = sorted(
        path
        for path in Path(output_dir).glob("*.md")
        if path.name != "product-guard.md" and path.stem not in ordered_paths
    )
    for path in extra_paths:
        documents.append(
            ExtractedDocument(
                path=path,
                title=path.stem,
                text=path.read_text(encoding="utf-8"),
            )
        )
    return documents


def _report(report, message: str) -> None:
    if report is not None:
        report(message)
