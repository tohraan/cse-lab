"""Permutations."""

def permutations(nums: list[int]) -> list[list[int]]:
    """All orderings of nums (distinct values)."""
    out: list[list[int]] = []

    def go(cur: list[int], used: list[bool]) -> None:
        if len(cur) == len(nums):
            out.append(cur[:])
            return
        for i, x in enumerate(nums):
            if not used[i]:
                used[i] = True
                cur.append(x)
                go(cur, used)
                cur.pop()
                used[i] = False

    go([], [False] * len(nums))
    return out
