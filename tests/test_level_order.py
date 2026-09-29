from cselab.level_order import TreeNode, level_order


def test_levels():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(root) == [[3], [9, 20], [15, 7]]


def test_empty():
    assert level_order(None) == []
