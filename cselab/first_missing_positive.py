"""First Missing Positive."""

def first_missing_positive(nums: list[int]) -> int:
    """Smallest positive integer not in nums (cyclic placement, mutates a copy)."""
    a = list(nums)
    n = len(a)
    for i in range(n):
        while 1 <= a[i] <= n and a[a[i] - 1] != a[i]:
            j = a[i] - 1
            a[i], a[j] = a[j], a[i]
    for i, x in enumerate(a):
        if x != i + 1:
            return i + 1
    return n + 1
