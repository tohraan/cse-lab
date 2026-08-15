from cselab.rotate_matrix import rotate


def test_rotate_3x3():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(m)
    assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


def test_rotate_1x1_and_2x2():
    m = [[1]]
    rotate(m)
    assert m == [[1]]
    m = [[1, 2], [3, 4]]
    rotate(m)
    assert m == [[3, 1], [4, 2]]
