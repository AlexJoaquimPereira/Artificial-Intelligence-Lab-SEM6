from collections import deque

def dfs(graph, start_node, visited: set):
    """
    Depth First Search (DFS)
    graph: dictionary
    start_node: starting node of the graph
    visited: set to keep track of visited nodes
    """
    stack = [start_node]  # Initialize stack with the start node
    path = ''  # To store the traversal path

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.add(current_node)  # Mark the node as visited
            path += current_node + " -> "  # Add the node to the path

            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return path[:-4] if path else "No nodes visited"

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
    print("Traversed Path:")
    path = dfs(graph, 'D', visited)
    print(path)
