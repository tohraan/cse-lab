"""Bloom Filter."""

import hashlib

class BloomFilter:
    """Probabilistic set: may report false positives, never false negatives."""

    def __init__(self, size_bits: int=8192, hashes: int=3):
        raise NotImplementedError

    def _positions(self, item: str):
        raise NotImplementedError

    def add(self, item: str) -> None:
        raise NotImplementedError

    def might_contain(self, item: str) -> bool:
        raise NotImplementedError
