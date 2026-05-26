# PyTutorial Sample Package

`pytutorial` is a small example package used by the tutorial's packaging,
testing, and project-structure lessons. It uses a `src` layout, a
`pyproject.toml`, and a pytest test folder.

## Structure

- [pyproject.toml](pyproject.toml) - package metadata and tool configuration.
- [src/pytutorial](src/pytutorial) - the importable package.
- [tests](tests) - package tests.

## Try It

```bash
python src/pytutorial/main.py
pytest
```

The package currently exposes a simple `execute()` function that prints a short
message. Install it in editable mode first if you want to run it as an importable
package with `python -m pytutorial`.
