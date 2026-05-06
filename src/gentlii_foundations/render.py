from __future__ import annotations

import html
import re
from pathlib import Path

from gentlii_foundations.models import ArtifactName, GeneratedArtifact

_ORDERED_LIST_PATTERN = re.compile(r"^\d+\. (.+)$")
_SLUG_SAFE_ARTIFACT_NAME_PATTERN = re.compile(r"^[a-z0-9-]+$")
_BOLD_PATTERN = re.compile(r"\*\*(.+?)\*\*")
_H3_HEADING_PATTERN = re.compile(r"^<h3>(.+)</h3>$")
_SIDE_BY_SIDE_H3_TITLE_PAIRS = {
    frozenset({"Completeness", "Strength"}),
    frozenset({"Alignment score", "Confidence"}),
}
_LABELED_METRIC_PATTERN = re.compile(r"^\*\*(Alignment score|Confidence|Evidence):\*\*\s*(.+)$")
_METRIC_VALUE_CLASSES = {
    "approve": "metric-high",
    "high": "metric-high",
    "complete": "metric-high",
    "revise": "metric-medium",
    "medium": "metric-medium",
    "partial": "metric-medium",
    "reject": "metric-low",
    "low": "metric-low",
    "incomplete": "metric-low",
}
_ALIGNMENT_SCORE_PATTERN = re.compile(r"^[1-5]/5$")


def write_artifacts(output_dir: Path, artifacts: list[GeneratedArtifact]) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    _validate_artifact_names(artifacts)
    for artifact in artifacts:
        write_markdown_artifact(output_path / f"{artifact.name}.md", artifact)
    (output_path / "index.html").write_text(_render_index_html(_sort_artifacts(artifacts)), encoding="utf-8")
    (output_path / "styles.css").write_text(_render_stylesheet(), encoding="utf-8")


def write_markdown_artifact(output_path: Path, artifact: GeneratedArtifact) -> None:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(artifact.markdown, encoding="utf-8")


def write_artifact_page(
    output_path: Path,
    artifact: GeneratedArtifact,
    page_title: str,
    page_kicker: str,
) -> None:
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    styles_path = output_file.parent / "styles.css"
    styles_path.write_text(_render_stylesheet(), encoding="utf-8")
    output_file.write_text(_render_artifact_page(artifact, page_title=page_title, page_kicker=page_kicker), encoding="utf-8")


def _render_index_html(artifacts: list[GeneratedArtifact]) -> str:
    nav_items = "\n".join(
        f'          <li><a href="#{html.escape(artifact.name)}">{html.escape(_artifact_eyebrow(artifact))}</a></li>'
        for artifact in artifacts
    )
    sections = "\n".join(_render_artifact_section(artifact) for artifact in artifacts)
    return _render_page_shell(
        page_title="Gentlii Foundations",
        page_kicker="Product Foundations",
        brand_title="Gentlii Foundations",
        subtitle="Static export of product description artifacts for review and publishing.",
        nav_label="Artifacts",
        nav_markup=(
            "      <nav class=\"doc-nav\" aria-label=\"Artifact navigation\">\n"
            "        <div class=\"panel-eyebrow\">Artifacts</div>\n"
            "        <p><a href=\"product-guard.html\">Product Guard</a></p>\n"
            "        <ol class=\"doc-nav-list\">\n"
            f"{nav_items}\n"
            "        </ol>\n"
            "      </nav>\n"
        ),
        main_markup=sections,
    )


def _render_artifact_page(artifact: GeneratedArtifact, page_title: str, page_kicker: str) -> str:
    section = _render_artifact_section(artifact)
    return _render_page_shell(
        page_title=page_title,
        page_kicker=page_kicker,
        brand_title=page_title,
        subtitle="Standalone export of the Product Guard review.",
        nav_label="Document",
        nav_markup=(
            "      <nav class=\"doc-nav\" aria-label=\"Document navigation\">\n"
            "        <div class=\"panel-eyebrow\">Document</div>\n"
            "        <p><a href=\"index.html\">Foundations</a></p>\n"
            "        <ol class=\"doc-nav-list\">\n"
            f'          <li><a href="#{html.escape(artifact.name)}">{html.escape(_artifact_eyebrow(artifact))}</a></li>\n'
            "        </ol>\n"
            "      </nav>\n"
        ),
        main_markup=section,
    )


def _render_page_shell(
    page_title: str,
    page_kicker: str,
    brand_title: str,
    subtitle: str,
    nav_label: str,
    nav_markup: str,
    main_markup: str,
) -> str:
    return (
        "<!DOCTYPE html>\n"
        "<html lang=\"en\">\n"
        "<head>\n"
        "  <meta charset=\"utf-8\" />\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n"
        f"  <title>{html.escape(page_title)}</title>\n"
        "  <link rel=\"icon\" href=\"logo.png\" />\n"
        "  <link rel=\"stylesheet\" href=\"styles.css\" />\n"
        "</head>\n"
        "<body>\n"
        "  <div class=\"app-shell\">\n"
        "    <header class=\"page-header\">\n"
        "      <div class=\"brand-block\">\n"
        "        <img class=\"brand-logo\" src=\"logo.png\" alt=\"Gentlii logo\" />\n"
        "        <div>\n"
        f"          <div class=\"brand-kicker\">{html.escape(page_kicker)}</div>\n"
        f"          <h1 class=\"brand-title\">{html.escape(brand_title)}</h1>\n"
        f"          <p class=\"brand-subtitle\">{html.escape(subtitle)}</p>\n"
        f"{_render_brand_links()}"
        "        </div>\n"
        "      </div>\n"
        f"{nav_markup}"
        "    </header>\n"
        "    <main class=\"page\">\n"
        f"{main_markup}\n"
        "    </main>\n"
        "  </div>\n"
        "</body>\n"
        "</html>\n"
    )


def _render_brand_links() -> str:
    return (
        "          <div class=\"brand-links\" aria-label=\"Page links\">\n"
        '            <a href="index.html">Foundations</a>\n'
        '            <a href="product-guard.html">Product Guard</a>\n'
        '            <a href="feature-validator.html">Feature Validator</a>\n'
        "          </div>\n"
    )


def _render_artifact_section(artifact: GeneratedArtifact) -> str:
    return (
        f'      <section class="doc-card" id="{html.escape(artifact.name)}">\n'
        f'        <div class="panel-eyebrow">{html.escape(_artifact_eyebrow(artifact))}</div>\n'
        '        <div class="doc-content">\n'
        f"{_indent(_markdown_to_html(artifact.markdown), 10)}\n"
        "        </div>\n"
        "      </section>"
    )


def _artifact_eyebrow(artifact: GeneratedArtifact) -> str:
    return artifact.name.replace("-", " ")


def _artifact_title(artifact: GeneratedArtifact) -> str:
    for line in _strip_frontmatter(artifact.markdown).splitlines():
        stripped = line.strip()
        heading = _parse_heading(stripped)
        if heading is not None:
            return heading
    return artifact.name.replace("-", " ").title()


def _strip_frontmatter(markdown: str) -> str:
    lines = markdown.splitlines()
    if len(lines) >= 3 and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                metadata_lines = lines[1:index]
                if metadata_lines and all(_looks_like_yaml_metadata(line) for line in metadata_lines):
                    return "\n".join(lines[index + 1 :]).lstrip("\n")
                break
    return markdown


def _markdown_to_html(markdown: str) -> str:
    lines = _strip_frontmatter(markdown).splitlines()
    blocks: list[str] = []
    paragraph: list[str] = []
    unordered_list_items: list[str] = []
    ordered_list_items: list[str] = []
    blockquote: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            for text in _normalize_paragraph_lines(paragraph):
                _append_paragraph_blocks(blocks, text)
            paragraph.clear()

    def flush_unordered_list() -> None:
        if unordered_list_items:
            items = "".join(f"<li>{html.escape(item)}</li>" for item in unordered_list_items)
            blocks.append(f"<ul>{items}</ul>")
            unordered_list_items.clear()

    def flush_ordered_list() -> None:
        if ordered_list_items:
            items = "".join(f"<li>{html.escape(item)}</li>" for item in ordered_list_items)
            blocks.append(f"<ol>{items}</ol>")
            ordered_list_items.clear()

    def flush_blockquote() -> None:
        if blockquote:
            text = " ".join(part.strip() for part in blockquote if part.strip())
            blocks.append(f"<blockquote><p>{html.escape(text)}</p></blockquote>")
            blockquote.clear()

    def flush_all() -> None:
        flush_paragraph()
        flush_unordered_list()
        flush_ordered_list()
        flush_blockquote()

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            flush_all()
            continue
        if line == "---":
            flush_all()
            blocks.append("<hr />")
            continue
        heading = _parse_heading(line)
        if heading is not None:
            flush_all()
            level = len(line) - len(line.lstrip("#"))
            blocks.append(f"<h{level}>{html.escape(heading)}</h{level}>")
            continue
        if line.startswith("- "):
            flush_paragraph()
            flush_ordered_list()
            flush_blockquote()
            unordered_list_items.append(line[2:].strip())
            continue
        ordered_list_match = _ORDERED_LIST_PATTERN.match(line)
        if ordered_list_match:
            flush_paragraph()
            flush_unordered_list()
            flush_blockquote()
            ordered_list_items.append(ordered_list_match.group(1).strip())
            continue
        if line.startswith("> "):
            flush_paragraph()
            flush_unordered_list()
            flush_ordered_list()
            blockquote.append(line[2:].strip())
            continue
        flush_unordered_list()
        flush_ordered_list()
        flush_blockquote()
        paragraph.append(line)

    flush_all()
    grouped_blocks = _group_side_by_side_sections(blocks)
    return "\n".join(_move_dual_section_grid_to_top(grouped_blocks))


def _indent(text: str, spaces: int) -> str:
    prefix = " " * spaces
    return "\n".join(f"{prefix}{line}" for line in text.splitlines())


def _append_paragraph_blocks(blocks: list[str], text: str) -> None:
    metric_block = _render_metric_block(text)
    if metric_block is not None:
        blocks.append(metric_block)
        return
    fragments = _split_bold_fragments(text)
    if not fragments:
        return
    if all(kind == "text" for kind, _ in fragments):
        blocks.append(f"<p>{html.escape(text)}</p>")
        return
    for kind, value in fragments:
        stripped = value.strip()
        if not stripped:
            continue
        if kind == "bold":
            blocks.append(f"<h3>{html.escape(stripped)}</h3>")
        else:
            blocks.append(f"<p>{html.escape(stripped)}</p>")


def _normalize_paragraph_lines(lines: list[str]) -> list[str]:
    normalized: list[str] = []
    text_buffer: list[str] = []

    def flush_text_buffer() -> None:
        if text_buffer:
            normalized.append(" ".join(part.strip() for part in text_buffer if part.strip()))
            text_buffer.clear()

    for raw_line in lines:
        stripped = raw_line.strip()
        if not stripped:
            continue
        if _is_metric_text(stripped):
            flush_text_buffer()
            normalized.append(stripped)
            continue
        text_buffer.append(stripped)

    flush_text_buffer()
    return normalized


def _split_bold_fragments(text: str) -> list[tuple[str, str]]:
    fragments: list[tuple[str, str]] = []
    cursor = 0
    for match in _BOLD_PATTERN.finditer(text):
        if match.start() > cursor:
            fragments.append(("text", text[cursor:match.start()]))
        fragments.append(("bold", match.group(1)))
        cursor = match.end()
    if cursor < len(text):
        fragments.append(("text", text[cursor:]))
    if not fragments:
        return [("text", text)]
    return fragments


def _render_metric_block(text: str) -> str | None:
    labeled_metric_match = _LABELED_METRIC_PATTERN.fullmatch(text.strip())
    if labeled_metric_match is not None:
        label = labeled_metric_match.group(1)
        value = labeled_metric_match.group(2).strip()
        if label == "Evidence":
            return (
                '<details class="evidence-accordion">'
                "<summary>Evidence</summary>"
                f'<div class="evidence-body"><p>{html.escape(value)}</p></div>'
                "</details>"
            )
        return (
            '<p class="metric-line">'
            f"<strong>{html.escape(label)}:</strong> "
            f"{_render_metric_value(value)}"
            "</p>"
        )
    stripped = text.strip()
    if _ALIGNMENT_SCORE_PATTERN.fullmatch(stripped) is not None:
        return f'<p class="metric-line">{_render_alignment_score_value(stripped)}</p>'
    if stripped.lower() in _METRIC_VALUE_CLASSES:
        return f'<p class="metric-line">{_render_metric_value(stripped)}</p>'
    return None


def _is_metric_text(text: str) -> bool:
    stripped = text.strip()
    return (
        _LABELED_METRIC_PATTERN.fullmatch(stripped) is not None
        or _ALIGNMENT_SCORE_PATTERN.fullmatch(stripped) is not None
        or stripped.lower() in _METRIC_VALUE_CLASSES
    )


def _render_metric_value(value: str) -> str:
    metric_class = _METRIC_VALUE_CLASSES.get(value.strip().lower())
    if metric_class is None:
        return html.escape(value)
    return f'<span class="metric-value metric-pill {metric_class}">{html.escape(value)}</span>'


def _render_alignment_score_value(value: str) -> str:
    score = value.strip()
    if _ALIGNMENT_SCORE_PATTERN.fullmatch(score) is None:
        return html.escape(score)
    return f'<span class="metric-value metric-pill score-pill score-{score[0]}">{html.escape(score)}</span>'


def _group_side_by_side_sections(blocks: list[str]) -> list[str]:
    grouped: list[str] = []
    index = 0
    while index < len(blocks):
        first_section = _collect_side_section(blocks, index)
        if first_section is None:
            grouped.append(blocks[index])
            index += 1
            continue
        second_section = _collect_side_section(blocks, first_section[1])
        if second_section is None:
            grouped.extend(first_section[0])
            index = first_section[1]
            continue
        first_title = _extract_h3_title(first_section[0][0])
        second_title = _extract_h3_title(second_section[0][0])
        if frozenset({first_title, second_title}) in _SIDE_BY_SIDE_H3_TITLE_PAIRS:
            grouped.append(
                '<div class="doc-dual-section-grid">'
                f'<section class="doc-side-section">{"".join(first_section[0])}</section>'
                f'<section class="doc-side-section">{"".join(second_section[0])}</section>'
                "</div>"
            )
            index = second_section[1]
            continue
        grouped.extend(first_section[0])
        index = first_section[1]
    return grouped


def _move_dual_section_grid_to_top(blocks: list[str]) -> list[str]:
    for index, block in enumerate(blocks):
        if block.startswith('<div class="doc-dual-section-grid">'):
            return [block, *blocks[:index], *blocks[index + 1 :]]
    return blocks


def _collect_side_section(blocks: list[str], start_index: int) -> tuple[list[str], int] | None:
    if start_index >= len(blocks):
        return None
    heading = blocks[start_index]
    title = _extract_h3_title(heading)
    if not any(title in title_pair for title_pair in _SIDE_BY_SIDE_H3_TITLE_PAIRS):
        return None
    end_index = start_index + 1
    section_blocks = [heading]
    while end_index < len(blocks):
        if title in {"Alignment score", "Confidence"} and len(section_blocks) >= 2:
            break
        if _starts_new_side_section(blocks[end_index]):
            break
        section_blocks.append(blocks[end_index])
        end_index += 1
    return section_blocks, end_index


def _extract_h3_title(block: str) -> str | None:
    match = _H3_HEADING_PATTERN.fullmatch(block)
    if match is None:
        return None
    return html.unescape(match.group(1))


def _is_heading_block(block: str) -> bool:
    return block.startswith("<h1>") or block.startswith("<h2>") or block.startswith("<h3>") or block.startswith("<h4>") or block.startswith("<h5>") or block.startswith("<h6>")


def _starts_new_side_section(block: str) -> bool:
    return _is_heading_block(block)


def _sort_artifacts(artifacts: list[GeneratedArtifact]) -> list[GeneratedArtifact]:
    artifact_order = {artifact.value: index for index, artifact in enumerate(ArtifactName)}
    return sorted(artifacts, key=lambda artifact: (artifact_order.get(artifact.name, len(artifact_order)), artifact.name))


def _validate_artifact_names(artifacts: list[GeneratedArtifact]) -> None:
    seen: set[str] = set()
    for artifact in artifacts:
        name = artifact.name
        if not _is_safe_artifact_name(name):
            raise ValueError(f"unsafe artifact name: {name}")
        if name in seen:
            raise ValueError(f"duplicate artifact name: {name}")
        seen.add(name)


def _is_safe_artifact_name(name: str) -> bool:
    if not name or name in {".", ".."}:
        return False
    if "/" in name or "\\" in name:
        return False
    path = Path(name)
    return not path.is_absolute() and path.name == name and bool(_SLUG_SAFE_ARTIFACT_NAME_PATTERN.fullmatch(name))


def _parse_heading(line: str) -> str | None:
    if not line.startswith("#"):
        return None
    level = len(line) - len(line.lstrip("#"))
    if 1 <= level <= 6 and len(line) > level and line[level] == " ":
        return line[level + 1 :].strip()
    return None


def _looks_like_yaml_metadata(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if line[:1].isspace():
        return True
    if stripped.startswith("- "):
        return True
    key, separator, value = stripped.partition(":")
    return bool(separator and key.strip())


def _render_stylesheet() -> str:
    return """
:root {
  --bg: #071423;
  --surface: rgba(8, 28, 46, 0.82);
  --surface-strong: rgba(10, 34, 55, 0.96);
  --text: #f2f7fb;
  --muted: #b7c9d8;
  --accent: #1186b8ff;
  --accent-bright: #e9821f;
  --accent-soft: rgba(17, 134, 184, 0.12);
  --accent-faint: rgba(17, 134, 184, 0.08);
  --border: rgba(125, 175, 205, 0.2);
  --shadow: 0 32px 80px rgba(0, 0, 0, 0.34);
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  min-height: 100vh;
  background: #071423;
  background-image:
    radial-gradient(circle at top, rgba(17, 134, 184, 0.22), transparent 36%),
    linear-gradient(180deg, #0a1a2b 0%, #071423 42%, #08111b 100%);
  color: var(--text);
  font-family: "Söhne", "Inter", "Avenir Next", "Helvetica Neue", "Segoe UI", sans-serif;
  font: 16px/1.6 "Söhne", "Inter", "Avenir Next", "Helvetica Neue", "Segoe UI", sans-serif;
}

a {
  color: var(--accent);
}

.app-shell {
  width: min(1100px, calc(100% - 32px));
  margin: 18px auto 36px;
}

.page-header {
  display: grid;
  grid-template-columns: minmax(0, 1.5fr) minmax(240px, 0.9fr);
  gap: 18px;
  padding: 22px;
  border: 1px solid var(--border);
  border-radius: 20px;
  box-shadow: var(--shadow);
}

.brand-block {
  display: flex;
  gap: 14px;
  align-items: flex-start;
}

.brand-logo {
  width: 44px;
  height: 44px;
  flex: 0 0 44px;
  display: block;
  object-fit: contain;
}

.brand-kicker,
.panel-eyebrow {
  color: var(--accent-bright);
  font-size: 1.35rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.brand-title {
  margin: 2px 0 6px;
  font-size: 1.65rem;
  line-height: 1.05;
  letter-spacing: -0.03em;
  font-weight: 750;
}

.brand-subtitle {
  margin: 0;
  max-width: 54ch;
  color: var(--muted);
  font-size: 0.96rem;
}

.brand-links {
  margin-top: 12px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px 14px;
}

.brand-links a {
  text-decoration: none;
  color: var(--muted);
  font-size: 0.92rem;
  font-weight: 650;
}

.brand-links a:hover,
.brand-links a:focus-visible {
  color: var(--text);
}

.doc-nav {
  padding: 16px 18px;
  border: 1px solid var(--border);
  border-radius: 16px;
  background: rgba(7, 20, 35, 0.32);
  backdrop-filter: blur(18px);
}

.doc-nav-list {
  margin: 10px 0 0;
  padding-left: 18px;
  display: grid;
  gap: 8px;
  color: var(--muted);
}

.doc-nav-list a {
  text-decoration: none;
  color: inherit;
}

.doc-nav-list a:hover,
.doc-nav-list a:focus-visible {
  color: var(--text);
}

.page {
  padding-top: 18px;
  display: grid;
  gap: 14px;
}

.doc-card {
  padding: 20px;
  border: 1px solid var(--border);
  border-radius: 18px;
  background:
    radial-gradient(circle at top, rgba(17, 134, 184, 0.16), transparent 32%),
    radial-gradient(circle at bottom, rgba(17, 134, 184, 0.12), transparent 28%),
    linear-gradient(180deg, var(--surface) 0%, var(--surface-strong) 100%);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.04);
}

.doc-content {
  margin-top: 10px;
}

.doc-dual-section-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
  margin: 0 0 0.82rem;
}

.doc-side-section {
  padding: 14px 16px;
  border: 1px solid var(--border);
  border-radius: 14px;
}

.doc-side-section h3 {
  margin-top: 0;
}

.doc-side-section p:last-child,
.doc-side-section ol:last-child,
.doc-side-section ul:last-child,
.doc-side-section blockquote:last-child {
  margin-bottom: 0;
}

.metric-line {
  margin: 0 0 0.82rem;
}

.score-callout {
  display: inline-flex;
  align-items: baseline;
  gap: 0.75rem;
  margin: 0 0 0.95rem;
  padding: 0.85rem 1rem;
  border: 1px solid rgba(17, 134, 184, 0.32);
  border-radius: 16px;
  background: linear-gradient(135deg, rgba(17, 134, 184, 0.16), rgba(233, 130, 31, 0.12));
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05);
}

.score-label {
  color: var(--muted);
  font-size: 0.9rem;
  font-weight: 650;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.score-value {
  font-size: 1.8rem;
  line-height: 1;
  font-weight: 780;
  letter-spacing: -0.04em;
}

.score-1,
.score-2 {
  color: #e06464;
}

.score-3 {
  color: #f0a94b;
}

.score-4,
.score-5 {
  color: #57c084;
}

.evidence-accordion {
  margin: 0 0 0.82rem;
  border: 1px solid var(--border);
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.03);
  overflow: hidden;
}

.evidence-accordion summary {
  cursor: pointer;
  list-style: none;
  padding: 0.78rem 0.95rem;
  font-weight: 650;
  color: var(--text);
}

.evidence-accordion summary::-webkit-details-marker {
  display: none;
}

.evidence-accordion summary::after {
  content: "+";
  float: right;
  color: var(--accent);
  font-weight: 700;
}

.evidence-accordion[open] summary::after {
  content: "−";
}

.evidence-body {
  padding: 0 0.95rem 0.82rem;
}

.evidence-body p:last-child {
  margin-bottom: 0;
}

.metric-value {
  font-weight: 700;
}

.metric-pill {
  display: inline-flex;
  align-items: center;
  padding: 0.18rem 0.55rem;
  border-radius: 999px;
  border: 1px solid transparent;
  line-height: 1.1;
}

.metric-high {
  color: #57c084;
  background: rgba(87, 192, 132, 0.14);
  border-color: rgba(87, 192, 132, 0.28);
}

.metric-medium {
  color: #f0a94b;
  background: rgba(240, 169, 75, 0.14);
  border-color: rgba(240, 169, 75, 0.28);
}

.metric-low {
  color: #e06464;
  background: rgba(224, 100, 100, 0.14);
  border-color: rgba(224, 100, 100, 0.28);
}

.doc-content h1,
.doc-content h2,
.doc-content h3,
.doc-content h4,
.doc-content h5,
.doc-content h6 {
  margin: 1.15em 0 0.45em;
  line-height: 1.18;
  letter-spacing: -0.03em;
  font-weight: 720;
}

.doc-content h1 {
  font-size: 1.85rem;
  color: var(--accent-bright);
}

.doc-content h2 {
  font-size: 1.45rem;
}

.doc-content h3,
.doc-content h4,
.doc-content h5,
.doc-content h6 {
  font-size: 1.25rem;
  color: var(--accent);
}

.doc-content h1:first-child,
.doc-content h2:first-child,
.doc-content h3:first-child {
  margin-top: 0;
}

.doc-content p,
.doc-content ol,
.doc-content ul,
.doc-content blockquote {
  margin: 0 0 0.82rem;
}

.doc-content p {
  color: var(--text);
}

.doc-content ol,
.doc-content ul {
  padding-left: 1.2rem;
  color: var(--muted);
}

.doc-content li + li {
  margin-top: 0.28rem;
}

.doc-content blockquote {
  padding: 0.05rem 0 0.05rem 0.9rem;
  border-left: 3px solid var(--accent);
  color: var(--text);
  background: transparent;
}

.doc-content hr {
  border: 0;
  border-top: 1px solid var(--border);
  margin: 1.2rem 0;
}

@media (max-width: 860px) {
  .page-header {
    grid-template-columns: 1fr;
  }

  .app-shell {
    width: min(100% - 20px, 1100px);
    margin-top: 10px;
  }

  .doc-dual-section-grid {
    grid-template-columns: 1fr;
  }
}
""".lstrip()
