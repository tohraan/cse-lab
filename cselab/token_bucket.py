"""Token Bucket Rate Limiter."""

import time
from typing import Callable

class TokenBucket:
    """Allows bursts up to capacity, refilling at `rate` tokens per second."""

    def __init__(self, capacity: float, rate: float, clock: Callable[[], float]=time.monotonic):
        raise NotImplementedError

    def allow(self, cost: float=1.0) -> bool:
        raise NotImplementedError
