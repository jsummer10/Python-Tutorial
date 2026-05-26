"""Text helpers for demonstrating strings, dictionaries, and lists."""

import re
from typing import Dict, List


def normalize_whitespace(text: str) -> str:
    """Collapse repeated whitespace and trim leading or trailing space.

    Args:
        text: Text to normalize.

    Returns:
        Text with single spaces between words and no leading or trailing space.
    """
    return " ".join(text.split())


def slugify(text: str) -> str:
    """Convert text into a simple lowercase URL slug.

    Args:
        text: Text to convert.

    Returns:
        A lowercase slug containing letters, numbers, and hyphens.
    """
    normalized = normalize_whitespace(text).lower()
    slug = re.sub(r"[^a-z0-9]+", "-", normalized)
    return slug.strip("-")


def word_count(text: str) -> Dict[str, int]:
    """Return a case-insensitive count of words in text.

    Args:
        text: Text to count.

    Returns:
        A dictionary mapping each lowercase word to its occurrence count.
    """
    words = re.findall(r"[a-z0-9']+", text.lower())
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_words(text: str, limit: int = 3) -> List[str]:
    """Return the most common words, sorted by count then alphabetically.

    Args:
        text: Text to inspect.
        limit: Maximum number of words to return.

    Returns:
        A list of the highest-ranked words.
    """
    counts = word_count(text)
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return [word for word, _count in ranked[:limit]]
