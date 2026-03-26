"""Union-Find (DSU)."""

class UnionFind:
    """Disjoint sets with path compression and union by size."""

    def __init__(self, n: int):
        raise NotImplementedError

    def find(self, x: int) -> int:
        raise NotImplementedError

    def union(self, a: int, b: int) -> bool:
        raise NotImplementedError

    def connected(self, a: int, b: int) -> bool:
        raise NotImplementedError
