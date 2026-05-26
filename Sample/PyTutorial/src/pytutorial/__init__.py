"""A reference package for the Python tutorial.

The package demonstrates source layout, imports, functions, classes,
dataclasses, exceptions, file helpers, tests, package metadata, and
command-line execution.
"""

from .__version__ import __version__
from .basics import add, greeting
from .cli import execute
from .errors import EmptyDataError, InvalidStudentError, PyTutorialError
from .grades import (
    GradeBook,
    Student,
    load_students_csv,
    parse_scores,
    save_students_csv,
)
from .utilities import (
    average,
    median,
    normalize_whitespace,
    passing_rate,
    slugify,
    top_words,
    word_count,
)

__all__ = [
    "__version__",
    "EmptyDataError",
    "GradeBook",
    "InvalidStudentError",
    "PyTutorialError",
    "Student",
    "add",
    "average",
    "execute",
    "greeting",
    "load_students_csv",
    "median",
    "normalize_whitespace",
    "parse_scores",
    "passing_rate",
    "save_students_csv",
    "slugify",
    "top_words",
    "word_count",
]
