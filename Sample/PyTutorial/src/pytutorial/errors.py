"""Custom exceptions used by the tutorial package."""


class PyTutorialError(Exception):
    """Base exception for package-specific errors.

    This gives callers one exception type they can catch for any intentional
    error raised by this package.
    """


class EmptyDataError(PyTutorialError):
    """Raised when a calculation needs at least one value."""


class InvalidStudentError(PyTutorialError):
    """Raised when student data is incomplete or invalid."""
