"""Climbing Stairs.

Topic: Dynamic Programming (Easy).
Complexity: O(n) time, O(1) space.
"""

def climb_stairs(n: int) -> int:
    """Distinct ways to climb n steps taking 1 or 2 at a time."""
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
