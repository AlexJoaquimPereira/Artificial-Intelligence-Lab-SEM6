from collections import deque
import numpy as np

# # taking multiple inputs at a time separated by comma
# x = [int(x) for x in input().split(",")]


# Take space-separated inputs and convert them to integers
# a = map(int, input().split())

# Convert the map object to a list
# b = list(a)

# create an empty queue
# queue = deque()

# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue.popleft())
# print(queue)
# queue.clear()

# BFS

def bfs(graph, start_node, visited:set):
    '''
    Breadth First Search(graph, start_node, visited)
    graph: dictionary
    visited: empty set
    '''
    queue = deque([start_node])
    visited.add(start_node)
    path = ''

    while queue:
        next = queue.popleft()
        # print(next, end=" ")
        path = path + next + "->"
        # if a goal state is needed
        # if next == 'D': return path

        for neighbor in graph.get(next, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                
    return path

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['C', 'D', 'E'],
        'C': ['D'],
        'D': ['B'],
        'E': ['B', 'A'],
        'F': ['C', 'E']
    }
    visited = set()
    print("Traversed path: ", )
    path = bfs(graph, 'A', visited)
    print(path)