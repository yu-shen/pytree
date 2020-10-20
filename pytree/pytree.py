class TreeNode(object):
    """
    Binary Search Tree Node
    """
    def __init__(self, value):
        """
        :param value: value of the tree node
        """
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        """
        :return: string representation of the binary tree structure
        """
        if self.left is None and self.right is None:
            return f"{self.value}"
        return f"[{self.left if self.left else ''}, {self.value}, {self.right if self.right else ''}]"


class AVLTree(object):
    """
    Python implementation of a self-balancing binary search tree.
    """
    def __init__(self):
        self.root = None

    @staticmethod
    def update_height(node):
        if node is not None:
            node.height = 1 + max(AVLTree.get_height(node.left), AVLTree.get_height(node.right))

    @staticmethod
    def get_height(node):
        if node is None:
            return 0
        return node.height

    @staticmethod
    def get_balance(node):
        """
        :param node: input node
        :return: balance factor of the input node as defined by: https://en.wikipedia.org/wiki/AVL_tree#Balance_factor
        """
        if node is None:
            return 0
        return AVLTree.get_height(node.right) - AVLTree.get_height(node.left)

    @staticmethod
    def get_smallest_node(node):
        if node is None or node.left is None:
            return node
        return AVLTree.get_smallest_node(node.left)

    @staticmethod
    def rotate_right(node):
        """
             node
             /  \
          root  T3
         /  \
        T1  T2
          root
          /  \
        T1   node
             /  \
            T2  T3
        """
        root = node.left
        node.left = root.right
        root.right = node
        AVLTree.update_height(node)
        AVLTree.update_height(root)
        return root

    @staticmethod
    def rotate_left(node):
        """
          node
          /  \
        T1   root
             /  \
            T2  T3
             root
             /  \
          node  T3
         /  \
        T1  T2
        """
        root = node.right
        node.right = root.left
        root.left = node
        AVLTree.update_height(node)
        AVLTree.update_height(root)
        return root

    @staticmethod
    def insert(node, value):
        # step 0: follow the same process as inserting into a Binary Search Tree
        if node is None:
            return TreeNode(value)
        elif value < node.value:
            node.left = AVLTree.insert(node.left, value)
        else:
            node.right = AVLTree.insert(node.right, value)

        # step 1: update the height
        AVLTree.update_height(node)

        # step 2: compute the balance factor
        balance = AVLTree.get_balance(node)

        if balance < -1:
            if value < node.left.value:
                return AVLTree.rotate_right(node)
            elif value > node.left.value:
                node.left = AVLTree.rotate_left(node.left)
                return AVLTree.rotate_right(node)
        elif balance > 1:
            if value > node.right.value:
                return AVLTree.rotate_left(node)
            elif value < node.right.value:
                node.right = AVLTree.rotate_right(node.right)
                return AVLTree.rotate_left(node)
        return node

    @staticmethod
    def delete(node, value):
        # step 0: follow the same process as deleting from a Binary Search Tree
        if node is None:
            return node
        elif value < node.value:
            node.left = AVLTree.delete(node.left, value)
        elif value > node.value:
            node.right = AVLTree.delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_value = AVLTree.get_smallest_node(node.right)
            node.value = min_value
            node.right = AVLTree.delete(node.right, min_value)

        if node is None:
            return node

        # step 1: update the height
        AVLTree.update_height(node)

        # step 2: compute the balance factor
        balance = AVLTree.get_balance(node)

        if balance < -1:
            if AVLTree.get_balance(node.left) >= 0:
                return AVLTree.rotate_right(node)
            else:
                node.left = AVLTree.rotate_left(node.left)
                return AVLTree.rotate_right(node)
        elif balance > 1:
            if AVLTree.get_balance(node.right) < 0:
                return AVLTree.rotate_left(node)
            else:
                node.right = AVLTree.rotate_right(node.right)
                return AVLTree.rotate_left(node)
        return node


if __name__ == '__main__':
    # left right
    tree = AVLTree()
    tree.root = AVLTree.insert(tree.root, 4)
    tree.root = AVLTree.insert(tree.root, 1)
    tree.root = AVLTree.insert(tree.root, 2)
    tree.root = AVLTree.insert(tree.root, 3)
    print(tree.root)

    # right left
    tree = AVLTree()
    tree.root = AVLTree.insert(tree.root, 1)
    tree.root = AVLTree.insert(tree.root, 4)
    tree.root = AVLTree.insert(tree.root, 3)
    tree.root = AVLTree.insert(tree.root, 2)
    print(tree.root)

    # left left
    tree = AVLTree()
    tree.root = AVLTree.insert(tree.root, 4)
    tree.root = AVLTree.insert(tree.root, 3)
    tree.root = AVLTree.insert(tree.root, 2)
    tree.root = AVLTree.insert(tree.root, 1)
    print(tree.root)

    # right right
    tree = AVLTree()
    tree.root = AVLTree.insert(tree.root, 1)
    tree.root = AVLTree.insert(tree.root, 2)
    tree.root = AVLTree.insert(tree.root, 3)
    tree.root = AVLTree.insert(tree.root, 4)
    tree.root = AVLTree.insert(tree.root, 5)
    tree.root = AVLTree.insert(tree.root, 6)
    tree.root = AVLTree.insert(tree.root, 7)
    tree.root = AVLTree.delete(tree.root, 1)
    tree.root = AVLTree.delete(tree.root, 2)
    tree.root = AVLTree.delete(tree.root, 3)
    print(tree.root)

