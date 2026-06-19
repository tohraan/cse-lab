from cselab.knapsack import knapsack


def test_classic():
    assert knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9


def test_edges():
    assert knapsack([5], [10], 4) == 0
    assert knapsack([], [], 10) == 0
    assert knapsack([2, 2], [3, 3], 3) == 3
