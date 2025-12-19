"""
Binary Search Tree implementation.
"""
class TreeNode:
    """
    Node of a binary search tree.
    """
    def __init__(self, key):
        """Initialize a tree node."""
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        """Return string representation of the node."""
        return str(self.key)

class BinarySearchTree:
    """
    Binary Search Tree data structure.
    """
    def __init__(self):
        """Initialize an empty binary search tree."""
        self.root = None

    def _insert(self, node, key):
        """Recursively insert a key starting from a given node."""
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:

            node.right = self._insert(node.right, key)
        return node

    def insert(self, key):
        """Insert a key into the binary search tree."""
        self.root = self._insert(self.root, key)

    def _search(self, node, key):
        """Recursively search for a key starting from a given node."""
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def search(self, key):
        """Search for a key in the tree."""
        return self._search(self.root, key)

    def _delete(self, node, key):
        """Recursively delete a key starting from a given node."""
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)

        return node

    def delete(self, key):
        """Delete a key from the tree."""
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        """Return the minimum key value starting from a given mode."""
        while node.left is not None:
            node = node.left
        return node.key

    def _inorder_traversal(self, node, result):
        """Perform inorder traversal starting from a given node."""
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        """Return the inorder traversal of the tree."""
        result = []
        self._inorder_traversal(self.root, result)
        return result

bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

for value in nodes:
    bst.insert(value)

print('Search for 80:', bst.search(80))

print("Inorder traversal:", bst.inorder_traversal())

bst.delete(40)

print("Search for 40:", bst.search(40))

print('Inorder traversal after deleting 40:', bst.inorder_traversal())
