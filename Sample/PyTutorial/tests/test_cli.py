import pytutorial


def test_execute_prints_demo(capsys):
    pytutorial.execute("Grace")

    captured = capsys.readouterr()
    assert captured.out.splitlines() == [
        "Hello, Grace!",
        "Class average: 83.7",
        "Students passing: Ada, Grace",
    ]
