from cselab.inorder_traversal import TreeNode, inorder


def test_inorder():
    root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(2.5), None))
    assert inorder(root) == [1, 2, 2.5, 3]


def test_empty_and_deep():
    assert inorder(None) == []
    node = None
    for i in range(5000):  # would blow the recursion limit if recursive
        node = TreeNode(i, node, None)
    assert len(inorder(node)) == 5000
