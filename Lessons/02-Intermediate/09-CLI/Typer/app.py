#!/usr/bin/env python3
"""
CLI tool built with Typer — a modern library built on Click, driven by type hints.
Implements the same "file utility" with subcommands: info, search, and convert.

Install: pip install "typer[all]"
"""

import os
from enum import Enum
from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated

EPILOG = """
[bold]Example Usage:[/bold]\n
  python cli_typer.py info README.md --verbose\n
  python cli_typer.py search README.md 'TODO' --ignore-case --line-numbers\n
  python cli_typer.py convert data.txt --line-ending unix
"""

app = typer.Typer(
    name="filetool",
    help="A handy file utility — Typer edition.",
    add_completion=True,
    context_settings={"help_option_names": ["-h", "--help"]},
    epilog=EPILOG
)


# ── Enum for line ending choice ───────────────────────────────────────────────

class LineEnding(str, Enum):
    unix = "unix"
    windows = "windows"


# ── info ──────────────────────────────────────────────────────────────────────

@app.command()
def info(
    file: Annotated[Path, typer.Argument(help="Path to the file.",
                                         exists=True, readable=True)],
    verbose: Annotated[bool, typer.Option("-v", "--verbose",
                                          help="Show extra metadata.")] = False,
):
    """Show information about FILE."""
    stat = file.stat()

    typer.echo(f"Name   : {file.name}")
    typer.echo(f"Path   : {file.resolve()}")
    typer.echo(f"Size   : {stat.st_size:,} bytes")
    typer.echo(f"Suffix : {file.suffix or '(none)'}")

    if verbose:
        import datetime
        mtime = datetime.datetime.fromtimestamp(stat.st_mtime)
        typer.echo(f"Modified : {mtime:%Y-%m-%d %H:%M:%S}")
        typer.echo(f"Readable : {os.access(file, os.R_OK)}")
        typer.echo(f"Writable : {os.access(file, os.W_OK)}")


# ── search ────────────────────────────────────────────────────────────────────

@app.command()
def search(
    file: Annotated[Path, typer.Argument(help="Path to the file.",
                                         exists=True, readable=True)],
    pattern: Annotated[str, typer.Argument(help="Text pattern to search for.")],
    ignore_case: Annotated[bool, typer.Option("-i", "--ignore-case",
                                              help="Case-insensitive search.")] = False,
    line_numbers: Annotated[bool, typer.Option("-n", "--line-numbers",
                                               help="Show line numbers.")] = False,
    max_results: Annotated[Optional[int], typer.Option("-m", "--max-results",
                                                       help="Stop after N matches.",
                                                       metavar="N")] = None,
):
    """Search for PATTERN in FILE."""
    needle = pattern.lower() if ignore_case else pattern
    matches: list[tuple[int, str]] = []

    with open(file, encoding="utf-8", errors="replace") as fh:
        for lineno, line in enumerate(fh, 1):
            haystack = line.lower() if ignore_case else line
            if needle in haystack:
                matches.append((lineno, line.rstrip()))
                if max_results and len(matches) >= max_results:
                    break

    if not matches:
        typer.secho("No matches found.", fg=typer.colors.YELLOW)
        raise typer.Exit()

    for lineno, line in matches:
        if line_numbers:
            typer.echo(f"{typer.style(str(lineno).rjust(4), fg=typer.colors.CYAN)}: {line}")
        else:
            typer.echo(line)

    typer.secho(f"\n{len(matches)} match(es) found.", fg=typer.colors.GREEN)


# ── convert ───────────────────────────────────────────────────────────────────

@app.command()
def convert(
    file: Annotated[Path, typer.Argument(help="Path to the file.",
                                         exists=True, readable=True)],
    line_ending: Annotated[LineEnding, typer.Option(
        help="Target line ending style.")] = LineEnding.unix,
    from_encoding: Annotated[str, typer.Option(
        "--from-encoding", metavar="ENC", help="Source encoding.")] = "utf-8",
    to_encoding: Annotated[str, typer.Option(
        "--to-encoding", metavar="ENC", help="Target encoding.")] = "utf-8",
    output: Annotated[Optional[Path], typer.Option(
        "-o", "--output", metavar="FILE", help="Output path.")] = None,
):
    """Convert FILE line endings or encoding."""
    typer.confirm("Overwrite output file if it exists?", abort=True)

    text = file.read_text(encoding=from_encoding, errors="replace")

    if line_ending == LineEnding.unix:
        text = text.replace("\r\n", "\n").replace("\r", "\n")
    else:
        text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "\r\n")

    out_path = output or file.with_suffix(".converted" + file.suffix)
    out_path.write_text(text, encoding=to_encoding)
    typer.secho(f"Converted → {out_path}", fg=typer.colors.GREEN, bold=True)


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app()