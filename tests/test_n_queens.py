from cselab.n_queens import total_n_queens


def test_known_counts():
    assert [total_n_queens(n) for n in range(1, 9)] == [1, 0, 0, 2, 10, 4, 40, 92]
