from cselab.first_missing_positive import first_missing_positive


def test_cases():
    assert first_missing_positive([1, 2, 0]) == 3
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1
    assert first_missing_positive([]) == 1
    assert first_missing_positive([1, 1]) == 2
