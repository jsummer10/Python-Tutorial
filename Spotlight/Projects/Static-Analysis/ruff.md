# Ruff

## Project

[https://github.com/astral-sh/ruff](https://github.com/astral-sh/ruff)

## What It Is

Ruff is an extremely fast Python linter and code formatter written in Rust. It is designed to replace or consolidate many common Python code-quality tools, including Flake8, isort, pyupgrade, pydocstyle, autoflake, and parts of other plugin-based linting workflows.

Traditionally, Python projects often stack several tools together: one for linting, one for import sorting, one for formatting, and several plugins for specific rule families. That works, but it can make configuration slower, noisier, and harder to teach. Ruff puts much of that workflow behind a single command-line tool.

The performance difference is the part that makes Ruff stand out. Because it is implemented in Rust and designed around fast static analysis, it can lint large codebases quickly enough to run constantly in editors, pre-commit hooks, and CI jobs without becoming a bottleneck.

## What It's Used For

- Linting Python Code: `ruff check` scans Python files for bugs, unused imports, style issues, modernization opportunities, and many other rule categories.
- Automatic Fixes: Ruff can automatically fix many violations, such as unused imports, import ordering, and simple modernization rules.
- Code Formatting: `ruff format` formats Python code with a Black-compatible style goal, giving projects a fast formatter in the same tool as the linter.
- Import Sorting: Ruff can replace many `isort` workflows, keeping imports organized without running a separate command.
- Editor Feedback: Because Ruff is fast, it works well inside editors where developers want near-instant feedback as they type.
- CI Enforcement: Teams can use Ruff in pull requests to keep style and common correctness checks consistent before code is merged.

## Demo

[https://docs.astral.sh/ruff/](https://docs.astral.sh/ruff/)

