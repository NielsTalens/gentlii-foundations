from __future__ import annotations

from pathlib import Path
import argparse

from gentlii_foundations.pipeline import build_foundations


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="gentlii-foundations")
    subparsers = parser.add_subparsers(dest="command")

    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("root", type=Path)

    args = parser.parse_args(argv)

    if args.command == "build":
        build_foundations(args.root, report=print)
        return 0

    parser.print_help()
    return 1
