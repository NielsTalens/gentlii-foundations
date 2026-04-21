# Product Description Pages Design

**Context:** `gentlii-foundations` currently writes structured markdown artifacts into `product-definitions/product-description/`. The next step is to publish that output as GitHub Pages HTML while keeping the styling aligned with the Gentlii application UI in the sibling `../gentlii` project rather than the separate marketing site.

## Goal

Generate a single static `index.html` from the markdown files in `product-definitions/product-description/`, styled to match the Gentlii app experience and suitable for publication via GitHub Pages.

## Source Of Truth For Styling

- Use the Gentlii application styling from:
  - `../gentlii/views/index.erb`
  - `../gentlii/public/styles.css`
- Do not use `../gentlii-website/index.html` as the primary styling reference for this feature.

## Why The App Styling

- The app styling is already optimized for reading structured, panel-based content rather than marketing sections.
- The styles live in a reusable CSS file, which is easier to copy or adapt into a static export than large inline CSS embedded in a single HTML file.
- The visual language aligns better with long-form product-definition artifacts.

## Output Structure

The generated site should live alongside the markdown artifacts in `product-definitions/product-description/`:

- `index.html`
- `styles.css`
- existing generated `*.md` files
- optional static assets copied locally only if required by the layout, for example `logo.png`

The markdown files remain the primary generated artifacts. The HTML and CSS are derived output generated from those files.

## Page Structure

The HTML export should be a single long-form page with these sections:

1. Gentlii-branded header based on the app shell
2. Intro block that identifies the page as a product definition export
3. Compact in-page navigation listing each artifact section
4. One content panel per markdown file

The page should not copy the two-panel interactive evaluator layout from the app. It should reuse the app's visual language while adapting the structure for document reading.

## Content Rendering

- Read all `.md` files from `product-definitions/product-description/`
- Sort them predictably, preferably lexicographically by filename so numbered files remain stable
- Convert markdown to HTML
- Derive a section title from the first markdown heading when present, otherwise from the filename
- Generate stable section anchors for in-page navigation
- Render each artifact as a separate content card/panel

## Styling Approach

- Start from the Gentlii app stylesheet in `../gentlii/public/styles.css`
- Reuse the same visual tokens where practical:
  - background gradients
  - typography
  - border and panel colors
  - spacing rhythm
  - rounded surfaces
  - responsive behavior
- Add only the minimum extra rules needed for:
  - markdown content
  - in-page table of contents
  - long-form reading layout

This should be an adaptation, not a redesign.

## Publishing Approach

- Do not place the generated `index.html` at repository root by default
- Keep generated site files in `product-definitions/product-description/`
- Publish that folder via a GitHub Pages workflow artifact

This keeps generated output near the markdown source, avoids root clutter, and keeps regeneration deterministic.

## Testing

Tests should cover:

- `index.html` generation
- `styles.css` generation
- presence of expected anchors and titles
- markdown-to-HTML conversion for representative headings, paragraphs, and lists
- operation when only a subset of markdown artifacts exists

## Risks And Constraints

- The sibling `../gentlii` repo is outside this project, so styling reuse should not depend on runtime access to that repo after generation.
- If the Gentlii app stylesheet changes later, this project will not automatically inherit those changes unless the copied or derived stylesheet is refreshed.
- The implementation should avoid introducing a heavy static-site toolchain unless there is a clear need.
