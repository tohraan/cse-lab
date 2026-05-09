"""Longest Common Subsequence.

Topic: Dynamic Programming (Medium).
Complexity: O(m * n) time, O(n) space.
"""

def lcs_length(a: str, b: str) -> int:
    """Length of the longest common subsequence of a and b."""
    prev = [0] * (len(b) + 1)
    for ch in a:
        cur = [0]
        for j, other in enumerate(b, 1):
            cur.append(prev[j - 1] + 1 if ch == other else max(prev[j], cur[j - 1]))
        prev = cur
    return prev[-1]
