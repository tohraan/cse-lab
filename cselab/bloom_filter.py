"""Bloom Filter.

Topic: Systems (Medium).
Complexity: O(k) per operation, no false negatives.
"""

import hashlib


class BloomFilter:
    """Probabilistic set: may report false positives, never false negatives."""

    def __init__(self, size_bits: int = 8192, hashes: int = 3):
        self.size = size_bits
        self.hashes = hashes
        self._bits = bytearray(size_bits)

    def _positions(self, item: str):
        for i in range(self.hashes):
            digest = hashlib.sha256(f"{i}:{item}".encode()).digest()
            yield int.from_bytes(digest[:8], "big") % self.size

    def add(self, item: str) -> None:
        for p in self._positions(item):
            self._bits[p] = 1

    def might_contain(self, item: str) -> bool:
        return all(self._bits[p] for p in self._positions(item))
