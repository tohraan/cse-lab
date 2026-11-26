from cselab.token_bucket import TokenBucket


class FakeClock:
    def __init__(self):
        self.t = 0.0

    def __call__(self):
        return self.t


def test_burst_then_refill():
    clock = FakeClock()
    b = TokenBucket(capacity=3, rate=1, clock=clock)
    assert [b.allow() for _ in range(4)] == [True, True, True, False]
    clock.t = 2.0
    assert [b.allow() for _ in range(3)] == [True, True, False]


def test_never_exceeds_capacity():
    clock = FakeClock()
    b = TokenBucket(capacity=2, rate=10, clock=clock)
    clock.t = 100.0
    assert [b.allow() for _ in range(3)] == [True, True, False]
