import pytest

import pytutorial


@pytest.mark.parametrize(
    "values, expected",
    [
        ([10, 20, 30], 20),
        ((1, 2, 3, 4), 2.5),
    ],
)
def test_average(values, expected):
    assert pytutorial.average(values) == expected


@pytest.mark.parametrize(
    "values, expected",
    [
        ([3, 1, 2], 2),
        ([10, 40, 20, 30], 25),
    ],
)
def test_median(values, expected):
    assert pytutorial.median(values) == expected


def test_stats_reject_empty_values():
    with pytest.raises(pytutorial.EmptyDataError, match="at least one value"):
        pytutorial.average([])


def test_passing_rate():
    assert pytutorial.passing_rate([100, 70, 69, 80]) == 0.75
