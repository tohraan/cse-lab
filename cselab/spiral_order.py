"""Spiral Matrix.

Topic: Matrix (Medium).
Complexity: O(m * n) time.
"""

def spiral_order(matrix: list[list[int]]) -> list[int]:
    """Elements of the matrix in clockwise spiral order."""
    out: list[int] = []
    if not matrix:
        return out
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        out.extend(matrix[top][left:right + 1])
        out.extend(matrix[r][right] for r in range(top + 1, bottom + 1))
        if top < bottom:
            out.extend(reversed(matrix[bottom][left:right]))
        if left < right:
            out.extend(matrix[r][left] for r in range(bottom - 1, top, -1))
        top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
    return out
