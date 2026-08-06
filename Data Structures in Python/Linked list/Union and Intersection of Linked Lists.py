# Statement
# Given the heads of two linked lists, head1 and head2, as inputs. Implement the union and intersection functions for the linked lists. The order of elements in the output lists doesn’t matter.

# Here’s how you will implement the functions:

# Union: This function will take two linked lists as input and return a new linked list containing all the unique elements.

# Intersection: This function will take two linked lists as input and return all the common elements between them as a new linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def union(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    
    current = head1
    while current.next:
        current = current.next
    current.next = head2

    if not head1:
            return None
    
    current = head1
    
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next  # Remove duplicate
            else:
                runner = runner.next
        current = current.next
    
    return head1

def intersection(head1, head2):
    if not head1 or not head2:
        return None

    inter_head = None
    inter_tail = None
    current1 = head1

    while current1:
        current2 = head2
        found = False
        # 在第二个链表找相同元素
        while current2:
            if current1.data == current2.data:
                found = True
                break
            current2 = current2.next
        
        # 找到且不在结果里，加入交集链表
        if found:
            new_node = Node(current1.data)
            # 空链表初始化
            if not inter_head:
                inter_head = new_node
                inter_tail = new_node
            else:
                # 去重：避免交集重复
                if inter_tail.data != new_node.data:
                    inter_tail.next = new_node
                    inter_tail = inter_tail.next
        current1 = current1.next
    return inter_head

def main():
    inputs = [
        ([1, 2, 3], [3, 4, 5]),  # Test case 1: Two linked lists with some common elements
        ([10, 20, 30], [40, 50]), # Test case 2: Two linked lists with no common elements
        ([], [1, 2, 3]),          # Test case 3: One empty linked list
        ([42], [42]),             # Test case 4: Two linked lists with the same single element
        ([1, 1, 1], [1, 1])       # Test case 5: Two linked lists with all duplicates
    ]

    for i, (values1, values2) in enumerate(inputs):
        # Create first linked list from input values
        head1 = None
        for value in reversed(values1):
            new_node = Node(value)
            new_node.next = head1
            head1 = new_node

        # Create second linked list from input values
        head2 = None
        for value in reversed(values2):
            new_node = Node(value)
            new_node.next = head2
            head2 = new_node

        # Get the union of the two linked lists
        union_head = union(head1, head2)

        # Print the modified linked list after union
        current = union_head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        print(f"Test case {i + 1}: Union of the two linked lists: {result}")

    inputs_intersection = [
        ([1, 2, 3], [3, 4, 5]),
        ([10, 20, 30], [40, 50]),
        ([], [1, 2, 3]),
        ([42], [42]),
        ([1, 1, 1], [1, 1])
    ]

    for i, (values1, values2) in enumerate(inputs_intersection):
        # Create first linked list from input values
        head1 = None
        for value in reversed(values1):
            new_node = Node(value)
            new_node.next = head1
            head1 = new_node

        # Create second linked list from input values
        head2 = None
        for value in reversed(values2):
            new_node = Node(value)
            new_node.next = head2
            head2 = new_node

        # Get the intersection of the two linked lists
        intersection_head = intersection(head1, head2)

        # Print the modified linked list after intersection
        current = intersection_head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        print(f"Test case {i + 1}: Intersection of the two linked lists: {result}")

if __name__ == "__main__":
    main()