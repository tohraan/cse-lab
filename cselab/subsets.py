"""Subsets."""

def subsets(nums: list[int]) -> list[list[int]]:
    """The power set of nums."""
    out: list[list[int]] = [[]]
    for x in nums:
        out += [s + [x] for s in out]
    return out
