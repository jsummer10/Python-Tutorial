"""Data models for demonstrating classes and dataclasses."""

from dataclasses import dataclass, field
from typing import Dict, Iterable, List

from ..errors import InvalidStudentError
from ..utilities.stats import average


@dataclass
class Student:
    """A student with a name and a list of assignment scores.

    Attributes:
        name: The student's display name.
        scores: Assignment scores from 0 to 100.

    Raises:
        InvalidStudentError: If the name is blank or a score is outside the
            inclusive range from 0 to 100.
    """

    name: str
    scores: List[float] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Normalize and validate dataclass fields after initialization.

        Returns:
            None. The ``name`` field may be stripped in place.

        Raises:
            InvalidStudentError: If the name is blank or a score is outside the
                inclusive range from 0 to 100.
        """
        self.name = self.name.strip()
        if not self.name:
            raise InvalidStudentError("student name cannot be blank")
        if any(score < 0 or score > 100 for score in self.scores):
            raise InvalidStudentError("scores must be between 0 and 100")

    @property
    def average_score(self) -> float:
        """Return the student's average score.

        Returns:
            The arithmetic mean of the student's scores.

        Raises:
            EmptyDataError: If the student has no scores.
        """
        return average(self.scores)

    def add_score(self, score: float) -> None:
        """Add one assignment score to the student.

        Args:
            score: Assignment score to append.

        Returns:
            None. The student's ``scores`` list is updated in place.

        Raises:
            InvalidStudentError: If ``score`` is outside the inclusive range
                from 0 to 100.
        """
        if score < 0 or score > 100:
            raise InvalidStudentError("scores must be between 0 and 100")
        self.scores.append(score)

    def is_passing(self, passing_score: float = 70) -> bool:
        """Return whether the student's average meets the passing score.

        Args:
            passing_score: Minimum average considered passing.

        Returns:
            True if the student's average is at least ``passing_score``.

        Raises:
            EmptyDataError: If the student has no scores.
        """
        return self.average_score >= passing_score

    def to_dict(self) -> Dict[str, object]:
        """Return a serializable dictionary representation.

        Returns:
            A dictionary containing the student's name, scores, average, and
            passing status.

        Raises:
            EmptyDataError: If the student has no scores.
        """
        return {
            "name": self.name,
            "scores": list(self.scores),
            "average": self.average_score,
            "passing": self.is_passing(),
        }


class GradeBook:
    """A collection of students with convenience reporting methods."""

    def __init__(self, students: Iterable[Student] = ()) -> None:
        """Initialize a grade book.

        Args:
            students: Initial students to add to the grade book.
        """
        self._students = {}
        for student in students:
            self.add_student(student)

    def add_student(self, student: Student) -> None:
        """Add or replace a student by name.

        Args:
            student: Student to store.

        Returns:
            None. The grade book is updated in place.
        """
        self._students[student.name] = student

    def get_student(self, name: str) -> Student:
        """Return a student by name.

        Args:
            name: Student name to look up.

        Returns:
            The matching student.

        Raises:
            KeyError: If no student exists with ``name``.
        """
        return self._students[name]

    def class_average(self) -> float:
        """Return the average of all student averages.

        Returns:
            The average of each student's average score.

        Raises:
            EmptyDataError: If the grade book has no students or a student has
                no scores.
        """
        return average(student.average_score for student in self._students.values())

    def passing_students(self, passing_score: float = 70) -> List[Student]:
        """Return students whose average is at least a passing score.

        Args:
            passing_score: Minimum average considered passing.

        Returns:
            Students whose averages meet or exceed ``passing_score``.

        Raises:
            EmptyDataError: If a student has no scores.
        """
        return [
            student
            for student in self._students.values()
            if student.is_passing(passing_score)
        ]

    def summary(self) -> Dict[str, object]:
        """Return a small report about the grade book.

        Returns:
            A dictionary with the student count, class average, and passing
            student names.

        Raises:
            EmptyDataError: If the grade book has no students or a student has
                no scores.
        """
        return {
            "student_count": len(self._students),
            "class_average": self.class_average(),
            "passing_students": [
                student.name for student in self.passing_students()
            ],
        }
