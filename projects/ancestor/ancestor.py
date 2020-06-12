import sys
sys.path.append('../graph')

from util import Queue
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # Create graph
    graph = Graph()

    # Add vertices
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
    # Add edges, direction child > parent
    for parent, child in ancestors:
        graph.add_edge(child, parent)

    q = Queue()
    q.enqueue([starting_node])

    # if vertex has no parent (i.e. not empty set)
    # return -1
    if not graph.get_neighbors(starting_node):
        return -1

    # else go through parents (neighbors) in breadth-first order
    # sort in descending order, so higher numeric ID is dequeued first
    # last vertex from queue is the earliest ancestor
    else:
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]

            parents = graph.get_neighbors(v)
            for parent in sorted(parents, reverse=True):
                q.enqueue(path + [parent])
        return v


if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8),
                      (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 1))
    print(earliest_ancestor(test_ancestors, 2))
    print(earliest_ancestor(test_ancestors, 3))
    print(earliest_ancestor(test_ancestors, 4))
    print(earliest_ancestor(test_ancestors, 5))
    print(earliest_ancestor(test_ancestors, 6))
    print(earliest_ancestor(test_ancestors, 7))
    print(earliest_ancestor(test_ancestors, 8))
    print(earliest_ancestor(test_ancestors, 9))
    print(earliest_ancestor(test_ancestors, 10))
    print(earliest_ancestor(test_ancestors, 11))

