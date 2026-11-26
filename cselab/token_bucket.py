"""Token Bucket Rate Limiter.

Topic: Systems (Medium).
Complexity: O(1) per request.
"""

import time
from typing import Callable


class TokenBucket:
    """Allows bursts up to capacity, refilling at `rate` tokens per second."""

    def __init__(self, capacity: float, rate: float, clock: Callable[[], float] = time.monotonic):
        self.capacity = capacity
        self.rate = rate
        self._clock = clock
        self._tokens = capacity
        self._last = clock()

    def allow(self, cost: float = 1.0) -> bool:
        now = self._clock()
        self._tokens = min(self.capacity, self._tokens + (now - self._last) * self.rate)
        self._last = now
        if self._tokens >= cost:
            self._tokens -= cost
            return True
        return False
