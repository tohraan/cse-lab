"""Trie (Prefix Tree)."""

class Trie:

    def __init__(self) -> None:
        raise NotImplementedError

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def _walk(self, s: str):
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError

    def starts_with(self, prefix: str) -> bool:
        raise NotImplementedError
