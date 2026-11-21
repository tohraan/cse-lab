"""Word Break."""

def word_break(s: str, words: list[str]) -> bool:
    """True if s can be segmented into dictionary words."""
    dictionary = set(words)
    ok = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        ok[i] = any(ok[j] and s[j:i] in dictionary for j in range(i))
    return ok[len(s)]
