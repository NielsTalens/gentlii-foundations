from __future__ import annotations

import html
import re
from pathlib import Path

from gentlii_foundations.models import ArtifactName, GeneratedArtifact

_ORDERED_LIST_PATTERN = re.compile(r"^\d+\. (.+)$")
_SLUG_SAFE_ARTIFACT_NAME_PATTERN = re.compile(r"^[a-z0-9-]+$")
_BOLD_PATTERN = re.compile(r"\*\*(.+?)\*\*")


def write_artifacts(output_dir: Path, artifacts: list[GeneratedArtifact]) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    _validate_artifact_names(artifacts)
    for artifact in artifacts:
        (output_path / f"{artifact.name}.md").write_text(artifact.markdown, encoding="utf-8")
    (output_path / "index.html").write_text(_render_index_html(_sort_artifacts(artifacts)), encoding="utf-8")
    (output_path / "styles.css").write_text(_render_stylesheet(), encoding="utf-8")


def _render_index_html(artifacts: list[GeneratedArtifact]) -> str:
    nav_items = "\n".join(
        f'          <li><a href="#{html.escape(artifact.name)}">{html.escape(_artifact_title(artifact))}</a></li>'
        for artifact in artifacts
    )
    sections = "\n".join(_render_artifact_section(artifact) for artifact in artifacts)
    return (
        "<!DOCTYPE html>\n"
        "<html lang=\"en\">\n"
        "<head>\n"
        "  <meta charset=\"utf-8\" />\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n"
        "  <title>Gentlii Foundations</title>\n"
        "  <link rel=\"stylesheet\" href=\"styles.css\" />\n"
        "</head>\n"
        "<body>\n"
        "  <div class=\"app-shell\">\n"
        "    <header class=\"page-header\">\n"
        "      <div class=\"brand-block\">\n"
        "        <div class=\"brand-mark\" aria-hidden=\"true\">G</div>\n"
        "        <div>\n"
        "          <div class=\"brand-kicker\">Product Foundations</div>\n"
        "          <h1 class=\"brand-title\">Gentlii Foundations</h1>\n"
        "          <p class=\"brand-subtitle\">Static export of product description artifacts for review and publishing.</p>\n"
        "        </div>\n"
        "      </div>\n"
        "      <nav class=\"doc-nav\" aria-label=\"Artifact navigation\">\n"
        "        <div class=\"panel-eyebrow\">Artifacts</div>\n"
        "        <ol class=\"doc-nav-list\">\n"
        f"{nav_items}\n"
        "        </ol>\n"
        "      </nav>\n"
        "    </header>\n"
        "    <main class=\"page\">\n"
        f"{sections}\n"
        "    </main>\n"
        "  </div>\n"
        "</body>\n"
        "</html>\n"
    )


def _render_artifact_section(artifact: GeneratedArtifact) -> str:
    return (
        f'      <section class="doc-card" id="{html.escape(artifact.name)}">\n'
        f'        <div class="panel-eyebrow">{html.escape(artifact.name.replace("-", " "))}</div>\n'
        '        <div class="doc-content">\n'
        f"{_indent(_markdown_to_html(artifact.markdown), 10)}\n"
        "        </div>\n"
        "      </section>"
    )


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
            text = " ".join(part.strip() for part in paragraph if part.strip())
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
    return "\n".join(blocks)


def _indent(text: str, spaces: int) -> str:
    prefix = " " * spaces
    return "\n".join(f"{prefix}{line}" for line in text.splitlines())


def _append_paragraph_blocks(blocks: list[str], text: str) -> None:
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

.brand-mark {
  width: 44px;
  height: 44px;
  flex: 0 0 44px;
  display: grid;
  place-items: center;
  border-radius: 14px;
  background: linear-gradient(135deg, rgba(17, 134, 184, 0.92), rgba(15, 111, 153, 0.92));
  color: var(--text);
  font-weight: 700;
  font-size: 1.05rem;
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
  font-size: 1.5rem;
}

.doc-content h2 {
  font-size: 1.25rem;
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
}
""".lstrip()
