# Typer

## Project

[https://github.com/fastapi/typer](https://github.com/fastapi/typer)

## What It Is

Typer is a Python library for building command-line applications using type hints. It is created by the FastAPI author and follows a similar philosophy: use standard Python type annotations to generate useful behavior with minimal boilerplate.

Typer is built on top of Click, so it inherits a mature command-line foundation. The difference is the developer experience. Instead of declaring many command options manually, Typer can infer argument types, defaults, help text, and validation from normal Python function signatures.

This makes Typer especially approachable for modern Python projects that already use type hints. A function can become a command-line interface with very little extra code.

## What It's Used For

- Typed CLI Apps: Typer turns annotated Python functions into command-line commands.
- Argument Parsing: It uses type hints to parse strings from the terminal into Python values like `int`, `bool`, `Path`, or enums.
- Auto-Generated Help: Typer creates command help output from function names, parameters, defaults, and docstrings.
- Shell Completion: It can generate shell completion support for command-line tools.
- Multi-Command Tools: Typer supports apps with multiple commands and subcommands.
- Internal Automation: It is useful for scripts that begin small but need a clean interface as they become team tools.

## Demo

[https://typer.tiangolo.com/](https://typer.tiangolo.com/)

