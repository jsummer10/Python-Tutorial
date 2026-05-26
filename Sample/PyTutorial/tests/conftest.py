import pytest

import pytutorial


@pytest.fixture
def sample_students():
    return [
        pytutorial.Student("Ada", [100, 95, 98]),
        pytutorial.Student("Grace", [88, 92, 85]),
        pytutorial.Student("Linus", [60, 65, 70]),
    ]
