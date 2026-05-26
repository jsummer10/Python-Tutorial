# Black

## Project

[https://github.com/psf/black](https://github.com/psf/black)

## What It Is

Black is an opinionated Python code formatter. It takes Python source files, parses them, and rewrites the formatting into a consistent style.

The key idea behind Black is that formatting should not be a recurring debate. Instead of offering many style options, Black intentionally keeps configuration small. Teams accept the formatter's style, run it automatically, and spend code review time on behavior instead of whitespace.

Black does not try to find bugs or enforce broad linting rules. Its job is narrower: make Python code look consistent across files, authors, editors, and pull requests.

## What It's Used For

- Automatic Formatting: Black reformats Python files so spacing, line breaks, indentation, and layout are consistent.
- Reducing Style Arguments: By using a fixed style, teams avoid spending review time debating small formatting choices.
- Editor Formatting: Black can run on save, giving developers immediate formatting feedback.
- CI Checks: Projects can run Black in check mode to make sure committed code has already been formatted.
- Consistent Diffs: Automated formatting makes code changes easier to review because layout decisions are handled uniformly.
- Toolchain Baseline: Many Python projects use Black as the formatter and combine it with linters or type checkers for broader analysis.

## Demo

[https://black.readthedocs.io/](https://black.readthedocs.io/)

