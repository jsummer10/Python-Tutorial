import pytest

import pytutorial


def test_student_average_and_passing_status():
    student = pytutorial.Student("Ada", [100, 95])
    student.add_score(98)

    assert student.average_score == pytest.approx(97.6666667)
    assert student.is_passing()
    assert student.to_dict() == {
        "name": "Ada",
        "scores": [100, 95, 98],
        "average": pytest.approx(97.6666667),
        "passing": True,
    }


@pytest.mark.parametrize(
    "name, scores",
    [
        ("   ", [90]),
        ("Ada", [-1]),
        ("Ada", [101]),
    ],
)
def test_student_rejects_invalid_data(name, scores):
    with pytest.raises(pytutorial.InvalidStudentError):
        pytutorial.Student(name, scores)


def test_gradebook_summary(sample_students):
    gradebook = pytutorial.GradeBook(sample_students)

    assert gradebook.get_student("Ada").average_score == pytest.approx(97.6666667)
    assert gradebook.class_average() == pytest.approx(83.6666667)
    assert [student.name for student in gradebook.passing_students()] == [
        "Ada",
        "Grace",
    ]
    assert gradebook.summary() == {
        "student_count": 3,
        "class_average": pytest.approx(83.6666667),
        "passing_students": ["Ada", "Grace"],
    }
