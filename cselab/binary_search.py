"""Binary Search & Lower Bound.

Topic: Searching (Easy).
Complexity: O(log n) time, O(1) space.
"""

def binary_search(a: list[int], target: int) -> int:
    """Index of target in sorted a, or -1."""
    i = lower_bound(a, target)
    return i if i < len(a) and a[i] == target else -1


def lower_bound(a: list[int], target: int) -> int:
    """First index whose value is >= target (len(a) if none)."""
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
