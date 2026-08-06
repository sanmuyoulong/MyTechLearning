# Statement
# Given the head of a linked list and a target, value, return the updated linked list head after adding the target value at the end of the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_tail(head, value):
    # 创建新节点
    new_node = Node(value)
    
    # 如果链表是空的，直接返回新节点作为头
    if head is None:
        return new_node
    
    # 找到最后一个节点
    current = head
    while current.next is not None:
        current = current.next
    
    # 让最后一个节点指向新节点
    current.next = new_node
    
    return head   # 返回原来的头节点

# 创建链表：1 → 2 → 3 → None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# 在尾部插入 4
new_head = insert_at_tail(head, 4)

# 打印结果：1 → 2 → 3 → 4 → None
current = new_head
while current:
    print(current.data, end=" → ")
    current = current.next
print("None")