"""Running Median."""

import heapq

class MedianFinder:
    """Median of a stream using a max-heap (lower half) and a min-heap (upper half)."""

    def __init__(self) -> None:
        raise NotImplementedError

    def add(self, x: int) -> None:
        raise NotImplementedError

    def median(self) -> float:
        raise NotImplementedError
