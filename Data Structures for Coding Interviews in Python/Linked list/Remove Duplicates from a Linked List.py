# Statement
# Given the head of a singly linked list, remove any duplicate nodes from the list in place, ensuring that only one occurrence of each value is retained in the modified list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return None

    current = head

    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next  # Remove duplicate
            else:
                runner = runner.next
        current = current.next

    return head

def main():
    inputs = [
        [1, 2, 3, 2, 4, 3],  # Test case 1: A linked list with duplicates
        [10, 20, 30, 20, 10], # Test case 2: A linked list with duplicates
        [],                   # Test case 3: An empty linked list
        [42],                 # Test case 4: A linked list with a single node
        [1, 1, 1, 1]          # Test case 5: A linked list with all duplicates
    ]

    for i, values in enumerate(inputs):
        # Create linked list from input values
        head = None
        for value in reversed(values):
            new_node = Node(value)
            new_node.next = head
            head = new_node

        # Remove duplicates from the linked list
        head = remove_duplicates(head)

        # Print the modified linked list
        current = head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        print(f"Test case {i + 1}: Modified linked list after removing duplicates: {result}")

if __name__ == "__main__":
    main()