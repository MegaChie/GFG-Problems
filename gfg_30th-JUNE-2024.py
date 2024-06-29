#!/usr/bin/python3


def delete_node(head, x):
    """
    Deletes the node at position x then returns the head of the linked list
    """
    if head is None:
        return None

    # Store head node
    temp = head

    # If the head needs to be removed
    if x == 1:
        head = temp.next
        if head is not None:
            head.prev = None
        temp = None
        return head

    # Traverse the list to find the node to be deleted
    for _ in range(x - 1):
        temp = temp.next
        if temp is None:
            return head

    # If the node to be deleted is the last node
    if temp.next is None:
        temp.prev.next = None
        temp = None
        return head

    # Node temp is the node to be deleted
    # Adjust the pointers
    temp.prev.next = temp.next
    temp.next.prev = temp.prev

    temp = None

    return head
