from cselab.union_find import UnionFind


def test_union_and_components():
    u = UnionFind(5)
    assert u.union(0, 1)
    assert u.union(1, 2)
    assert not u.union(0, 2)
    assert u.connected(0, 2)
    assert not u.connected(0, 4)
    assert u.components == 3
