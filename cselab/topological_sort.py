"""Topological Sort (Kahn)."""

from collections import deque


def topological_sort(n: int, edges: list[tuple[int, int]]) -> list[int]:
    """Order of nodes 0..n-1 where every edge u->v has u before v; [] if cyclic."""
    adj: list[list[int]] = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order: list[int] = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []
