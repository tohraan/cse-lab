from cselab.min_stack import MinStack


def test_min_tracks_pops():
    s = MinStack()
    for x in (5, 3, 7, 3, 1):
        s.push(x)
    assert s.get_min() == 1
    s.pop()
    assert s.get_min() == 3
    s.pop()
    s.pop()
    assert s.get_min() == 3
    assert s.top() == 3
    s.pop()
    assert s.get_min() == 5
