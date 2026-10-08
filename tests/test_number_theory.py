from math import gcd as std_gcd

from cselab.number_theory import gcd, lcm, sieve


def test_sieve():
    assert sieve(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert sieve(1) == []
    assert len(sieve(10000)) == 1229


def test_gcd_lcm():
    for a, b in [(12, 18), (17, 5), (0, 9), (100, 75)]:
        assert gcd(a, b) == std_gcd(a, b)
    assert lcm(4, 6) == 12
    assert lcm(0, 5) == 0
