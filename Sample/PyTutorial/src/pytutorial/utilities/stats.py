"""Small statistics helpers for demonstrating functions and collections."""

from typing import Iterable, List

from ..errors import EmptyDataError


def _as_list(values: Iterable[float]) -> List[float]:
    """Return iterable values as a list and reject empty input.

    Args:
        values: Numbers to convert into a list.

    Returns:
        A list containing the provided values.

    Raises:
        EmptyDataError: If ``values`` contains no items.
    """
    numbers = list(values)
    if not numbers:
        raise EmptyDataError("at least one value is required")
    return numbers


def average(values: Iterable[float]) -> float:
    """Return the arithmetic mean of the provided values.

    Args:
        values: Numbers to average.

    Returns:
        The arithmetic mean.

    Raises:
        EmptyDataError: If ``values`` contains no items.
    """
    numbers = _as_list(values)
    return sum(numbers) / len(numbers)


def median(values: Iterable[float]) -> float:
    """Return the median value after sorting the provided values.

    Args:
        values: Numbers to inspect.

    Returns:
        The middle value for odd-length input, or the midpoint of the two
        middle values for even-length input.

    Raises:
        EmptyDataError: If ``values`` contains no items.
    """
    numbers = sorted(_as_list(values))
    midpoint = len(numbers) // 2

    if len(numbers) % 2 == 1:
        return numbers[midpoint]

    return (numbers[midpoint - 1] + numbers[midpoint]) / 2


def passing_rate(scores: Iterable[float], passing_score: float = 70) -> float:
    """Return the fraction of scores that meet or exceed a passing score.

    Args:
        scores: Scores to evaluate.
        passing_score: Minimum score considered passing.

    Returns:
        A float from 0.0 to 1.0 representing the passing fraction.

    Raises:
        EmptyDataError: If ``scores`` contains no items.
    """
    numbers = _as_list(scores)
    passing = [score for score in numbers if score >= passing_score]
    return len(passing) / len(numbers)
