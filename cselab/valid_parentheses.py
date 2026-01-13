"""Valid Parentheses.

Topic: Stack (Easy).
Complexity: O(n) time, O(n) space.
"""

def is_valid(s: str) -> bool:
    """True if every bracket in s is closed in the right order."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        elif ch in "([{":
            stack.append(ch)
    return not stack
