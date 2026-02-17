"""Maximum Subarray (Kadane).

Topic: Dynamic Programming (Medium).
Complexity: O(n) time, O(1) space.
"""

def max_subarray(nums: list[int]) -> int:
    """Largest sum of a non-empty contiguous subarray."""
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
