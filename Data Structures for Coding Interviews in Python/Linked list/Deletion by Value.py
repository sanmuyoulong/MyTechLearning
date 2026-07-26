# Statement
# Given the head of a singly linked list and a value to be deleted from the linked list, if the value exists in the linked list, delete the value and return TRUE. Otherwise, return FALSE.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete(head, value):
    if head is None:
        return False

    if head.data == value:
        head = head.next
        return True

    else:
        current = head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next
    return False

