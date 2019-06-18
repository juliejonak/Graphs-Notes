def bfs(self, starting_vertex, destination_vertex):
    #Create an empty set to store the visited vertices
    visited = set()
    # Create an empty Queue and enqueue & PATH TO the starting vertex
    q = Queue()
    q.enqueue( [starting_vertex] )
    # While the queue is not empty...
    while q.size() > 0:
        # Dequeue the first PATH
        path = q.dequeue()
        # GRAB THE VERTEX FROM THE END OF THE PATH
        v = path[-1]
        # IF VERTEX = TARGET, RETURN PATH
        if v == destination_vertex:
            return path
        # If that vertex has not been visited...
        if v not in visited
            # Mark it as visited
            visited.add(v)
            # Then add & PATH TO all of its neighbors to the back of the queue
            for neighbor in self.vertices[v]:
                # Copy the path so that the append is being added to the list copy, not to the actual list which would result in 
                path_copy = list(path)
                # Append neighbor to the back of the copy
                path_copy.append(neighbor)
                # Enqueue copy
                q.enqueue(path_copy)

                
## Recursive DFS solution

def dft_recursive(self, starting_vertex, visited=None ):
    # Print each vertex in depth-first order beginning from starting_verex. This should be done using recursion.
    if visited is None:
        visited = set()
    # If the node hasn't been visited...
    if starting_vertex not in visited:
        # Mark the node as visited
        print(starting_vertex)
        visited.add(starting_vertex)
    # Then call DFT_recursive on each child
    for neighbor in self.vertices[starting_vertex]:
        self.dft_recursive(neighbor, visited)

    
                