"""Level Order Traversal."""

from collections import deque

class TreeNode:

    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        raise NotImplementedError

def level_order(root: 'TreeNode | None') -> list[list[int]]:
    """Node values grouped by depth, left to right."""
    raise NotImplementedError
