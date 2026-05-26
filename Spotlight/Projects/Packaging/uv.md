# uv

## Project

[https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

## What It Is

uv is a fast Python package and project manager written in Rust. It is built by Astral, the same team behind Ruff, and is designed to replace several tools that Python developers often have to combine manually: `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `virtualenv`, and more.

The main idea is simple: Python project setup should be fast, reproducible, and handled by one tool. uv can create virtual environments, install packages, resolve dependencies, lock project requirements, install Python versions, run scripts, and execute command-line tools published as Python packages.

Because uv uses a global cache and a very fast dependency resolver, repeated installs are often dramatically quicker than traditional `pip` workflows. That makes it useful both on a developer's laptop and in CI, where dependency installation can be one of the slowest parts of a test run.

## What It's Used For

- Project Management: uv can initialize a project, manage dependencies in `pyproject.toml`, create a lockfile, and sync the local environment so everyone is using the same resolved package set.
- Faster Dependency Installs: It can install dependencies much faster than typical `pip` workflows, especially when packages are already available in the global cache.
- Python Version Management: uv can install and select Python versions for a project, reducing the need for a separate version manager.
- Tool Execution: It can run tools like Ruff, pytest, or Black-style command-line utilities without permanently installing them into a project environment.
- Script Dependencies: uv supports scripts with inline dependency metadata, making small Python scripts easier to share and run reproducibly.
- CI Setup: In GitHub Actions or other CI systems, uv can speed up environment creation and make dependency resolution more predictable.

## Demo

[https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

