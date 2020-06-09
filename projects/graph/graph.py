"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() # set of edges from this vert

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2) # add v2 as a neighbor to v1

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)

        # Create a set to store visited vertices
        visited = set()

        # While queue is not empty
        while q.size() > 0:
            # Dequeue first vertex
            v = q.dequeue()

            # If that has not been visited
            if v not in visited:
                # Visit it
                # print(f"BFT: {v}")
                print(v)

                # Mark it as visited
                visited.add(v)

                # Then add all of its neighbors to back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and enqueue starting vertex ID
        s = Stack()
        s.push(starting_vertex)

        # Create a set to store visited vertices
        visited = set()

        # While stack is not empty
        while s.size() > 0:
            # Pop first vertex
            v = s.pop()

            # If that has not been visited
            if v not in visited:
                # Visit it
                # print(f"DFT: {v}")
                print(v)

                # Mark it as visited
                visited.add(v)

                # Then add all of its neighbors to back of the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Create new set
        if visited is None:
            visited = set()

        # print(f"DFT recursive: {starting_vertex}")
        print(starting_vertex)
        # Mark vertex as visited
        visited.add(starting_vertex)

        # Recursively do same for neighbors
        for next_vert in self.get_neighbors(starting_vertex):
            if next_vert not in visited:
                self.dft_recursive(next_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            # print(path)
            # Item from end of path
            v = path[-1]
            # print(v)
            if v not in visited:
                visited.add(v)
                # print(visited)
                if v is destination_vertex:
                    return path
                else:
                    for next_vert in self.get_neighbors(v):
                        q.enqueue(path + [next_vert])
        return False

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            path = s.pop()
            # print(path)
            # Item from end of path
            v = path[-1]
            if v not in visited:
                visited.add(v)
                # print(visited)
                if v is destination_vertex:
                    return path
                else:
                    for next_vert in self.get_neighbors(v):
                        s.push(path + [next_vert])
        return False

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Create new set & path
        if visited is None:
            visited = set()
        if path is None:
            path = [starting_vertex]

        visited.add(starting_vertex)

        # If at destination, return path
        if starting_vertex is destination_vertex:
            return path

        # Else recursively iterate through vertices
        for next_vert in self.get_neighbors(starting_vertex):
            if next_vert not in visited:
                new_path = self.dfs_recursive(next_vert, destination_vertex,
                                              visited, path=path+[next_vert])
                # If new_path exists
                if new_path:
                    return new_path
        return False

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
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

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    print("----------")

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    print("----------")

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print("----------")
    graph.dft_recursive(1)
    print("----------")

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))
    print("----------")

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print("----------")
    print(graph.dfs_recursive(1, 6))
    print("----------")
