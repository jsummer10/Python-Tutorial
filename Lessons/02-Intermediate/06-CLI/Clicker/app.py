#!/usr/bin/env python3
"""
CLI tool built with Click — a popular third-party library from Pallets.
Implements the same "file utility" with subcommands: info, search, and convert.

Install: pip install click
"""

import os
import sys
from pathlib import Path

import click


# ── CLI group (the root command) ──────────────────────────────────────────────

@click.group()
@click.version_option("1.0.0", prog_name="filetool")
def cli():
    """A handy file utility — Click edition."""


# ── info ──────────────────────────────────────────────────────────────────────

@cli.command()
@click.argument("file", type=click.Path(exists=True, readable=True))
@click.option("-v", "--verbose", is_flag=True, help="Show extra metadata.")
def info(file, verbose):
    """Show information about FILE."""
    path = Path(file)
    stat = path.stat()

    click.echo(f"Name   : {path.name}")
    click.echo(f"Path   : {path.resolve()}")
    click.echo(f"Size   : {stat.st_size:,} bytes")
    click.echo(f"Suffix : {path.suffix or '(none)'}")

    if verbose:
        import datetime
        mtime = datetime.datetime.fromtimestamp(stat.st_mtime)
        click.echo(f"Modified : {mtime:%Y-%m-%d %H:%M:%S}")
        click.echo(f"Readable : {os.access(path, os.R_OK)}")
        click.echo(f"Writable : {os.access(path, os.W_OK)}")


# ── search ────────────────────────────────────────────────────────────────────

@cli.command()
@click.argument("file", type=click.Path(exists=True, readable=True))
@click.argument("pattern")
@click.option("-i", "--ignore-case", is_flag=True, help="Case-insensitive search.")
@click.option("-n", "--line-numbers", is_flag=True, help="Show line numbers.")
@click.option("-m", "--max-results", default=None, type=int,
              metavar="N", help="Stop after N matches.")
def search(file, pattern, ignore_case, line_numbers, max_results):
    """Search for PATTERN in FILE."""
    path = Path(file)
    needle = pattern.lower() if ignore_case else pattern
    matches = []

    with open(path, encoding="utf-8", errors="replace") as fh:
        for lineno, line in enumerate(fh, 1):
            haystack = line.lower() if ignore_case else line
            if needle in haystack:
                matches.append((lineno, line.rstrip()))
                if max_results and len(matches) >= max_results:
                    break

    if not matches:
        click.secho("No matches found.", fg="yellow")
        return

    for lineno, line in matches:
        if line_numbers:
            click.echo(f"{click.style(str(lineno).rjust(4), fg='cyan')}: {line}")
        else:
            click.echo(line)

    click.secho(f"\n{len(matches)} match(es) found.", fg="green")


# ── convert ───────────────────────────────────────────────────────────────────

@cli.command()
@click.argument("file", type=click.Path(exists=True, readable=True))
@click.option("--line-ending", type=click.Choice(["unix", "windows"]),
              default="unix", show_default=True, help="Target line ending style.")
@click.option("--from-encoding", default="utf-8", show_default=True,
              metavar="ENC", help="Source encoding.")
@click.option("--to-encoding", default="utf-8", show_default=True,
              metavar="ENC", help="Target encoding.")
@click.option("-o", "--output", default=None, type=click.Path(),
              metavar="FILE", help="Output path.")
@click.confirmation_option(prompt="Overwrite output file if it exists?")
def convert(file, line_ending, from_encoding, to_encoding, output):
    """Convert FILE line endings or encoding."""
    path = Path(file)
    text = path.read_text(encoding=from_encoding, errors="replace")

    if line_ending == "unix":
        text = text.replace("\r\n", "\n").replace("\r", "\n")
    else:
        text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "\r\n")

    out_path = Path(output) if output else path.with_suffix(".converted" + path.suffix)
    out_path.write_text(text, encoding=to_encoding)
    click.secho(f"Converted → {out_path}", fg="green", bold=True)


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    cli()