from gentlii_foundations.models import GeneratedArtifact
from gentlii_foundations.render import write_artifact_page, write_artifacts


def test_write_artifacts_creates_expected_markdown_files(tmp_path):
    artifact = GeneratedArtifact(name="strategy", markdown="# Strategy\n")
    write_artifacts(tmp_path, [artifact])
    assert (tmp_path / "strategy.md").read_text() == "# Strategy\n"


def test_write_artifact_page_creates_standalone_product_guard_html(tmp_path):
    artifact = GeneratedArtifact(
        name="product-guard",
        markdown="# Product Guard\n\n## Strategy <-> Business Case\n\nAligned.\n",
    )

    write_artifact_page(tmp_path / "product-guard.html", artifact, page_title="Product Guard", page_kicker="Product Guard")

    html = (tmp_path / "product-guard.html").read_text(encoding="utf-8")

    assert "<title>Product Guard</title>" in html
    assert "<h1 class=\"brand-title\">Product Guard</h1>" in html
    assert "<div class=\"brand-kicker\">Product Guard</div>" in html
    assert "<h1>Product Guard</h1>" in html
    assert "<h2>Strategy &lt;-&gt; Business Case</h2>" in html
    assert "<p>Aligned.</p>" in html
    assert '<link rel="stylesheet" href="styles.css" />' in html
    assert 'href="index.html"' in html
    assert 'href="product-guard.html"' in html
    assert 'href="feature-validator.html"' in html


def test_write_artifact_page_refreshes_existing_stylesheet(tmp_path):
    (tmp_path / "styles.css").write_text("body { color: hotpink; }\n", encoding="utf-8")
    artifact = GeneratedArtifact(name="product-guard", markdown="# Product Guard\n\n### Alignment score\n\n4/5\n")

    write_artifact_page(tmp_path / "product-guard.html", artifact, page_title="Product Guard", page_kicker="Product Guard")

    css = (tmp_path / "styles.css").read_text(encoding="utf-8")

    assert ".doc-dual-section-grid" in css
    assert ".doc-side-section" in css
    assert "hotpink" not in css


def test_write_artifacts_creates_static_site_files(tmp_path):
    artifacts = [
        GeneratedArtifact(name="strategy", markdown="# Strategy\n\nBody text.\n"),
        GeneratedArtifact(name="product-charter", markdown="# Product Charter\n\n- First\n- Second\n"),
    ]

    write_artifacts(tmp_path, artifacts)

    assert (tmp_path / "strategy.md").exists()
    assert (tmp_path / "product-charter.md").exists()
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
    assert 'href="index.html"' in html
    assert 'href="product-guard.html"' in html
    assert 'href="feature-validator.html"' in html


def test_write_artifacts_uses_logo_png_for_favicon_and_brand_logo(tmp_path):
    write_artifacts(tmp_path, [GeneratedArtifact(name="strategy", markdown="# Strategy\n")])
    html = (tmp_path / "index.html").read_text(encoding="utf-8")

    assert '<link rel="icon" href="logo.png" />' in html
    assert '<img class="brand-logo" src="logo.png" alt="Gentlii logo" />' in html


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


def test_write_artifacts_places_completeness_and_strength_side_by_side(tmp_path):
    artifact = GeneratedArtifact(
        name="strategy",
        markdown=(
            "# Strategy\n\n"
            "## Company Strategy\n\n"
            "Defined.\n\n"
            "### Completeness\n\n"
            "Complete\n\n"
            "### Strength\n\n"
            "Medium\n"
        ),
    )

    write_artifacts(tmp_path, [artifact])
    html = (tmp_path / "index.html").read_text(encoding="utf-8")
    css = (tmp_path / "styles.css").read_text(encoding="utf-8")

    assert '<div class="doc-dual-section-grid">' in html
    assert '<section class="doc-side-section"><h3 class="metric-heading">Completeness: <span class="metric-value metric-pill metric-high">Complete</span></h3></section>' in html
    assert '<section class="doc-side-section"><h3 class="metric-heading">Strength: <span class="metric-value metric-pill metric-medium">Medium</span></h3></section>' in html
    assert ".doc-dual-section-grid" in css
    assert ".doc-side-section" in css


def test_write_artifacts_colorizes_metric_values(tmp_path):
    artifact = GeneratedArtifact(
        name="strategy",
        markdown=(
            "# Strategy\n\n"
            "## Company Strategy\n\n"
            "Defined.\n\n"
            "### Confidence\n\n"
            "Low\n\n"
            "### Completeness\n\n"
            "Complete\n\n"
            "### Strength\n\n"
            "Medium\n"
        ),
    )

    write_artifacts(tmp_path, [artifact])
    html = (tmp_path / "index.html").read_text(encoding="utf-8")
    css = (tmp_path / "styles.css").read_text(encoding="utf-8")

    assert '<span class="metric-value metric-pill metric-high">Complete</span>' in html
    assert '<span class="metric-value metric-pill metric-medium">Medium</span>' in html
    assert '<h3 class="metric-heading">Confidence: <span class="metric-value metric-pill metric-low">Low</span></h3>' in html
    assert ".metric-value" in css
    assert ".metric-pill" in css
    assert ".metric-high" in css
    assert ".metric-medium" in css
    assert ".metric-low" in css


def test_write_artifact_page_colorizes_feature_validator_decision_as_metric_pill(tmp_path):
    artifact = GeneratedArtifact(
        name="feature-validator",
        markdown=(
            "# Feature Validator\n\n"
            "### Decision\n\n"
            "Approve\n\n"
            "### Alignment score\n\n"
            "4/5\n\n"
            "### Confidence\n\n"
            "Medium\n"
        ),
    )

    write_artifact_page(
        tmp_path / "feature-validator.html",
        artifact,
        page_title="Feature Validator",
        page_kicker="Feature Validator",
    )
    html = (tmp_path / "feature-validator.html").read_text(encoding="utf-8")

    assert '<h3 class="metric-heading">Decision: <span class="metric-value metric-pill metric-high">Approve</span></h3>' in html


def test_write_artifact_page_places_alignment_score_and_confidence_side_by_side(tmp_path):
    artifact = GeneratedArtifact(
        name="product-guard",
        markdown=(
            "# Product Guard\n\n"
            "## Strategy <-> Business Case\n\n"
            "Aligned.\n\n"
            "### Alignment score\n\n"
            "4/5\n\n"
            "### Confidence\n\n"
            "High\n\n"
            "**Evidence:** Explicit support from source.\n"
        ),
    )

    write_artifact_page(tmp_path / "product-guard.html", artifact, page_title="Product Guard", page_kicker="Product Guard")
    html = (tmp_path / "product-guard.html").read_text(encoding="utf-8")
    css = (tmp_path / "styles.css").read_text(encoding="utf-8") if (tmp_path / "styles.css").exists() else ""

    assert '<div class="doc-dual-section-grid">' in html
    assert '<section class="doc-side-section"><h3 class="metric-heading">Alignment score: <span class="metric-value metric-pill score-pill score-4">4/5</span></h3></section>' in html
    assert '<section class="doc-side-section"><h3 class="metric-heading">Confidence: <span class="metric-value metric-pill metric-high">High</span></h3>' in html
    assert '<details class="evidence-accordion"><summary>Evidence</summary>' in html
    assert ".doc-dual-section-grid" in css


def test_write_artifacts_keeps_confidence_and_evidence_separate_without_blank_lines(tmp_path):
    artifact = GeneratedArtifact(
        name="strategy",
        markdown=(
            "# Strategy\n\n"
            "## Company Strategy\n"
            "Defined.\n"
            "### Confidence\n"
            "High\n"
            "**Evidence:** Explicit support from source.\n"
        ),
    )

    write_artifacts(tmp_path, [artifact])
    html = (tmp_path / "index.html").read_text(encoding="utf-8")
    css = (tmp_path / "styles.css").read_text(encoding="utf-8")

    assert '<h3 class="metric-heading">Confidence: <span class="metric-value metric-pill metric-high">High</span></h3>' in html
    assert '<details class="evidence-accordion"><summary>Evidence</summary><div class="evidence-body"><p>Explicit support from source.</p></div></details>' in html
    assert '<h3 class="metric-heading">Confidence: <span class="metric-value metric-pill metric-high">High</span></h3>**Evidence:**' not in html
    assert ".evidence-accordion" in css
    assert ".evidence-body" in css


def test_write_artifacts_keeps_suggestion_below_side_by_side_blocks(tmp_path):
    artifact = GeneratedArtifact(
        name="strategy",
        markdown=(
            "# Strategy\n\n"
            "### Completeness\n\n"
            "Complete\n\n"
            "### Strength\n\n"
            "Medium\n\n"
            "## Suggestion\n\n"
            "Clarify the strategic trade-offs in a short paragraph.\n"
        ),
    )

    write_artifacts(tmp_path, [artifact])
    html = (tmp_path / "index.html").read_text(encoding="utf-8")

    assert '<div class="doc-dual-section-grid">' in html
    assert '<section class="doc-side-section"><h3 class="metric-heading">Completeness: <span class="metric-value metric-pill metric-high">Complete</span></h3></section>' in html
    assert '<section class="doc-side-section"><h3 class="metric-heading">Strength: <span class="metric-value metric-pill metric-medium">Medium</span></h3></section>' in html
    assert "<h2>Suggestion</h2>" in html
    assert "<p>Clarify the strategic trade-offs in a short paragraph.</p>" in html
    assert html.index('<div class="doc-dual-section-grid">') < html.index("<h2>Suggestion</h2>")


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
        GeneratedArtifact(name="product-charter", markdown="# Product Charter\n"),
        GeneratedArtifact(name="strategy", markdown="# Strategy\n"),
        GeneratedArtifact(name="product-vision", markdown="# Product Vision\n"),
        GeneratedArtifact(name="business-case", markdown="# Business Case\n"),
    ]

    write_artifacts(tmp_path, artifacts)
    html = (tmp_path / "index.html").read_text(encoding="utf-8")

    assert 'href="#strategy">strategy</a>' in html
    assert 'href="#business-case">business case</a>' in html
    assert 'href="#product-vision">product vision</a>' in html
    assert 'href="#product-charter">product charter</a>' in html

    nav_order = [
        html.index('href="#strategy"'),
        html.index('href="#business-case"'),
        html.index('href="#product-vision"'),
        html.index('href="#product-charter"'),
    ]
    section_order = [
        html.index('<section class="doc-card" id="strategy">'),
        html.index('<section class="doc-card" id="business-case">'),
        html.index('<section class="doc-card" id="product-vision">'),
        html.index('<section class="doc-card" id="product-charter">'),
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

    assert 'href="#customer-research">customer research</a>' in html
    assert "<h3>Deep Dive</h3>" in html


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
        GeneratedArtifact(name="product-charter", markdown="# Product Charter\n"),
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
