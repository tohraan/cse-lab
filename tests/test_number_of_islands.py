from cselab.number_of_islands import num_islands


def test_islands():
    g = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert num_islands(g) == 3


def test_empty_and_water():
    assert num_islands([]) == 0
    assert num_islands([list("000")]) == 0
