"""String examples for demonstrating simple functions."""


def greeting(name: str = "Python learner") -> str:
    """Return a friendly greeting for a person using the tutorial.

    Args:
        name: The name to include in the greeting. Blank names use the
            default tutorial learner label.

    Returns:
        A greeting string.
    """
    clean_name = name.strip() or "Python learner"
    return f"Hello, {clean_name}!"
