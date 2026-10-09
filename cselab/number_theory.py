"""Sieve, GCD and LCM.

Topic: Math (Easy).
Complexity: Sieve O(n log log n); GCD O(log n).
"""

def sieve(n: int) -> list[int]:
    """All primes <= n (sieve of Eratosthenes)."""
    if n < 2:
        return []
    is_p = bytearray([1]) * (n + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if is_p[i]:
            is_p[i * i::i] = bytearray(len(is_p[i * i::i]))
    return [i for i, p in enumerate(is_p) if p]


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b) if a and b else 0
