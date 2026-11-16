"""Bit Tricks."""

def single_number(nums: list[int]) -> int:
    """The value that appears once when every other appears twice."""
    x = 0
    for n in nums:
        x ^= n
    return x


def count_bits(n: int) -> int:
    """Number of set bits (Kernighan's trick)."""
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


def is_power_of_two(n: int) -> bool:
    return n > 0 and n & (n - 1) == 0
