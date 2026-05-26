# PyTutorial Sample Package

`pytutorial` is an example package used by the tutorial's packaging, testing,
and project-structure lessons. It uses a `src` layout, a `pyproject.toml`, a
pytest test folder, and a small public API that demonstrates common Python
features.

## Structure

- [pyproject.toml](pyproject.toml) - package metadata and tool configuration.
- [src/pytutorial](src/pytutorial) - the importable package.
- [src/pytutorial/basics](src/pytutorial/basics) - introductory function examples.
- [src/pytutorial/grades](src/pytutorial/grades) - classes, dataclasses, and CSV file helpers.
- [src/pytutorial/utilities](src/pytutorial/utilities) - reusable text and statistics helpers.
- [tests](tests) - package tests split by feature area.

## Public API

Functions:

- `pytutorial.greeting(name="Python learner")` returns a greeting string.
- `pytutorial.add(left, right)` returns the sum of two integers.
- `pytutorial.execute(name="Python learner")` prints the greeting.
- `pytutorial.__version__` exposes the package version.

Statistics:

- `pytutorial.average(values)` returns the arithmetic mean.
- `pytutorial.median(values)` returns the middle sorted value.
- `pytutorial.passing_rate(scores, passing_score=70)` returns a fraction.

Text helpers:

- `pytutorial.normalize_whitespace(text)` cleans up repeated whitespace.
- `pytutorial.slugify(text)` creates a lowercase URL slug.
- `pytutorial.word_count(text)` counts words in a string.
- `pytutorial.top_words(text, limit=3)` returns the most common words.

Classes:

- `pytutorial.Student(name, scores)` demonstrates dataclasses and validation.
- `pytutorial.GradeBook(students)` demonstrates a small class that manages a
  collection.

Files:

- `pytutorial.parse_scores(raw_scores)` parses pipe-separated scores.
- `pytutorial.load_students_csv(path)` reads students from CSV.
- `pytutorial.save_students_csv(path, students)` writes students to CSV.

Errors:

- `pytutorial.EmptyDataError` is raised for empty calculations.
- `pytutorial.InvalidStudentError` is raised for invalid student data.

## Test Examples

The pytest suite demonstrates:

- normal assertions
- `pytest.mark.parametrize`
- fixtures
- `tmp_path` for temporary files
- `pytest.raises`
- `capsys` for captured output

Test files are split by topic:

- `test_basics.py`
- `test_cli.py`
- `test_grades.py`
- `test_package.py`
- `test_stats.py`
- `test_storage.py`
- `test_text.py`

## Try It

```bash
uv run python -m pytutorial
uv run pytest
```

Or install the package in editable mode if you want to import it or run it with
`python -m pytutorial` from outside this directory:

```bash
python -m pip install -e .
```
