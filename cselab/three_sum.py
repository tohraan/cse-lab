"""3Sum."""

def three_sum(nums: list[int]) -> list[list[int]]:
    """All unique triplets that sum to zero."""
    nums = sorted(nums)
    out: list[list[int]] = []
    for i, a in enumerate(nums):
        if i and a == nums[i - 1]:
            continue
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            s = a + nums[lo] + nums[hi]
            if s < 0:
                lo += 1
            elif s > 0:
                hi -= 1
            else:
                out.append([a, nums[lo], nums[hi]])
                lo += 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
    return out
