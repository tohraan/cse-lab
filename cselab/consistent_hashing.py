"""Consistent Hashing Ring.

Topic: Systems (Hard).
Complexity: O(log n) lookup.
"""

import bisect
import hashlib


def _h(s: str) -> int:
    return int.from_bytes(hashlib.md5(s.encode()).digest()[:8], "big")


class ConsistentHashRing:
    """Maps keys to nodes so adding/removing a node only moves ~1/n of the keys."""

    def __init__(self, nodes: list[str], replicas: int = 100):
        self.replicas = replicas
        self._ring: list[int] = []
        self._owner: dict[int, str] = {}
        for n in nodes:
            self.add_node(n)

    def add_node(self, node: str) -> None:
        for i in range(self.replicas):
            h = _h(f"{node}#{i}")
            bisect.insort(self._ring, h)
            self._owner[h] = node

    def remove_node(self, node: str) -> None:
        for i in range(self.replicas):
            h = _h(f"{node}#{i}")
            self._ring.remove(h)
            del self._owner[h]

    def get_node(self, key: str) -> str:
        i = bisect.bisect(self._ring, _h(key)) % len(self._ring)
        return self._owner[self._ring[i]]
