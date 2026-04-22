from cselab.dijkstra import dijkstra


def test_shortest_paths():
    g = {0: [(1, 4), (2, 1)], 2: [(1, 2), (3, 7)], 1: [(3, 1)]}
    assert dijkstra(g, 0) == {0: 0, 2: 1, 1: 3, 3: 4}


def test_unreachable_omitted():
    assert dijkstra({0: [(1, 1)], 5: [(6, 1)]}, 0) == {0: 0, 1: 1}
