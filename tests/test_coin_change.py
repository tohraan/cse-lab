from cselab.coin_change import coin_change


def test_basic():
    assert coin_change([1, 2, 5], 11) == 3


def test_impossible():
    assert coin_change([2], 3) == -1


def test_zero():
    assert coin_change([1], 0) == 0


def test_greedy_fails():
    assert coin_change([1, 3, 4], 6) == 2
