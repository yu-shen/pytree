from __future__ import annotations
from typing import List


class TreeNode(object):
    """
    Binary Search Tree Node
    """
    def __init__(self, value: object):
        """
        :param value: value of the tree node
        """
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def in_order_traversal(self) -> List[object]:
        """
        Implements in order binary tree traversal as defined in: https://en.wikipedia.org/wiki/Tree_traversal#In-order
        :return: array containing
        """
        res = []
        if self.left:
            res += self.left.in_order_traversal()
        res.append(self.value)
        if self.right:
            res += self.right.in_order_traversal()
        return res

    def __str__(self):
        """
        :return: string representation of the binary tree structure
        """
        if self.left is None and self.right is None:
            return f"{self.value}"
        return f"[{self.left if self.left else ''}, {self.value}, {self.right if self.right else ''}]"


class AVLTree(object):
    """
    Python implementation of a self-balancing binary search tree (AVL tree).
    """
    def __init__(self):
        self.root = None

    def insert_array(self, array: List[object]) -> AVLTree:
        """
        Insert an array of values into the AVLTree
        :param array: array of values we want to insert into the AVLTree
        :return: the updated AVLTree
        """
        for value in array:
            self.insert(value)
        return self

    def insert(self, value: object) -> AVLTree:
        """
        Insert a single value into the AVLTree
        :param value: input value we want to insert into the AVLTree
        :return: the updated AVLTree
        """
        self.root = self._insert(self.root, value)
        return self

    def delete_array(self, array: List[object]) -> AVLTree:
        """
        Delete an array of values from the AVLTree
        :param array: array of values we want to delete from the AVLTree
        :return: the updated AVLTree
        """
        for value in array:
            self.delete(value)
        return self

    def delete(self, value: object) -> AVLTree:
        """
        Delete a single value into the AVLTree
        :param value: input value we want to delete from the AVLTree
        :return: the updated AVLTree
        """
        self.root = self._delete(self.root, value)
        return self

    def _insert(self, node: TreeNode, value: object) -> TreeNode:
        """
        Detailed implementation of node insertion followed by self balancing when necessary
        Average complexity O(log N), worst case O(log N)
        :param node: root of the subtree on which to insert the input value
        :param value: input value to insert into the subtree
        :return: root of the subtree
        """
        # step 0: follow the same process as inserting into a Binary Search Tree
        if node is None:
            return TreeNode(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        # step 1: update the height
        self._update_height(node)

        # step 2: compute the balance factor
        balance = self._get_balance(node)

        if balance < -1:
            if value < node.left.value:
                # step 3a: left left case
                return self._rotate_right(node)
            elif value > node.left.value:
                # step 3b: left right case
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        elif balance > 1:
            if value > node.right.value:
                # step 3c: right right case
                return self._rotate_left(node)
            elif value < node.right.value:
                # step 3d: right left case
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        return node

    def _delete(self, node: TreeNode, value: object) -> TreeNode:
        """
        Detailed implementation of node deletion followed by self balancing when necessary
        Average complexity O(log N), worst case O(log N)
        :param node: root of the subtree on which to delete the input value
        :param value: input value to delete from the subtree
        :return: root of the subtree
        """
        # step 0: follow the same process as deleting from a Binary Search Tree
        if node is None:
            return node
        elif value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_value = self._get_smallest_node(node.right).value
            node.value = min_value
            node.right = self._delete(node.right, min_value)

        if node is None:
            return node

        # step 1: update the height
        self._update_height(node)

        # step 2: compute the balance factor
        balance = self._get_balance(node)

        if balance < -1:
            if self._get_balance(node.right) >= 0:
                # step 3a: left left case
                return self._rotate_right(node)
            else:
                # step 3b: right left case
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        elif balance > 1:
            if self._get_balance(node.left) <= 0:
                # step 3c: right right case
                return self._rotate_left(node)
            else:
                # step 3d: left right case
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        return node

    def _rotate_right(self, node: TreeNode) -> TreeNode:
        """
        Before the right rotation:
             node
             /  \
          root  T3
          /  \
        T1  T2

        After the right rotation:
          root
          /  \
        T1   node
             /  \
           T2   T3
        :param node: node from which we want to perform the right rotation
        :return: the right rotated subtree
        """
        root = node.left
        node.left = root.right
        root.right = node
        self._update_height(node)
        self._update_height(root)
        return root

    def _rotate_left(self, node: TreeNode) -> TreeNode:
        """
        Before the left rotation:
          node
          /  \
        T1   root
             /  \
           T2   T3

        After the left rotation:
             root
             /  \
          node  T3
          /  \
        T1   T2
        :param node: node from which we want to perform the left rotation
        :return: the left rotated subtree
        """
        root = node.right
        node.right = root.left
        root.left = node
        self._update_height(node)
        self._update_height(root)
        return root

    @staticmethod
    def _get_height(node: TreeNode) -> int:
        """
        :param node: input node
        :return: the height of the input node
        """
        if node is None:
            return 0
        return node.height

    def _update_height(self, node: TreeNode) -> None:
        """
        Update the height value for the input node assuming height of child node have already been updated
        :param node: the input node on which we want to update teh height
        :return: the updated height of the input node
        """
        if node is not None:
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _get_balance(self, node: TreeNode) -> int:
        """
        :param node: input node
        :return: balance factor of the input node as defined by: https://en.wikipedia.org/wiki/AVL_tree#Balance_factor
        """
        if node is None:
            return 0
        return self._get_height(node.right) - self._get_height(node.left)

    def _get_smallest_node(self, node: TreeNode) -> TreeNode or None:
        """
        Traverse down from input node and return the smallest node in the subtree
        :param node: the root of the subtree in which we want to find the smallest node
        :return: the smallest node in the subtree
        """
        if node is None or node.left is None:
            return node
        return self._get_smallest_node(node.left)


if __name__ == '__main__':
    tree = AVLTree()
    tree.insert_array(["abc", "ab", "a"])
    print(tree.root)

