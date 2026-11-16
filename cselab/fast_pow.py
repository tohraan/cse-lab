"""Fast Modular Exponentiation.

Topic: Math (Medium).
Complexity: O(log exp) time.
"""

def pow_mod(base: int, exp: int, mod: int) -> int:
    """base ** exp % mod by repeated squaring."""
    result = 1
    base %= mod
    while exp:
        if exp & 1:
            result = result * base % mod
        base = base * base % mod
        exp >>= 1
    return result % mod
