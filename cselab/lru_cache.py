"""LRU Cache."""

from collections import OrderedDict


class LRUCache:
    """Fixed-capacity cache that evicts the least recently used key."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._d: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self._d:
            return -1
        self._d.move_to_end(key)
        return self._d[key]

    def put(self, key: int, value: int) -> None:
        if key in self._d:
            self._d.move_to_end(key)
        self._d[key] = value
        if len(self._d) > self.capacity:
            self._d.popitem(last=False)
