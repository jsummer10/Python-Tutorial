# isort

## Project

[https://github.com/PyCQA/isort](https://github.com/PyCQA/isort)

## What It Is

isort is a Python utility for sorting and organizing imports. It rewrites import sections into a consistent order so developers do not have to manually arrange standard library imports, third-party imports, and local project imports.

Import order seems small, but it becomes noisy in real code reviews. Without an automated tool, pull requests can fill up with minor disagreements about whether one import belongs above another. isort removes that discussion by applying the same rules every time.

It can be used directly as a command-line formatter, through editor integrations, in pre-commit hooks, or as part of CI. Many projects pair isort with Black so files are both consistently formatted and consistently organized.

## What It's Used For

- Sorting Imports: isort alphabetizes and groups imports into consistent sections.
- Separating Import Categories: It can distinguish standard library, third-party, first-party, and local imports.
- Reducing Review Noise: Automated import sorting prevents style-only import changes from becoming manual code review comments.
- Formatting Existing Files: Running isort across a codebase can normalize old files that accumulated inconsistent import order over time.
- Pre-Commit Hooks: It is commonly run before commits so import cleanup happens automatically.
- Formatter Pairing: isort is often configured to work with Black so the two tools do not fight over formatting.

## Demo

[https://pycqa.github.io/isort/](https://pycqa.github.io/isort/)

