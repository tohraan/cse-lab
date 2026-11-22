"""KMP String Search."""

def kmp_search(text: str, pattern: str) -> list[int]:
    """Start index of every occurrence of pattern in text (empty pattern -> [])."""
    if not pattern:
        return []
    fail = [0] * len(pattern)
    k = 0
    for i in range(1, len(pattern)):
        while k and pattern[i] != pattern[k]:
            k = fail[k - 1]
        if pattern[i] == pattern[k]:
            k += 1
        fail[i] = k
    out: list[int] = []
    k = 0
    for i, ch in enumerate(text):
        while k and ch != pattern[k]:
            k = fail[k - 1]
        if ch == pattern[k]:
            k += 1
        if k == len(pattern):
            out.append(i - k + 1)
            k = fail[k - 1]
    return out
