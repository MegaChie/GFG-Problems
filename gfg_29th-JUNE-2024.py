#!/usr/bin/python3


def areIdentical(head1, head2):
    """
    Checks if the passed linked lists are identical or not.
    Returns "True" if they are and "False" if not.
    """
    current1 = head1
    current2 = head2

    while current1 and current2:
        if current1.data != current2.data:
            return False
        current1 = current1.next
        current2 = current2.next

    if not current1 and not current2:
        return True

    if current1 and current2:
        return True

    return False
