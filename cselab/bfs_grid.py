"""Shortest Path in a Grid (BFS)."""

from collections import deque


def shortest_path(grid: list[list[int]]) -> int:
    """Steps from top-left to bottom-right through 0-cells (4-directional), or -1."""
    if not grid or grid[0][0] or grid[-1][-1]:
        return -1
    rows, cols = len(grid), len(grid[0])
    q = deque([(0, 0, 0)])
    seen = {(0, 0)}
    while q:
        r, c, d = q.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return d
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols and not grid[nr][nc] and (nr, nc) not in seen:
                seen.add((nr, nc))
                q.append((nr, nc, d + 1))
    return -1
