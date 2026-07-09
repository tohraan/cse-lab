"""Top K Frequent Elements.

Topic: Hashing (Medium).
Complexity: O(n) time with bucket sort.
"""

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """The k most frequent values (bucket sort by frequency)."""
    freq: dict[int, int] = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1
    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for x, f in freq.items():
        buckets[f].append(x)
    out: list[int] = []
    for f in range(len(nums), 0, -1):
        for x in buckets[f]:
            out.append(x)
            if len(out) == k:
                return out
    return out
