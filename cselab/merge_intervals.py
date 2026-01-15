"""Merge Intervals.

Topic: Sorting (Medium).
Complexity: O(n log n) time, O(n) space.
"""

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merge all overlapping closed intervals."""
    out: list[list[int]] = []
    for start, end in sorted(intervals):
        if out and start <= out[-1][1]:
            out[-1][1] = max(out[-1][1], end)
        else:
            out.append([start, end])
    return out
