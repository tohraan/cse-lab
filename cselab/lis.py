"""Longest Increasing Subsequence.

Topic: Dynamic Programming (Medium).
Complexity: O(n log n) time, O(n) space.
"""

from bisect import bisect_left


def lis_length(nums: list[int]) -> int:
    """Length of the longest strictly increasing subsequence (patience sorting)."""
    tails: list[int] = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
