"""Binary Tree Inorder (iterative).

Topic: Trees (Easy).
Complexity: O(n) time, O(h) space.
"""

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: "TreeNode | None") -> list[int]:
    """Left, node, right - with an explicit stack instead of recursion."""
    out: list[int] = []
    stack: list[TreeNode] = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        out.append(node.val)
        node = node.right
    return out
