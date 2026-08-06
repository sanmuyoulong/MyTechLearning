class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev to current
        current = next_node       # Move to the next node
    return prev  # New head of the reversed linked list

def if_palindrome(head):
    if head is None:
        return True

    # Reverse the linked list
    reversed_head = reverse(head)

    # Compare the original and reversed linked lists
    current_original = head
    current_reversed = reversed_head
    while current_original is not None and current_reversed is not None:
        if current_original.data != current_reversed.data:
            # Reverse the linked list back to original order before returning
            reverse(reversed_head)
            return False
        current_original = current_original.next
        current_reversed = current_reversed.next

    # Reverse the linked list back to original order before returning
    reverse(reversed_head)
    return True

def main():
    inputs = [
        [1, 2, 3, 2, 1],
        [10, 20, 30, 20, 10],
        [5, 10, 15, 20],
        [1],
        [],
        [1, 2, 3]
    ]

    for values in inputs:
        # Create linked list from values
        head = None
        tail = None
        for value in values:
            new_node = Node(value)
            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

        # Check if the linked list is a palindrome
        result = if_palindrome(head)
        print(f"Linked list {values} is a palindrome: {result}")

if __name__ == "__main__":
    main()