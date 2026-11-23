from cselab.kmp_search import kmp_search


def test_search():
    assert kmp_search("abababca", "abab") == [0, 2]
    assert kmp_search("aaaaa", "aa") == [0, 1, 2, 3]
    assert kmp_search("hello", "xyz") == []
    assert kmp_search("hello", "") == []
