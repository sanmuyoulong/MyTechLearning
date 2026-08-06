# From linked_list_node import node
from edu_linked_list_node import EduLinkedListNode

# Template for the LinkedList
class EduLinkedList:
    # __init__ will be used to make a LinkedList-type object
    def __init__(self):
        self.head = None

    # The insert_node_at_head method will insert a EduLinkedListNode at head
    # of a LinkedList
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # The create_linked_list method will create the LinkedList using the
    # given integer array with the help of the InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = EduLinkedListNode(x)
            self.insert_node_at_head(new_node)

    # Returns the number of nodes in the LinkedList
    def get_length(self, head):
        temp = head
        length = 0
        while(temp):
            length+=1
            temp = temp.next
        return length

    # Returns the node at the specified position (index) of the LinkedList
    def get_node(self, head, pos):
        if pos != -1:
            p = 0
            ptr = head
            while p < pos:
                ptr = ptr.next
                p += 1
            return ptr
    
    # The __str__(self) method will display the elements of the LinkedList.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result
