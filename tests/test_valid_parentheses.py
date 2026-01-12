from cselab.valid_parentheses import is_valid


def test_valid():
    assert is_valid("()[]{}")
    assert is_valid("{[()]}")
    assert is_valid("")


def test_invalid():
    assert not is_valid("(]")
    assert not is_valid("(((")
    assert not is_valid("]")
