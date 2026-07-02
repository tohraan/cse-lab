"""Kth Largest Element.

Topic: Heap (Medium).
Complexity: O(n log k) time, O(k) space.
"""

import heapq


def kth_largest(nums: list[int], k: int) -> int:
    """The k-th largest value (1-based) using a size-k min-heap."""
    heap = nums[:k]
    heapq.heapify(heap)
    for x in nums[k:]:
        if x > heap[0]:
            heapq.heapreplace(heap, x)
    return heap[0]
