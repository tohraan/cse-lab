import random
import statistics

from cselab.median_finder import MedianFinder


def test_stream_matches_statistics():
    rng = random.Random(3)
    m, seen = MedianFinder(), []
    for _ in range(200):
        x = rng.randint(-100, 100)
        m.add(x)
        seen.append(x)
        assert m.median() == statistics.median(seen)
