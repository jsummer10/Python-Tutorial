import pytutorial


def test_text_helpers():
    text = " Python   Python tests, readable tests! "

    assert pytutorial.normalize_whitespace(text) == "Python Python tests, readable tests!"
    assert pytutorial.slugify("Build a Python Package!") == "build-a-python-package"
    assert pytutorial.word_count(text) == {
        "python": 2,
        "tests": 2,
        "readable": 1,
    }
    assert pytutorial.top_words(text, limit=2) == ["python", "tests"]
