"""Min Stack."""

class MinStack:
    """Stack that returns its minimum in O(1)."""

    def __init__(self) -> None:
        self._s: list[tuple[int, int]] = []  # (value, min so far)

    def push(self, x: int) -> None:
        self._s.append((x, min(x, self._s[-1][1]) if self._s else x))

    def pop(self) -> int:
        return self._s.pop()[0]

    def top(self) -> int:
        return self._s[-1][0]

    def get_min(self) -> int:
        return self._s[-1][1]
