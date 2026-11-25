"""Running Median.

Topic: Heap (Hard).
Complexity: O(log n) add, O(1) median.
"""

import heapq


class MedianFinder:
    """Median of a stream using a max-heap (lower half) and a min-heap (upper half)."""

    def __init__(self) -> None:
        self._lo: list[int] = []  # max-heap via negation
        self._hi: list[int] = []

    def add(self, x: int) -> None:
        heapq.heappush(self._lo, -x)
        heapq.heappush(self._hi, -heapq.heappop(self._lo))
        if len(self._hi) > len(self._lo):
            heapq.heappush(self._lo, -heapq.heappop(self._hi))

    def median(self) -> float:
        if len(self._lo) > len(self._hi):
            return float(-self._lo[0])
        return (-self._lo[0] + self._hi[0]) / 2
