# mypy

## Project

[https://github.com/python/mypy](https://github.com/python/mypy)

## What It Is

mypy is a static type checker for Python. It reads Python code and type hints, then checks whether values are being used consistently with the types the code claims to support.

Python itself is dynamically typed, so type errors usually show up when the code runs. mypy moves some of that feedback earlier. If a function says it expects a `str`, but another part of the program passes an `int`, mypy can flag that mismatch before the program reaches production.

mypy is built around gradual typing. A project does not need perfect annotations everywhere on day one. Teams can add type hints to the most important modules first, run mypy in CI, and tighten the rules over time.

## What It's Used For

- Catching Type Mismatches: mypy can find places where a value's inferred type does not match the function, class, or variable annotation.
- Documenting Interfaces: Type hints make function signatures easier to understand without reading the full implementation.
- Safer Refactoring: When changing a function signature or data model, mypy can point out call sites that still use the old shape.
- Gradual Adoption: Teams can start with loose settings and make type checking stricter as the codebase matures.
- CI Enforcement: Running mypy in pull requests helps catch type-related regressions before merge.
- Library Development: Public APIs benefit from type hints because users and editors can understand expected inputs and outputs more clearly.

## Demo

[https://mypy.readthedocs.io/](https://mypy.readthedocs.io/)

