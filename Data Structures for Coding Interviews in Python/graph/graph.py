from edu_linked_list import EduLinkedList
from edu_linked_list_node import EduLinkedListNode

class Graph:
    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # Definining a list that can hold multiple EduLinkedLists
        # Equal to the number of vertices in the graph
        self.array = []
        # Creating a new EduLinkedList for each vertex/index of the list
        for i in range(vertices):
            self.array.append(EduLinkedList())

    # Function to add an edge from source to destination
    def add_edge(self, source, destinations):
        if source < self.vertices:
            for dest in destinations:
                if dest < self.vertices:
                    dest_node = EduLinkedListNode(dest)
                    self.array[source].insert_node_at_head(dest_node)
        
        # As we are implementing a directed graph, (1,0) is not equal to (0,1)
            # dest_node = EduLinkedListNode(destination)
            # self.array[source].insert_node_at_head(dest_node)

        # If we were to implement an Undirected Graph, i.e., (1,0) == (0,1),
        # we would create an edge from destination toward source as well
        # i.e., self.list[destination].insertAtHead(source)

    def print_graph(self):
        for i in range(self.vertices):
            print("\t|", i, end=" | => ")
            temp = self.array[i].head
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next
            print("None")
