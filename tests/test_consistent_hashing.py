from cselab.consistent_hashing import ConsistentHashRing


def test_deterministic_and_balanced():
    ring = ConsistentHashRing(["a", "b", "c"])
    keys = [f"key{i}" for i in range(3000)]
    assert [ring.get_node(k) for k in keys] == [ring.get_node(k) for k in keys]
    counts = {n: 0 for n in "abc"}
    for k in keys:
        counts[ring.get_node(k)] += 1
    assert all(500 < c < 1600 for c in counts.values())


def test_removal_only_moves_that_nodes_keys():
    ring = ConsistentHashRing(["a", "b", "c"])
    keys = [f"key{i}" for i in range(2000)]
    before = {k: ring.get_node(k) for k in keys}
    ring.remove_node("b")
    for k in keys:
        if before[k] != "b":
            assert ring.get_node(k) == before[k]
        else:
            assert ring.get_node(k) in ("a", "c")
