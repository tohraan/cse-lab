"""Container With Most Water.

Topic: Two Pointers (Medium).
Complexity: O(n) time, O(1) space.
"""

def max_area(height: list[int]) -> int:
    """Largest water area between two lines, moving the shorter side inward."""
    lo, hi, best = 0, len(height) - 1, 0
    while lo < hi:
        best = max(best, (hi - lo) * min(height[lo], height[hi]))
        if height[lo] < height[hi]:
            lo += 1
        else:
            hi -= 1
    return best
