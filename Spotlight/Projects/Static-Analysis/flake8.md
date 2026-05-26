# Flake8

## Project

[https://github.com/PyCQA/flake8](https://github.com/PyCQA/flake8)

## What It Is

Flake8 is a Python linting tool that combines several checks behind one command-line interface. It brings together PyFlakes for logical errors, pycodestyle for style conventions, and McCabe complexity checks.

Before tools like Ruff consolidated large parts of the Python linting workflow, Flake8 was one of the most common ways to enforce code quality in Python projects. It is still widely recognized because of its plugin ecosystem and its simple mental model: run `flake8`, get a list of line-level issues to fix.

Flake8 focuses on static analysis. It does not run the program. Instead, it scans the source code for patterns that are likely to be mistakes, style violations, unused imports, or overly complex functions.

## What It's Used For

- Finding Common Mistakes: Flake8 can catch unused imports, undefined names, syntax-adjacent mistakes, and other issues found by PyFlakes.
- Enforcing Style: It can report code that violates selected pycodestyle rules, helping teams keep formatting and layout consistent.
- Measuring Complexity: Its McCabe checks can flag functions that are getting too complex to reason about easily.
- Plugin-Based Checks: Teams can add plugins for docstrings, annotations, import order, bugbear-style checks, and many other rule families.
- Editor Feedback: Flake8 can run in editors to show lint errors while code is being written.
- CI Enforcement: It is often used in pull requests to block code that violates a project's linting rules.

## Demo

[https://flake8.pycqa.org/](https://flake8.pycqa.org/)

