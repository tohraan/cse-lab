from cselab.top_k_frequent import top_k_frequent


def test_top_k():
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert top_k_frequent([4, 4, 4, 5, 5, 6], 1) == [4]
