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

def find_nth(head, n):
    if head is None or n <= 0:
        return None

    # Reverse the linked list
    reversed_head = reverse(head)

    # Traverse to the nth node
    current = reversed_head
    count = 1
    while current is not None and count < n:
        current = current.next
        count += 1

    # Reverse the linked list back to original order
    reverse(reversed_head)

    # If we reached the nth node, return it; otherwise, return None
    if count == n and current is not None:
        return current.data
    else:
        return None

def main():
    inputs = [
        ([1, 2, 3, 4, 5], 2),
        ([10, 20, 30], 1),
        ([5, 10, 15, 20], 4),
        ([1], 1),
        ([], 1),  # Edge case: empty list
        ([1, 2, 3], 5)  # Edge case: n greater than length of list
    ]

    for values, n in inputs:
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

        # Find the nth node from the end
        result = find_nth(head, n)
        print(f"The {n}th node from the end of the list {values} is: {result}")

if __name__ == "__main__":
    main()