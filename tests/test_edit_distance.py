from cselab.edit_distance import edit_distance


def test_known():
    assert edit_distance("horse", "ros") == 3
    assert edit_distance("intention", "execution") == 5


def test_edges():
    assert edit_distance("", "abc") == 3
    assert edit_distance("abc", "") == 3
    assert edit_distance("same", "same") == 0
