"""Ring Buffer."""

class RingBuffer:
    """Fixed-size buffer that overwrites the oldest item when full."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._buf: list = [None] * capacity
        self._start = 0
        self._len = 0

    def push(self, item) -> None:
        if self._len < self.capacity:
            self._buf[(self._start + self._len) % self.capacity] = item
            self._len += 1
        else:
            self._buf[self._start] = item
            self._start = (self._start + 1) % self.capacity

    def __len__(self) -> int:
        return self._len

    def to_list(self) -> list:
        return [self._buf[(self._start + i) % self.capacity] for i in range(self._len)]
