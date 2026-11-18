"""Group Anagrams."""

def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams of each other."""
    groups: dict[str, list[str]] = {}
    for w in words:
        groups.setdefault("".join(sorted(w)), []).append(w)
    return list(groups.values())
