from cselab.bit_tricks import count_bits, is_power_of_two, single_number


def test_single_number():
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([7]) == 7


def test_count_bits():
    assert [count_bits(n) for n in (0, 1, 7, 8, 255)] == [0, 1, 3, 1, 8]


def test_power_of_two():
    assert is_power_of_two(1) and is_power_of_two(1024)
    assert not is_power_of_two(0) and not is_power_of_two(6) and not is_power_of_two(-4)
