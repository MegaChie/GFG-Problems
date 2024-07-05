#!/usr/bin/python3


def populateNext(root):
    """
    Populates the next pointer for all nodes.
    If the the node is the last in the tree the pointer will be -1
    """
    prev = None

    def inorder(node):
        nonlocal prev
        if node is None:
            return
        # Traverse the left subtree
        inorder(node.left)
        # If prev is not None, set its next pointer to the current node
        if prev:
            prev.next = node
        # Update prev to the current node
        prev = node
        # Traverse the right subtree
        inorder(node.right)
    # Start the in-order traversal from the root
    inorder(root)
