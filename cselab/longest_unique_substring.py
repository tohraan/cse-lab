"""Longest Substring Without Repeats."""

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
