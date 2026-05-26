import pytest

import pytutorial


def test_greeting_uses_default_name():
    assert pytutorial.greeting() == "Hello, Python learner!"


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Ada", "Hello, Ada!"),
        ("  Grace  ", "Hello, Grace!"),
        ("   ", "Hello, Python learner!"),
    ],
)
def test_greeting_formats_names(name, expected):
    assert pytutorial.greeting(name) == expected


def test_add_returns_sum():
    assert pytutorial.add(2, 3) == 5
