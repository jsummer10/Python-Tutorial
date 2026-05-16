# glitchforge

`glitchforge` is a deliberately inconsistent Python package for exercising static
code checkers. It includes style issues, type issues, dead code, questionable
security patterns, mutable defaults, broad exceptions, unused imports, complex
branches, and a few runtime bugs.

It is not intended for production use.

Example:

```bash
python -m glitchforge --count 3
```
