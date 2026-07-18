"""Longest Substring Without Repeats.

Topic: Sliding Window (Medium).
Complexity: O(n) time, O(k) space.
"""

def longest_unique_substring(s: str) -> int:
    """Length of the longest substring with all distinct characters."""
    last: dict[str, int] = {}
    start = best = 0
    for i, ch in enumerate(s):
        if ch in last and last[ch] >= start:
            start = last[ch] + 1
        last[ch] = i
        best = max(best, i - start + 1)
    return best
