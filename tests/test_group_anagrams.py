from cselab.group_anagrams import group_anagrams


def test_groups():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(sorted(g) for g in result) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]


def test_empty():
    assert group_anagrams([]) == []
