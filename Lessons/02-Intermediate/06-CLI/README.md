# Python Command Line Interface

This section compares several ways to build command-line and terminal
applications in Python. The examples include a shared file utility implemented
with multiple CLI frameworks, plus Rich and Textual demos for richer terminal
interfaces.

## Examples

- [Argparse](Argparse/app.py) - standard-library command parsing.
- [Click](Clicker/app.py) - decorator-based commands and options.
- [Typer](Typer/app.py) - type-hint-driven CLI commands.
- [Rich](Rich/app.py) - formatted terminal output, tables, progress, panels, and
  syntax highlighting.
- [Textual](Textual/app.py) - an interactive terminal UI application.

## Try It

```bash
python Argparse/app.py --help
python Clicker/app.py --help
python Typer/app.py --help
python Rich/app.py
python Textual/app.py
```

Install the relevant third-party package before running the Click, Typer, Rich,
or Textual examples.
