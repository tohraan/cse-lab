"""Rotate Image.

Topic: Matrix (Medium).
Complexity: O(n^2) time, O(1) space.
"""

def rotate(matrix: list[list[int]]) -> None:
    """Rotate an n x n matrix 90 degrees clockwise, in place."""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
