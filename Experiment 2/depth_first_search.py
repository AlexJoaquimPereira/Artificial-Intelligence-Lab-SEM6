from collections import deque
import numpy as np

def dfs(graph, start_node, visited:set):
    '''
    Depth First Search(graph, start_node, visited)
    graph: dictionary
    visited: empty set
    '''
    stack = [start_node]
    visited.add(start_node)
    path = ''

    while stack:
        next = stack.pop()
        # print(next, end=" ")
        path = path + next + "->"
        # if a goal state is needed
        if next == 'C': return path

        for neighbor in graph.get(next, []):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                
    return None

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
    path = dfs(graph, 'D', visited)
    print(path)