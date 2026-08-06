# Statement
# Given the head of a singly linked list, reverse the linked list and return its updated head.

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

def main():
    inputs = [
        [1, 2, 3, 4, 5],  # Test case 1: A linked list with 5 nodes
        [10, 20, 30],     # Test case 2: A linked list with 3 nodes
        [],               # Test case 3: An empty linked list
        [42],             # Test case 4: A linked list with a single node
        [1, 1, 1, 1, 1]   # Test case 5: A linked list with duplicate values
    ]

    for i, values in enumerate(inputs):
        # Create linked list from input values
        head = None
        for value in reversed(values):
            new_node = Node(value)
            new_node.next = head
            head = new_node

        # Reverse the linked list
        reversed_head = reverse(head)

        # Print the reversed linked list
        current = reversed_head
        reversed_list = []
        while current is not None:
            reversed_list.append(current.data)
            current = current.next
        print(f"Test case {i + 1}: Reversed linked list is {reversed_list}")

if __name__ == "__main__":
    main()
