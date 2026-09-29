"""Level Order Traversal.

Topic: Trees (Medium).
Complexity: O(n) time and space.
"""

from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: "TreeNode | None") -> list[list[int]]:
    """Node values grouped by depth, left to right."""
    out: list[list[int]] = []
    q = deque([root] if root else [])
    while q:
        out.append([n.val for n in q])
        for _ in range(len(q)):
            n = q.popleft()
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
    return out
