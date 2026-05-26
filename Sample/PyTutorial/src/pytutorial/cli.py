"""Command-line demonstration for the PyTutorial sample package."""

from .basics import greeting
from .grades import GradeBook, Student


def execute(name: str = "Python learner") -> None:
    """Print a short demonstration of the sample package.

    Args:
        name: The name to include in the greeting line.

    Returns:
        None. The demonstration is written to standard output.
    """
    gradebook = GradeBook(
        [
            Student("Ada", [100, 95, 98]),
            Student("Grace", [88, 92, 85]),
            Student("Linus", [60, 65, 70]),
        ]
    )

    print(greeting(name))
    print(f"Class average: {gradebook.class_average():.1f}")
    print(f"Students passing: {', '.join(gradebook.summary()['passing_students'])}")


if __name__ == "__main__":
    execute()
