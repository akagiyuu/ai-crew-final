from data_structure.binary_tree import BinaryTree


def test_vec_dequeue():
    tree = BinaryTree()
    for item in [8, 3, 6, 1, 10, 14, 13, 4, 7]:
        tree.insert(item)

    assert str(tree) == "[1, 3, 4, 6, 7, 8, 10, 13, 14]"
    assert (8 in tree) is True
    assert (100 in tree) is False
    assert tree.depth() == 4

    assert list(tree.inorder_traversal()) == [1, 3, 4, 6, 7, 8, 10, 13, 14]
    assert list(tree.preorder_traversal()) == [8, 3, 1, 6, 4, 7, 10, 14, 13]
    assert list(tree.postorder_traversal()) == [1, 4, 7, 6, 3, 13, 14, 10, 8]
