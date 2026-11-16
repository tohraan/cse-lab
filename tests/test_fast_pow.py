from cselab.fast_pow import pow_mod


def test_matches_builtin():
    for b, e, m in [(2, 10, 1000), (7, 0, 13), (3, 200, 1_000_000_007), (10, 18, 7)]:
        assert pow_mod(b, e, m) == pow(b, e, m)


def test_mod_one():
    assert pow_mod(5, 3, 1) == 0
