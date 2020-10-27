from pytree.pytree import AVLTree


def test_update_height():
    """
    Test to make sure the height is being updated correctly:
    Height = 3:       4
                    /   \
    Height = 2:   2       5
                 / \\    / \
    Height = 1: 1   3   6   7
    """
    tree = AVLTree()
    tree.insert_array([1, 2, 3, 4, 5, 6, 7])
    assert tree.root.height == 3
    assert tree.root.left.height == 2
    assert tree.root.right.height == 2
    assert tree.root.left.left.height == 1
    assert tree.root.left.right.height == 1
    assert tree.root.right.left.height == 1
    assert tree.root.right.right.height == 1


def test_get_balance():
    """
    Test to make sure the balance is being calculated correctly:
    Tree 1, balance on root is 0:
      2
    Tree 2, balance on root is -1:
      2
     /
    1
    Tree 3, balance on root is 0:
      2
     / \
    1   3
    Tree 4, balance on root is 1:
      2
     / \
    1   3
         \
          4
    """
    tree = AVLTree()
    tree.insert(2)
    assert tree._get_balance(tree.root) == 0
    tree.insert(1)
    assert tree._get_balance(tree.root) == -1
    tree.insert(3)
    assert tree._get_balance(tree.root) == 0
    tree.insert(4)
    assert tree._get_balance(tree.root) == 1


def test_insert():
    """
    Test inserting the following tree:
          4
        /   \
      2       5
     / \\    / \
    1   3   6   7
    """
    tree = AVLTree()
    tree.insert(1).insert(2).insert(3).insert(4).insert(5).insert(6).insert(7)
    assert str(tree.root) == "[[1, 2, 3], 4, [5, 6, 7]]"


def test_delete():
    """
    Test deleting [4, ] from the following tree:
          4
        /   \
      2       5
     / \\    / \
    1   3   6   7
                 \
                  8
    Test deleting [1, 3] from the following tree:
          6
        /   \
      4       7
     / \\      \
    2   5       8
    Test deleting [7, 8] from the following tree:
       4
     /  \
    2    6
        /
       5
    Test deleting 4 from the following tree:
       5
     /  \
    2    6
    """
    tree = AVLTree()
    tree.insert_array([1, 2, 3, 4, 5, 6, 7, 8])
    assert str(tree.root) == "[[1, 2, 3], 4, [5, 6, [, 7, 8]]]"
    tree.delete_array([1, 3])
    assert str(tree.root) == "[[2, 4, 5], 6, [, 7, 8]]"
    tree.delete_array([7, 8])
    assert str(tree.root) == "[2, 4, [5, 6, ]]"
    tree.delete(4)
    assert str(tree.root) == "[2, 5, 6]"


def test_insert_array():
    """
    Test inserting the following tree using input array:
          4
        /   \
      2       5
     / \\    / \
    1   3   6   7
    """
    tree = AVLTree()
    tree.insert_array([1, 2, 3, 4, 5, 6, 7])
    assert str(tree.root) == "[[1, 2, 3], 4, [5, 6, 7]]"


def test_left_right():
    """
    Test Tree for left right rotation:
        5
       / \
      2   6
     / \
    1   3
         \
          4
    After rotation, height = 3:
        3
       / \
      2   5
     /   / \
    1   4   6
    """
    tree = AVLTree()
    tree.insert_array([5, 2, 6, 1, 3, 4])
    assert tree.root.height == 3
    assert str(tree.root) == "[[1, 2, ], 3, [4, 5, 6]]"


def test_right_left():
    """
    Test Tree for right left rotation:
      2
     / \
    1   5
       / \
      4   6
     /
    3
    After rotation, height = 3:
        4
       / \
      2   5
     / \\  \
    1   3   6
    """
    tree = AVLTree()
    tree.insert_array([2, 1, 5, 4, 6, 3])
    assert tree.root.height == 3
    assert str(tree.root) == "[[1, 2, 3], 4, [, 5, 6]]"


def test_right_right():
    """
    Test Tree for right right rotation:
      2
     / \
    1   4
       / \
      3   5
           \
            6
    After rotation, height = 2:
        4
       / \
      2   5
     / \\  \
    1   3   6
    """
    tree = AVLTree()
    tree.insert_array([2, 1, 4, 3, 5, 6])
    assert tree.root.height == 3
    assert str(tree.root) == "[[1, 2, 3], 4, [, 5, 6]]"


def test_left_left():
    """
    Test Tree for left left rotation:
          5
         / \
        3   6
       / \
      2   4
     /
    1
    After rotation, height = 3:
        3
       / \
      2   5
     /   / \
    1   4   6
    """
    tree = AVLTree()
    tree.insert_array([5, 3, 6, 2, 4, 1])
    assert tree.root.height == 3
    assert str(tree.root) == "[[1, 2, ], 3, [4, 5, 6]]"


def test_rebalance():
    """
    Testing deleting from a single side of the tree to see if the resulting tree remain balanced
    """
    tree = AVLTree()
    tree.insert_array([i for i in range(10000)])
    assert tree.root.height == 14
    tree.delete_array([i for i in range(9900)])
    assert tree.root.height == 7
    tree = AVLTree()
    tree.insert_array([i for i in range(10000)])
    assert tree.root.height == 14
    tree.delete_array([i for i in range(100, 10000)])
    assert tree.root.height == 7


def test_different_data_type():
    """
    Testing the AVL tree works on different data type
    """
    tree = AVLTree()
    tree.insert_array(['abcd', 'xyz', 'cbz', 'abc', 'ab', 'a', 'abb'])
    assert str(tree.root) == "[[a, ab, abb], abc, [abcd, cbz, xyz]]"
    tree = AVLTree()
    tree.insert_array([(3, 1), (1, 3), (2, 2), (2, 1), (1, 2), (2, 3), (3, 2)])
    assert str(tree.root) == "[[(1, 2), (1, 3), (2, 1)], (2, 2), [(2, 3), (3, 1), (3, 2)]]"
