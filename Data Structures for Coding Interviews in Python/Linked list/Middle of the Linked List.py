# Given the head of a singly linked list, return the middle node.

# - Even length: return **second middle**
# - Odd length: return exact middle

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_mid(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def main():
    inputs = [
        [1, 2, 3, 4, 5],  # Test case 1: A linked list with 5 nodes (odd length)
        [10, 20, 30, 40], # Test case 2: A linked list with 4 nodes (even length)
        [],               # Test case 3: An empty linked list
        [42],             # Test case 4: A linked list with a single node
        [1, 1, 1, 1]      # Test case 5: A linked list with duplicate values (even length)
    ]

    for i, values in enumerate(inputs):
        # Create linked list from input values
        head = None
        for value in reversed(values):
            new_node = Node(value)
            new_node.next = head
            head = new_node

        # Find the middle node
        mid_node = find_mid(head)

        # Print the middle node's value or indicate if the list is empty
        if mid_node:
            print(f"Test case {i + 1}: Middle node value is {mid_node.data}")
        else:
            print(f"Test case {i + 1}: The linked list is empty.")

if __name__ == "__main__":
    main()