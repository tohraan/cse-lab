from cselab.merge_intervals import merge_intervals


def test_overlap():
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_touching():
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]


def test_unsorted_and_empty():
    assert merge_intervals([[5, 6], [1, 2]]) == [[1, 2], [5, 6]]
    assert merge_intervals([]) == []
