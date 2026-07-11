"""Valid Anagram."""

from collections import Counter


def is_anagram(a: str, b: str) -> bool:
    """True if b is a rearrangement of a."""
    return Counter(a) == Counter(b)
