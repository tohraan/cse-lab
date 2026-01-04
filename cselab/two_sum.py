"""Two Sum.

Topic: Hashing (Easy).
Complexity: O(n) time, O(n) space.
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of the two numbers that add up to target, or []."""
    seen: dict[int, int] = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
