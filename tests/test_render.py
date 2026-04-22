from gentlii_foundations.models import GeneratedArtifact
from gentlii_foundations.render import write_artifacts


def test_write_artifacts_creates_expected_markdown_files(tmp_path):
    artifact = GeneratedArtifact(name="strategy", markdown="# Strategy\n")
    write_artifacts(tmp_path, [artifact])
    assert (tmp_path / "strategy.md").read_text() == "# Strategy\n"


def test_write_artifacts_creates_static_site_files(tmp_path):
    artifacts = [
        GeneratedArtifact(name="strategy", markdown="# Strategy\n\nBody text.\n"),
        GeneratedArtifact(name="jtbd", markdown="# JTBD\n\n- First\n- Second\n"),
    ]

    write_artifacts(tmp_path, artifacts)

    assert (tmp_path / "strategy.md").exists()
    assert (tmp_path / "jtbd.md").exists()
    assert (tmp_path / "index.html").exists()
    assert (tmp_path / "styles.css").exists()


def test_write_artifacts_renders_combined_html_content(tmp_path):
    artifact = GeneratedArtifact(
        name="product-vision",
        markdown=(
            "---\n"
            "title: Product Vision\n"
            "---\n\n"
            "# Product Vision\n\n"
            "Intro paragraph.\n\n"
            "> Strong point of view.\n\n"
            "## Focus Areas\n\n"
            "- One\n"
            "- Two\n\n"
            "---\n\n"
            "Closing paragraph.\n"
        ),
    )

    write_artifacts(tmp_path, [artifact])
    html = (tmp_path / "index.html").read_text(encoding="utf-8")

    assert "Gentlii Foundations" in html
    assert "href=\"#product-vision\"" in html
    assert "<section class=\"doc-card\" id=\"product-vision\">" in html
    assert "<h1>Product Vision</h1>" in html
    assert "<h2>Focus Areas</h2>" in html
    assert "<p>Intro paragraph.</p>" in html
    assert "<blockquote><p>Strong point of view.</p></blockquote>" in html
    assert "<li>One</li>" in html
    assert "<li>Two</li>" in html
    assert "<hr />" in html
    assert "title: Product Vision" not in html


def test_write_artifacts_renders_ordered_lists(tmp_path):
    artifact = GeneratedArtifact(
        name="launch-plan",
        markdown="# Launch Plan\n\n1. Align messaging\n2. Review rollout\n",
    )

    write_artifacts(tmp_path, [artifact])
    html = (tmp_path / "index.html").read_text(encoding="utf-8")

    assert "<ol><li>Align messaging</li><li>Review rollout</li></ol>" in html


def test_write_artifacts_promotes_inline_bold_text_to_h3_blocks(tmp_path):
    artifact = GeneratedArtifact(
        name="product-charter",
        markdown="# Product Charter\n\nIntro **Principles** more text.\n",
    )

    write_artifacts(tmp_path, [artifact])
    html = (tmp_path / "index.html").read_text(encoding="utf-8")

    assert "<p>Intro</p>" in html
    assert "<h3>Principles</h3>" in html
    assert "<p>more text.</p>" in html


def test_write_artifacts_generates_gentlii_based_stylesheet(tmp_path):
    write_artifacts(tmp_path, [GeneratedArtifact(name="strategy", markdown="# Strategy\n")])
    css = (tmp_path / "styles.css").read_text(encoding="utf-8")

    assert 'font-family: "Söhne", "Inter", "Avenir Next", "Helvetica Neue", "Segoe UI", sans-serif;' in css
    assert "--surface:" in css
    assert "--accent: #1186b8ff;" in css
    assert ".app-shell" in css
    assert ".page-header" in css
    assert ".brand-block" in css
    assert ".doc-nav" in css
    assert ".doc-nav-list" in css
    assert ".doc-card" in css
    assert ".doc-content" in css
    assert 'font: 16px/1.6 "Söhne", "Inter", "Avenir Next", "Helvetica Neue", "Segoe UI", sans-serif;' in css


def test_write_artifacts_orders_combined_export_deterministically(tmp_path):
    artifacts = [
        GeneratedArtifact(name="zeta", markdown="# Zeta\n"),
        GeneratedArtifact(name="alpha", markdown="# Alpha\n"),
        GeneratedArtifact(name="middle", markdown="# Middle\n"),
    ]

    write_artifacts(tmp_path, artifacts)
    html = (tmp_path / "index.html").read_text(encoding="utf-8")

    nav_order = [
        html.index('href="#alpha"'),
        html.index('href="#middle"'),
        html.index('href="#zeta"'),
    ]
    section_order = [
        html.index('<section class="doc-card" id="alpha">'),
        html.index('<section class="doc-card" id="middle">'),
        html.index('<section class="doc-card" id="zeta">'),
    ]

    assert nav_order == sorted(nav_order)
    assert section_order == sorted(section_order)


def test_write_artifacts_only_strips_yaml_like_frontmatter(tmp_path):
    artifact = GeneratedArtifact(
        name="notes",
        markdown="---\nLead with a thematic break.\n---\n\nParagraph after rule.\n",
    )

    write_artifacts(tmp_path, [artifact])
    html = (tmp_path / "index.html").read_text(encoding="utf-8")

    assert "<hr />" in html
    assert "<p>Lead with a thematic break.</p>" in html
    assert "<p>Paragraph after rule.</p>" in html


def test_write_artifacts_uses_first_heading_at_any_level_for_titles(tmp_path):
    artifact = GeneratedArtifact(
        name="customer-research",
        markdown="Intro without heading.\n\n### Deep Dive\n\nBody text.\n",
    )

    write_artifacts(tmp_path, [artifact])
    html = (tmp_path / "index.html").read_text(encoding="utf-8")

    assert 'href="#customer-research">Deep Dive</a>' in html


def test_write_artifacts_rejects_unsafe_names(tmp_path):
    artifact = GeneratedArtifact(name="../escape", markdown="# Escape\n")

    try:
        write_artifacts(tmp_path, [artifact])
    except ValueError as exc:
        assert "unsafe artifact name" in str(exc)
    else:
        raise AssertionError("Expected unsafe artifact name to be rejected")


def test_write_artifacts_accepts_slug_safe_names(tmp_path):
    artifacts = [
        GeneratedArtifact(name="strategy-2026", markdown="# Strategy\n"),
        GeneratedArtifact(name="jtbd", markdown="# JTBD\n"),
    ]

    write_artifacts(tmp_path, artifacts)

    assert (tmp_path / "strategy-2026.md").exists()
    html = (tmp_path / "index.html").read_text(encoding="utf-8")
    assert 'href="#strategy-2026"' in html


def test_write_artifacts_rejects_duplicate_names(tmp_path):
    artifacts = [
        GeneratedArtifact(name="strategy", markdown="# Strategy\n"),
        GeneratedArtifact(name="strategy", markdown="# Strategy Copy\n"),
    ]

    try:
        write_artifacts(tmp_path, artifacts)
    except ValueError as exc:
        assert "duplicate artifact name" in str(exc)
    else:
        raise AssertionError("Expected duplicate artifact name to be rejected")


def test_write_artifacts_rejects_names_outside_slug_safe_set(tmp_path):
    for name in ["Strategy", "customer research", "customer_research", "roadmap!"]:
        try:
            write_artifacts(tmp_path, [GeneratedArtifact(name=name, markdown="# Invalid\n")])
        except ValueError as exc:
            assert "unsafe artifact name" in str(exc)
        else:
            raise AssertionError(f"Expected {name!r} to be rejected")


def test_write_artifacts_strips_multiline_yaml_frontmatter(tmp_path):
    artifact = GeneratedArtifact(
        name="roadmap",
        markdown=(
            "---\n"
            "title:\n"
            "tags:\n"
            "  - alpha\n"
            "  - beta\n"
            "summary: Ready for review\n"
            "---\n\n"
            "## Roadmap\n\n"
            "Body text.\n"
        ),
    )

    write_artifacts(tmp_path, [artifact])
    html = (tmp_path / "index.html").read_text(encoding="utf-8")

    assert "<h2>Roadmap</h2>" in html
    assert "<p>Body text.</p>" in html
    assert "summary: Ready for review" not in html
    assert "<li>alpha</li>" not in html
