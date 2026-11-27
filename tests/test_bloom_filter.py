from cselab.bloom_filter import BloomFilter


def test_no_false_negatives():
    bf = BloomFilter(10_000, 3)
    items = [f"user:{i}" for i in range(200)]
    for it in items:
        bf.add(it)
    assert all(bf.might_contain(it) for it in items)


def test_low_false_positive_rate():
    bf = BloomFilter(10_000, 3)
    for i in range(200):
        bf.add(f"user:{i}")
    false_pos = sum(bf.might_contain(f"other:{i}") for i in range(1000))
    assert false_pos < 30
