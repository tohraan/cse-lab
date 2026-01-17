from cselab.binary_search import binary_search, lower_bound


def test_found_and_missing():
    a = [1, 3, 5, 7, 9]
    assert binary_search(a, 7) == 3
    assert binary_search(a, 4) == -1
    assert binary_search([], 1) == -1


def test_lower_bound_duplicates():
    assert lower_bound([1, 2, 2, 2, 3], 2) == 1
    assert lower_bound([1, 2, 3], 10) == 3
    assert lower_bound([1, 2, 3], 0) == 0
