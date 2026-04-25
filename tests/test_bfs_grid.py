from cselab.bfs_grid import shortest_path


def test_open_grid():
    assert shortest_path([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 4


def test_walls():
    assert shortest_path([[0, 1, 0], [0, 1, 0], [0, 0, 0]]) == 4
    assert shortest_path([[0, 1], [1, 0]]) == -1
    assert shortest_path([[1]]) == -1
    assert shortest_path([[0]]) == 0
