from itertools import permutations as std

from cselab.permutations import permutations


def test_matches_itertools():
    assert permutations([1, 2, 3]) == [list(p) for p in std([1, 2, 3])]


def test_edges():
    assert permutations([]) == [[]]
    assert permutations([9]) == [[9]]
