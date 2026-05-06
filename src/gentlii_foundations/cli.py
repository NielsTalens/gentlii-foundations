from __future__ import annotations

import argparse
from pathlib import Path

from gentlii_foundations import pipeline
from gentlii_foundations.pipeline import build_foundations, run_product_guard


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="gentlii-foundations")
    subparsers = parser.add_subparsers(dest="command")

    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("root", type=Path)
    guard_parser = subparsers.add_parser("guard")
    guard_parser.add_argument("root", type=Path)
    feature_validate_parser = subparsers.add_parser("feature-validate")
    feature_validate_parser.add_argument("root", type=Path)
    feature_validate_parser.add_argument("feature_request_file", type=Path)

    args = parser.parse_args(argv)

    if args.command == "build":
        build_foundations(args.root, report=print)
        return 0
    if args.command == "guard":
        run_product_guard(args.root, report=print)
        return 0
    if args.command == "feature-validate":
        pipeline.run_feature_validator(args.root, args.feature_request_file, report=print)
        return 0

    parser.print_help()
    return 1
