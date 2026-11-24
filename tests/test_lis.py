from cselab.lis import lis_length


def test_lis():
    assert lis_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lis_length([0, 1, 0, 3, 2, 3]) == 4
    assert lis_length([7, 7, 7]) == 1
    assert lis_length([]) == 0
