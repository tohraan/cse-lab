"""Dijkstra Shortest Paths."""

import heapq


def dijkstra(graph: dict[int, list[tuple[int, int]]], src: int) -> dict[int, int]:
    """Shortest distance from src to every reachable node (non-negative weights)."""
    dist = {src: 0}
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, float("inf")):
            continue
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist
