from cselab.lru_cache import LRUCache


def test_eviction_order():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)  # evicts 2
    assert c.get(2) == -1
    assert c.get(3) == 3


def test_update_refreshes():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    c.put(1, 10)
    c.put(3, 3)  # evicts 2, not 1
    assert c.get(1) == 10
    assert c.get(2) == -1
