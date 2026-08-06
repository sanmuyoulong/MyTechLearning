# Statement
# Given the head of a singly linked list, find the length of the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count

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

        # Calculate length of the linked list
        result = length(head)
        print(f"Test case {i + 1}: Length of the linked list is {result}")

if __name__ == "__main__":
    main()