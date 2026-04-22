from __future__ import annotations

from pathlib import Path
import argparse
import re


class UnsafeHtmlError(ValueError):
    pass


_DISALLOWED_PATTERNS = (
    re.compile(r"<script\b", re.IGNORECASE),
    re.compile(r"\bjavascript:", re.IGNORECASE),
    re.compile(r"\bon[a-z]+\s*=", re.IGNORECASE),
    re.compile(r"<iframe\b", re.IGNORECASE),
    re.compile(r"<object\b", re.IGNORECASE),
    re.compile(r"<embed\b", re.IGNORECASE),
)


def assert_safe_publish_html(html: str) -> None:
    violations: list[str] = []
    for pattern in _DISALLOWED_PATTERNS:
        match = pattern.search(html)
        if match is not None:
            violations.append(match.group(0).lower())
    if violations:
        joined = ", ".join(dict.fromkeys(violations))
        raise UnsafeHtmlError(f"unsafe HTML patterns detected: {joined}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m gentlii_foundations.html_security")
    parser.add_argument("html_path", type=Path)
    args = parser.parse_args(argv)

    assert_safe_publish_html(args.html_path.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
