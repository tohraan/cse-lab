"""N-Queens (count).

Topic: Backtracking (Hard).
Complexity: O(n!) time worst case.
"""

def total_n_queens(n: int) -> int:
    """Number of ways to place n non-attacking queens on an n x n board."""
    cols: set[int] = set()
    diag1: set[int] = set()
    diag2: set[int] = set()

    def place(r: int) -> int:
        if r == n:
            return 1
        total = 0
        for c in range(n):
            if c in cols or r - c in diag1 or r + c in diag2:
                continue
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            total += place(r + 1)
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)
        return total

    return place(0)
