from pytree.pytree import AVLTree


def test_update_height():
    tree = AVLTree()
    tree.root = AVLTree.insert(tree.root, 4)
    assert tree.root.height == 1
    tree.root = AVLTree.insert(tree.root, 3)
    assert tree.root.height == 2
    tree.root = AVLTree.insert(tree.root, 2)
    assert tree.root.height == 2
    tree.root = AVLTree.insert(tree.root, 1)
    assert tree.root.height == 3


def test_get_height():
    tree = AVLTree()
    for i in range(7):
        tree.root = AVLTree.insert(tree.root, i + 1)
    assert AVLTree.get_height(tree.root) == 3
    assert AVLTree.get_height(tree.root.left) == 2
    assert AVLTree.get_height(tree.root.right) == 2
    assert AVLTree.get_height(tree.root.left.left) == 1
    assert AVLTree.get_height(tree.root.left.right) == 1
    assert AVLTree.get_height(tree.root.right.left) == 1
    assert AVLTree.get_height(tree.root.right.right) == 1


def test_get_balance():
    tree = AVLTree()
    tree.root = AVLTree.insert(tree.root, 1)
    tree.root = AVLTree.insert(tree.root, 2)
    assert AVLTree.get_balance(tree.root) == 1
    tree = AVLTree()
    tree.root = AVLTree.insert(tree.root, 2)
    tree.root = AVLTree.insert(tree.root, 1)
    assert AVLTree.get_balance(tree.root) == -1


def test_insert():
    tree = AVLTree()
    tree.root = AVLTree.insert(tree.root, 1)
    tree.root = AVLTree.insert(tree.root, 2)
    tree.root = AVLTree.insert(tree.root, 3)
    tree.root = AVLTree.insert(tree.root, 4)
    tree.root = AVLTree.insert(tree.root, 5)
    tree.root = AVLTree.insert(tree.root, 6)
    tree.root = AVLTree.insert(tree.root, 7)
    assert str(tree.root) == "[[1, 2, 3], 4, [5, 6, 7]]"


def test_left_right():
    tree = AVLTree()
    tree.root = AVLTree.insert(tree.root, 4)
    tree.root = AVLTree.insert(tree.root, 1)
    tree.root = AVLTree.insert(tree.root, 2)
    tree.root = AVLTree.insert(tree.root, 3)
    assert str(tree.root) == "[1, 2, [3, 4, ]]"


def test_right_left():
    tree = AVLTree()
    tree.root = AVLTree.insert(tree.root, 1)
    tree.root = AVLTree.insert(tree.root, 4)
    tree.root = AVLTree.insert(tree.root, 3)
    tree.root = AVLTree.insert(tree.root, 2)
    assert str(tree.root) == "[[, 1, 2], 3, 4]"


def test_right_right():
    tree = AVLTree()
    tree.root = AVLTree.insert(tree.root, 1)
    tree.root = AVLTree.insert(tree.root, 2)
    tree.root = AVLTree.insert(tree.root, 3)
    tree.root = AVLTree.insert(tree.root, 4)
    assert str(tree.root) == "[1, 2, [, 3, 4]]"


def test_left_left():
    tree = AVLTree()
    tree.root = AVLTree.insert(tree.root, 4)
    tree.root = AVLTree.insert(tree.root, 3)
    tree.root = AVLTree.insert(tree.root, 2)
    tree.root = AVLTree.insert(tree.root, 1)
    assert str(tree.root) == "[[1, 2, ], 3, 4]"
