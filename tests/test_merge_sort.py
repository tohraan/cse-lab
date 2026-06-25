import random

from cselab.merge_sort import merge_sort


def test_sorted_matches_builtin():
    rng = random.Random(7)
    for _ in range(50):
        a = [rng.randint(-50, 50) for _ in range(rng.randint(0, 40))]
        assert merge_sort(a) == sorted(a)


def test_does_not_mutate():
    a = [3, 1, 2]
    merge_sort(a)
    assert a == [3, 1, 2]
