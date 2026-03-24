"""Trie (Prefix Tree)."""

class Trie:
    def __init__(self) -> None:
        self._root: dict = {}

    def insert(self, word: str) -> None:
        node = self._root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def _walk(self, s: str):
        node = self._root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return bool(node and "$" in node)

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None
