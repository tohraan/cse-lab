"""Ring Buffer."""

class RingBuffer:
    """Fixed-size buffer that overwrites the oldest item when full."""

    def __init__(self, capacity: int):
        raise NotImplementedError

    def push(self, item) -> None:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def to_list(self) -> list:
        raise NotImplementedError
