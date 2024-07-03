#!/usr/bin/python3


def removeAllDuplicates(self, head):
    """
    Given a linked list, it deletes all node that occure more than once
    and then returns the head.
    """
    if not head:
        return None

    temp = Node(0)
    temp.next = head
    prev = temp
    current = head

    while current:
        # Move current forward while there are duplicates
        while current.next and current.data == current.next.data:
            current = current.next

        # If prev.next is not current, we found duplicates
        if prev.next != current:
            prev.next = current.next  # Skip all duplicates
        else:
            prev = prev.next  # No duplicates, move prev forward

        current = current.next  # Move current forward

    return temp.next
