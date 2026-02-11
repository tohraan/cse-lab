from cselab.reverse_linked_list import from_list, reverse_list, to_list


def test_reverse():
    assert to_list(reverse_list(from_list([1, 2, 3, 4]))) == [4, 3, 2, 1]


def test_edges():
    assert reverse_list(None) is None
    assert to_list(reverse_list(from_list([7]))) == [7]
