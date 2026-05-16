#!/usr/bin/env python3
"""
CLI tool built with argparse — Python's built-in argument parsing library.
Implements a "file utility" with subcommands: info, search, and convert.
"""

import argparse
import os
import sys
from pathlib import Path


# ── Handlers ──────────────────────────────────────────────────────────────────

def cmd_info(args):
    """Show information about a file."""
    path = Path(args.file)
    if not path.exists():
        print(f"Error: '{args.file}' does not exist.", file=sys.stderr)
        sys.exit(1)

    stat = path.stat()
    print(f"Name   : {path.name}")
    print(f"Path   : {path.resolve()}")
    print(f"Size   : {stat.st_size:,} bytes")
    print(f"Suffix : {path.suffix or '(none)'}")

    if args.verbose:
        import datetime
        mtime = datetime.datetime.fromtimestamp(stat.st_mtime)
        print(f"Modified : {mtime:%Y-%m-%d %H:%M:%S}")
        print(f"Readable : {os.access(path, os.R_OK)}")
        print(f"Writable : {os.access(path, os.W_OK)}")


def cmd_search(args):
    """Search for a pattern in a file."""
    path = Path(args.file)
    if not path.exists():
        print(f"Error: '{args.file}' does not exist.", file=sys.stderr)
        sys.exit(1)

    pattern = args.pattern.lower() if args.ignore_case else args.pattern
    matches = []

    with open(path, encoding="utf-8", errors="replace") as fh:
        for lineno, line in enumerate(fh, 1):
            haystack = line.lower() if args.ignore_case else line
            if pattern in haystack:
                matches.append((lineno, line.rstrip()))
                if args.max_results and len(matches) >= args.max_results:
                    break

    if not matches:
        print("No matches found.")
        return

    for lineno, line in matches:
        if args.line_numbers:
            print(f"{lineno:4d}: {line}")
        else:
            print(line)

    print(f"\n{len(matches)} match(es) found.")


def cmd_convert(args):
    """Convert file line endings or encoding."""
    path = Path(args.file)
    if not path.exists():
        print(f"Error: '{args.file}' does not exist.", file=sys.stderr)
        sys.exit(1)

    text = path.read_text(encoding=args.from_encoding, errors="replace")

    if args.line_ending == "unix":
        text = text.replace("\r\n", "\n").replace("\r", "\n")
    elif args.line_ending == "windows":
        text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "\r\n")

    out_path = Path(args.output) if args.output else path.with_suffix(".converted" + path.suffix)
    out_path.write_text(text, encoding=args.to_encoding)
    print(f"Converted → {out_path}")


# ── Parser setup ──────────────────────────────────────────────────────────────

def build_parser():
    parser = argparse.ArgumentParser(
        prog="filetool",
        description="A handy file utility — argparse edition.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s info README.md --verbose
  %(prog)s search README.md "TODO" --ignore-case --line-numbers
  %(prog)s convert data.txt --line-ending unix --to-encoding utf-8
        """,
    )

    # Global flags
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")
    subparsers.required = True  # Require a subcommand

    # ── info ──
    p_info = subparsers.add_parser("info", help="Show file information")
    p_info.add_argument("file", help="Path to the file")
    p_info.add_argument("-v", "--verbose", action="store_true",
                        help="Show extra metadata (timestamps, permissions)")
    p_info.set_defaults(func=cmd_info)

    # ── search ──
    p_search = subparsers.add_parser("search", help="Search for a pattern in a file")
    p_search.add_argument("file", help="Path to the file")
    p_search.add_argument("pattern", help="Text pattern to search for")
    p_search.add_argument("-i", "--ignore-case", action="store_true",
                          help="Case-insensitive search")
    p_search.add_argument("-n", "--line-numbers", action="store_true",
                          help="Show line numbers in output")
    p_search.add_argument("-m", "--max-results", type=int, default=None,
                          metavar="N", help="Stop after N matches")
    p_search.set_defaults(func=cmd_search)

    # ── convert ──
    p_conv = subparsers.add_parser("convert", help="Convert line endings or encoding")
    p_conv.add_argument("file", help="Path to the file")
    p_conv.add_argument("--line-ending", choices=["unix", "windows"], default="unix",
                        help="Target line ending style (default: unix)")
    p_conv.add_argument("--from-encoding", default="utf-8", metavar="ENC",
                        help="Source encoding (default: utf-8)")
    p_conv.add_argument("--to-encoding", default="utf-8", metavar="ENC",
                        help="Target encoding (default: utf-8)")
    p_conv.add_argument("-o", "--output", default=None, metavar="FILE",
                        help="Output path (default: <file>.converted<ext>)")
    p_conv.set_defaults(func=cmd_convert)

    return parser


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()