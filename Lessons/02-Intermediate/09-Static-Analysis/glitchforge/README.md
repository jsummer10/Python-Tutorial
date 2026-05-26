# glitchforge

`glitchforge` is a deliberately inconsistent Python package for exercising static
code checkers. It includes style issues, type issues, dead code, questionable
security patterns, mutable defaults, broad exceptions, unused imports, complex
branches, and a few runtime bugs.

It is not intended for production use.

## Try It

```bash
python -m glitchforge --count 3
```

## Use With Tools

Run linters, formatters, type checkers, security scanners, and tests against this
package to see the kinds of issues each tool reports. The point is to inspect and
discuss the findings, not to treat this as clean application code.
