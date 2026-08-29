from cselab.subsets import subsets


def test_power_set():
    result = subsets([1, 2, 3])
    assert len(result) == 8
    assert sorted(map(tuple, result)) == sorted([(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)])


def test_empty():
    assert subsets([]) == [[]]
