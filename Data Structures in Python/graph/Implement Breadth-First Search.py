from graph import Graph
from my_queue import MyQueue

def bfs_traversal(graph, source):
    result = []
    num_of_vertices = graph.vertices
    visited = [False] * num_of_vertices

    # Create a queue for BFS
    queue = MyQueue()

    # Enqueue the source vertex and mark it as visited
    queue.enqueue(source)
    visited[source] = True

    # Perform BFS
    while not queue.is_empty():
        # dequeue a vertex from the queue and add it to the result
        current_vertex = queue.dequeue()
        result.append(current_vertex)

        # Enqueue all neighbors of the dequeued vertex
        temp = graph.array[current_vertex].head
        while temp is not None:
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                # Mark the neighbors as visited when they are enqueued
                visited[temp.data] = True
            temp = temp.next

    return result

# Driver code
def main():
    # Vertices for each graph
    graph_vertices = [5, 4, 6]  
    # Edges for each graph
    graph_edges = [[[[0, [1, 2]], [2, [0, 3, 4]]]], [[[0, [1, 2]], [2, [0, 3]]]], [[[0, [1, 4]], [1, [2, 5]], [4, [3]], [3, [2]]]]]  
    sources = [2, 0, 0]
    
    for i in range(len(graph_vertices)):
        graph = Graph(graph_vertices[i])
        for j in range(len(graph_edges[i][0])):
            source, destinations = graph_edges[i][0][j]
            graph.add_edge(source, destinations)
        
        print(str(i+1)+".\t>>Adjacency List of the Graph<<\n")
        graph.print_graph()
        print("\n\tBFS Traversal starting from vertex "+ str(sources[i])+ ":", bfs_traversal(graph, sources[i]))
        print("-"*100, "\n")
if __name__ == "__main__":
    main()