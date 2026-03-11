"""LRU Cache."""

from collections import OrderedDict

class LRUCache:
    """Fixed-capacity cache that evicts the least recently used key."""

    def __init__(self, capacity: int):
        raise NotImplementedError

    def get(self, key: int) -> int:
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError
