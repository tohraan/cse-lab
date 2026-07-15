"""Valid Anagram.

Topic: Hashing (Easy).
Complexity: O(n) time, O(1) space.
"""

from collections import Counter


def is_anagram(a: str, b: str) -> bool:
    """True if b is a rearrangement of a."""
    return Counter(a) == Counter(b)
