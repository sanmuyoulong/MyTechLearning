# Statement
# Given the head of a linked list, check whether or not a cycle is present in the linked list. A cycle is present in a linked list if at least one node can be reached again by traversing the next pointer. If a cycle exists, return TRUE; otherwise, return FALSE.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detect_cycle(head):
    if not head:
        return False
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def create_linked_list(values, cycle_pos=-1):
    """
    values: 节点值列表
    cycle_pos: 环入口的下标（-1 表示无环）
    """
    if not values:
        return None
    
    nodes = []
    head = Node(values[0])
    nodes.append(head)
    current = head
    
    for val in values[1:]:
        new_node = Node(val)
        current.next = new_node
        current = new_node
        nodes.append(new_node)
    
    # 创建环
    if 0 <= cycle_pos < len(nodes):
        current.next = nodes[cycle_pos]
    
    return head


def main():
    # 每个测试用例：(节点值列表, 环入口位置)
    test_cases = [
        ([1, 2, 3, 1], 0),       # 有环，入口在第0个节点
        ([2, 4, 6, 8, 2], 0),    # 有环
        ([1, 2, 3, 4, 5], -1),   # 无环
        ([10, 20, 30, 40, 50, 10], 0),  # 有环
        ([5, 10, 15, 20], -1),   # 无环
    ]

    for i, (values, pos) in enumerate(test_cases):
        head = create_linked_list(values, pos)
        has_cycle = detect_cycle(head)
        print(f"Test case {i + 1}: Cycle detected? {has_cycle}")


if __name__ == "__main__":
    main()