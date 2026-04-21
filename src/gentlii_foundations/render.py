from __future__ import annotations

import html
import re
from pathlib import Path

from gentlii_foundations.models import GeneratedArtifact

_ORDERED_LIST_PATTERN = re.compile(r"^\d+\. (.+)$")
_SLUG_SAFE_ARTIFACT_NAME_PATTERN = re.compile(r"^[a-z0-9-]+$")


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
            blocks.append(f"<p>{html.escape(text)}</p>")
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


def _sort_artifacts(artifacts: list[GeneratedArtifact]) -> list[GeneratedArtifact]:
    return sorted(artifacts, key=lambda artifact: artifact.name)


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
@import url("https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;500;600&family=Source+Serif+4:wght@500;600&display=swap");

:root {
  --bg: #071423;
  --bg-glow: #11294a;
  --text: rgba(255, 255, 255, 0.92);
  --muted: rgba(222, 233, 250, 0.72);
  --panel: rgba(10, 27, 49, 0.82);
  --panel-2: #13335d;
  --border: rgba(173, 201, 240, 0.16);
  --accent: #89b2f2;
  --accent-strong: #d0e0ff;
  --shadow: 0 22px 60px rgba(0, 0, 0, 0.28);
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
  background:
    radial-gradient(circle at top left, rgba(88, 154, 255, 0.18), transparent 28%),
    radial-gradient(circle at top right, rgba(255, 128, 0, 0.12), transparent 24%),
    linear-gradient(180deg, var(--bg-glow) 0%, var(--bg) 22%, #050d18 100%);
  color: var(--text);
  font: 17px/1.6 "Source Sans 3", "Segoe UI", sans-serif;
}

a {
  color: var(--accent-strong);
}

.app-shell {
  width: min(1180px, calc(100% - 32px));
  margin: 24px auto 48px;
}

.page-header {
  display: grid;
  grid-template-columns: minmax(0, 1.5fr) minmax(260px, 0.9fr);
  gap: 24px;
  padding: 28px;
  border: 1px solid var(--border);
  border-radius: 24px;
  background: linear-gradient(180deg, rgba(17, 40, 71, 0.95), rgba(10, 27, 49, 0.88));
  box-shadow: var(--shadow);
}

.brand-block {
  display: flex;
  gap: 18px;
  align-items: flex-start;
}

.brand-mark {
  width: 52px;
  height: 52px;
  flex: 0 0 52px;
  display: grid;
  place-items: center;
  border-radius: 16px;
  background: linear-gradient(135deg, #8ab5ff, #6b95e6);
  color: #071423;
  font-weight: 700;
  font-size: 1.35rem;
}

.brand-kicker,
.panel-eyebrow {
  color: var(--muted);
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.4px;
}

.brand-title {
  margin: 2px 0 8px;
  font: 600 2.15rem/1.1 "Source Serif 4", "Times New Roman", serif;
}

.brand-subtitle {
  margin: 0;
  max-width: 46ch;
  color: var(--muted);
}

.doc-nav {
  padding: 18px 20px;
  border: 1px solid var(--border);
  border-radius: 18px;
  background: var(--panel);
}

.doc-nav-list {
  margin: 12px 0 0;
  padding-left: 18px;
  display: grid;
  gap: 10px;
}

.doc-nav-list a {
  text-decoration: none;
}

.page {
  padding-top: 24px;
  display: grid;
  gap: 18px;
}

.doc-card {
  padding: 24px;
  border: 1px solid var(--border);
  border-radius: 22px;
  background: var(--panel);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.04);
}

.doc-content {
  margin-top: 12px;
}

.doc-content h1,
.doc-content h2,
.doc-content h3,
.doc-content h4,
.doc-content h5,
.doc-content h6 {
  margin: 1.2em 0 0.45em;
  font-family: "Source Serif 4", "Times New Roman", serif;
  font-weight: 600;
  letter-spacing: 0.2px;
}

.doc-content h1:first-child,
.doc-content h2:first-child,
.doc-content h3:first-child {
  margin-top: 0;
}

.doc-content p,
.doc-content ul,
.doc-content blockquote {
  margin: 0 0 1rem;
}

.doc-content ul {
  padding-left: 1.4rem;
}

.doc-content li + li {
  margin-top: 0.35rem;
}

.doc-content blockquote {
  padding: 0.2rem 0 0.2rem 1rem;
  border-left: 3px solid rgba(137, 178, 242, 0.5);
  color: var(--accent-strong);
}

.doc-content hr {
  border: 0;
  border-top: 1px solid var(--border);
  margin: 1.5rem 0;
}

@media (max-width: 860px) {
  .page-header {
    grid-template-columns: 1fr;
  }

  .app-shell {
    width: min(100% - 24px, 1180px);
    margin-top: 12px;
  }
}
""".lstrip()
