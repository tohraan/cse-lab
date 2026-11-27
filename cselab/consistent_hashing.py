"""Consistent Hashing Ring."""

import bisect
import hashlib

def _h(s: str) -> int:
    raise NotImplementedError

class ConsistentHashRing:
    """Maps keys to nodes so adding/removing a node only moves ~1/n of the keys."""

    def __init__(self, nodes: list[str], replicas: int=100):
        raise NotImplementedError

    def add_node(self, node: str) -> None:
        raise NotImplementedError

    def remove_node(self, node: str) -> None:
        raise NotImplementedError

    def get_node(self, key: str) -> str:
        raise NotImplementedError
