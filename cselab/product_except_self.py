"""Product of Array Except Self.

Topic: Arrays (Medium).
Complexity: O(n) time, O(1) extra space.
"""

def product_except_self(nums: list[int]) -> list[int]:
    """out[i] is the product of every element except nums[i], without division."""
    n = len(nums)
    out = [1] * n
    left = 1
    for i in range(n):
        out[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        out[i] *= right
        right *= nums[i]
    return out
