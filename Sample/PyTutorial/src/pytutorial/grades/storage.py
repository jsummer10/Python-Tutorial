"""File helpers for demonstrating standard-library CSV handling."""

import csv
from pathlib import Path
from typing import Iterable, List

from .models import Student


def parse_scores(raw_scores: str) -> List[float]:
    """Parse a pipe-separated score string.

    Args:
        raw_scores: Scores formatted like ``"90|85|100"``.

    Returns:
        A list of scores as floats. Blank input returns an empty list.

    Raises:
        ValueError: If any score cannot be converted to a float.
    """
    if not raw_scores.strip():
        return []
    return [float(score.strip()) for score in raw_scores.split("|")]


def load_students_csv(path: Path) -> List[Student]:
    """Load students from a CSV file with ``name`` and ``scores`` columns.

    Args:
        path: CSV file to read.

    Returns:
        A list of students from the file.

    Raises:
        FileNotFoundError: If ``path`` does not exist.
        KeyError: If the CSV is missing required columns.
        InvalidStudentError: If a row contains invalid student data.
        ValueError: If a score cannot be converted to a float.
    """
    students = []
    with Path(path).open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            students.append(Student(row["name"], parse_scores(row["scores"])))
    return students


def save_students_csv(path: Path, students: Iterable[Student]) -> None:
    """Save students to a CSV file with ``name`` and ``scores`` columns.

    Args:
        path: CSV file to write.
        students: Students to serialize.

    Returns:
        None. The file at ``path`` is created or replaced.
    """
    with Path(path).open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "scores"])
        writer.writeheader()
        for student in students:
            scores = "|".join(str(score) for score in student.scores)
            writer.writerow({"name": student.name, "scores": scores})
