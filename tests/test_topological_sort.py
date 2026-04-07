from cselab.topological_sort import topological_sort


def test_order_respects_edges():
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    order = topological_sort(6, edges)
    assert sorted(order) == list(range(6))
    pos = {v: i for i, v in enumerate(order)}
    assert all(pos[u] < pos[v] for u, v in edges)


def test_cycle():
    assert topological_sort(3, [(0, 1), (1, 2), (2, 0)]) == []
