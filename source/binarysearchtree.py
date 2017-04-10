#!python

class BinaryNode(object):

    def __init__(self, data):
        """Initialize this binary node with the given data"""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary node"""
        return 'BinaryNode({})'.format(repr(self.data))

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)"""
        # Check if both left child and right child have no value
        return self.left is None and self.right is None

    def is_internal(self):
        """Return True if this node is internal (has at least one child)"""
        # Check if either left child or right child has a value
        return self.left is not None or self.right is not None

    def height(self):
        """Return the number of edges on the longest downward path from this
        node to a descendant leaf node"""
        if self.is_leaf():
            return 0
        # Check if left child has a value and if so calculate its height
        left_height = self.left.height() if self.left is not None else -1
        # Check if right child has a value and if so calculate its height
        right_height = self.right.height() if self.right is not None else -1
        # Return one more than the greater of the left height and right height
        return 1 + max(left_height, right_height)


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items"""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree"""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree contains no nodes"""
        return self.root is None

    def height(self):
        """Return the number of edges on the longest downward path from this
        tree's root node to a descendant leaf node (the height of the root)"""
        # Check if root node has a value and if so calculate its height
        return self.root.height() if self.root is not None else -1

    def contains(self, item):
        """Return True if this binary search tree contains the given item"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return the node's data if found, or None
        return node.data if node is not None else None

    def _find_node(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Descend to the node's left child
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_parent_node(self, item):
        """Return the parent node of where the given item is (or would be) in
        this binary search tree, or None if this tree has only a root node"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def insert(self, item):
        """Insert the given item in order into this binary search tree"""
        # Handle the case where the tree is empty
        if self.is_empty():
        # if self.root is None:
            # Create a new root node
            self.root = BinaryNode(item)
            # Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node(item)
        # Check if the given item should be inserted left of the parent node
        if item < parent.data:
            # Create a new node and set the parent's left child
            parent.left = BinaryNode(item)
        # Check if the given item should be inserted right of the parent node
        elif item > parent.data:
            # Create a new node and set the parent's right child
            parent.right = BinaryNode(item)
        # Increase the tree size
        self.size += 1

    def delete(self, item):
        """Delete the given item from this binary search tree,
        or raise ValueError if this tree does not contain the given item"""
        # return
        if self.root is None:
            raise ValueError("Cannot delete from empty tree")

        # Find the node to delete and it's parent node
        parent = self.root
        node = self.root
        while node is not None:
            if item == node.data:
                break
            elif item > node.data:
                parent = node
                node = node.right
            else:
                parent = node
                node = node.left

        # Assert ValueError if the node was not found
        if node is None:
            raise ValueError("Item not found in tree: {}".format(item))

        # Delete the item
        if node.left is not None:
            rightmost, rightmost_parent = self._rightmost_node_and_parent(node.left)
            rightmost_parent.right = rightmost.left

            if node == self.root:
                self._reassign_root(rightmost)
                self.size -= 1
                return

            rightmost.right = node.right
            if node.data > parent.data:
                parent.right = rightmost
            else:
                parent.left = rightmost

        elif node.right is not None:
            leftmost, leftmost_parent = self._leftmost_node_and_parent(node.right)
            leftmost_parent.left = leftmost.right

            if node == self.root:
                self._reassign_root(leftmost)
                self.size -= 1
                return

            leftmost.left = node.left
            if node.data > parent.data:
                parent.right = leftmost
            else:
                parent.left = leftmost

        else:
            if node.data == parent.data: # self.root
                self.root = None
            elif node.data > parent.data:
                parent.right = None
            else:
                parent.left = None

        self.size -= 1

    def _reassign_root(self, new_node):
        new_node.right = self.root.right
        new_node.left = self.root.left
        self.root = new_node

    def _leftmost_node_and_parent(self, start_node):
        """Return a tuple containing the leftmost node in the subtree rooted at
        the given node and its parent node""" # or the same if it's the given node"""
        parent = start_node
        node = start_node
        while node.left is not None:
            parent = node
            node = node.left
        return (node, parent)

    def _rightmost_node_and_parent(self, start_node):
        """Find the rightmost node in the subtree"""
        parent = start_node
        node = start_node
        while node.right is not None:
            parent = node
            node = node.right
        return (node, parent)

    # def find_smallest(self):
    #     if self.root is None:
    #         return None
    #
    #     node = self.root
    #     while node.left is not None:
    #         node = node.left
    #
    #     return node.data
    #
    # def delete_smallest(self):
    #     if self.root is None:
    #         raise ValueError("Cannot delete from empty tree")
    #
    #     # Find the node to delete and it's parent node
    #     parent = self.root
    #     node = self.root
    #     while node.left is not None:
    #         parent = node
    #         node = node.left
    #
    #     if node == self.root:
    #         item = self.root.data
    #         self.root = node.right
    #         self.size -= 1
    #         return item
    #
    #     parent.left = node.left
    #     parent.right = node.right
    #     self.size -= 1
    #     return node.data

    def items_in_order(self, node=None, items=None):
        """Return a list of all items in this binary search tree found using
        in-order traversal starting at the given node after the given items"""
        if self.is_empty():
            return list()
        # Set up starting node and items list if not given
        if node is None:
            node = self.root
        if items is None:
            items = list()
        # Traverse left subtree, if it exists
        if node.left is not None:
            self.items_in_order(node.left, items)
        # Add this node's data to the items list
        items.append(node.data)
        # Traverse right subtree, if it exists
        if node.right is not None:
            self.items_in_order(node.right, items)
        # Return the items list to the original caller
        return items

    def items_pre_order(self, node=None, items=None):
        """Return a list of all items in this binary search tree found using
        pre-order traversal starting at the given node after the given items"""
        if self.is_empty():
            return list()
        # Set up starting node and items list if not given
        if node is None:
            node = self.root
        if items is None:
            items = list()
        # Add this node's data to the items list
        items.append(node.data)
        # Traverse left subtree, if it exists
        if node.left is not None:
            self.items_pre_order(node.left, items)
        # Traverse right subtree, if it exists
        if node.right is not None:
            self.items_pre_order(node.right, items)
        # Return the items list to the original caller
        return items

    def items_post_order(self, node=None, items=None):
        """Return a list of all items in this binary search tree found using
        post-order traversal starting at the given node after the given items"""
        if self.is_empty():
            return list()
        # Set up starting node and items list if not given
        if node is None:
            node = self.root
        if items is None:
            items = list()
        # Traverse left subtree, if it exists
        if node.left is not None:
            self.items_post_order(node.left, items)
        # Traverse right subtree, if it exists
        if node.right is not None:
            self.items_post_order(node.right, items)
        # Add this node's data to the items list
        items.append(node.data)
        # Return the items list to the original caller
        return items

    def items_level_order(self):
        """Return a list of all items in this binary search tree found using
        level-order traversal"""
        # Create a queue to store nodes not yet traversed in level-order
        queue = list()
        # Create an items list
        items = list()
        # Enqueue the root node if this tree is not empty
        if not self.is_empty():
            queue.append(self.root)
        # Loop until the queue is empty
        while len(queue) > 0:
            # Dequeue the node at the front of the queue
            node = queue.pop(0)
            # Add this node's data to the items list
            items.append(node.data)
            # Enqueue this node's left child if it exists
            if node.left is not None:
                queue.append(node.left)
            # Enqueue this node's right child if it exists
            if node.right is not None:
                queue.append(node.right)
        # Return the items list
        return items


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: ' + str(items))

    bst = BinarySearchTree()
    print('tree: ' + str(bst))
    print('root: ' + str(bst.root))

    print('\nInserting items:')
    for item in items:
        bst.insert(item)
        print('insert({}), size: {}'.format(item, bst.size))
    print('root: ' + str(bst.root))

    print('\nSearching for items:')
    for item in items:
        result = bst.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = bst.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    ' + str(bst.items_in_order()))
    print('items pre-order:   ' + str(bst.items_pre_order()))
    print('items post-order:  ' + str(bst.items_post_order()))
    print('items level-order: ' + str(bst.items_level_order()))

    # print('\nDeleting items:')
    # for item in items:
    #     bst.delete(item)
    #     print('delete({}), size: {}'.format(item, bst.size))
    # print('root: ' + str(bst.root))


if __name__ == '__main__':
    test_binary_search_tree()
