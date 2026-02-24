from cselab.climbing_stairs import climb_stairs


def test_small():
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8


def test_zero_and_large():
    assert climb_stairs(0) == 1
    assert climb_stairs(45) == 1836311903
