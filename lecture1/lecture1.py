class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

    class Graph:
        """Represent a graph as a dictionary of vertices mapping labels to edges."""
        def __init__(self):
            self.vertices = {}

        def add_vertex(self, vertex):
            """
            Add a vertex to the graph.
            """
            if self.vertices[vertex] is not None:
                self.vertices[vertex] = set()
            else:
                print("Warning: vertex exists.")

        def add_edge(self, vertex_from, vertex_to):
            """
            Add a directed edge to the graph.
            """
            if vertex_from in self.vertices and vertex_to in self.vertices:
                self.vertices[vertex_from].add(vertex_to)
            else:
                raise IndexError("That vertex does not exist!")

        def bft(self, starting_vertex):
            """
            Print each vertex in breadth-first order
            beginning from starting_vertex.
            """
            pass  # TODO

        def dft(self, starting_vertex):
            """
            Print each vertex in depth-first order
            beginning from starting_vertex.
            """
            pass  # TODO

        def dft_recursive(self, starting_vertex):
            """
            Print each vertex in depth-first order
            beginning from starting_vertex.
            This should be done using recursion.
            """
            pass  # TODO

        def bfs(self, starting_vertex, destination_vertex):
            """
            Return a list containing the shortest path from
            starting_vertex to destination_vertex in
            breath-first order.
            """
            pass  # TODO
        
        def dfs(self, starting_vertex, destination_vertex):
            """
            Return a list containing a path from
            starting_vertex to destination_vertex in
            depth-first order.
            """
            pass  # TODO

    
if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)