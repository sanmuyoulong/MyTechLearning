# Statement
# Given the head of a singly linked list, search for a specific value. If the value is found, return TRUE; otherwise, return FALSE.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search(head, value):
    current = head
    while current is not None:
        if current.data == value:
            return True
        current = current.next

    return False

# 创建链表：1 → 2 → 3 → None
head = Node(1)  
head.next = Node(2)
head.next.next = Node(3)

# 搜索值 2
result = search(head, 2)
print(result)  # 输出: True