from cselab.valid_anagram import is_anagram


def test_anagram():
    assert is_anagram("listen", "silent")
    assert not is_anagram("rat", "car")
    assert not is_anagram("aab", "abb")
    assert is_anagram("", "")
