import pytutorial


def test_parse_scores():
    assert pytutorial.parse_scores("90| 91.5 |88") == [90, 91.5, 88]
    assert pytutorial.parse_scores("   ") == []


def test_save_and_load_students_csv(tmp_path, sample_students):
    path = tmp_path / "students.csv"

    pytutorial.save_students_csv(path, sample_students)
    loaded_students = pytutorial.load_students_csv(path)

    assert [student.name for student in loaded_students] == ["Ada", "Grace", "Linus"]
    assert loaded_students[0].scores == [100, 95, 98]
