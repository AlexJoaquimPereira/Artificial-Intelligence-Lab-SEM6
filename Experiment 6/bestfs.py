from queue import PriorityQueue

def reconstructPath(node, parent_map, cost_map):
    path = []
    total_cost = cost_map.get(node, 0)
    while node is not None:
        path.append(node)
        node = parent_map.get(node)
    path.reverse()
    path_str = " -> ".join(path)
    return path_str, total_cost

def heuristic(node, goal_node):
    heuristic_values = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 0
    }
    return heuristic_values.get(node, float('inf'))

def bestfs(graph, start_node, goal_node):
    """
    Best-First Search (graph, start_node, goal_node) with heuristic function
    """
    priQueue = PriorityQueue()
    priQueue.put((heuristic(start_node, goal_node), start_node))
    visited = set()
    parent_map = {start_node: None}  # Stores parent for path reconstruction
    cost_map = {start_node: 0}  # Stores mincost to reach each node

    while not priQueue.empty():
        heuristic_cost, next_node = priQueue.get()

        if next_node in visited: 
            continue

        visited.add(next_node)

        if next_node == goal_node:
            return reconstructPath(next_node, parent_map, cost_map)

        for neighbor, edge_cost in graph.get(next_node, []):
            if neighbor not in visited:
                new_cost = cost_map[next_node] + edge_cost
                parent_map[neighbor] = next_node
                cost_map[neighbor] = new_cost
                priQueue.put((heuristic(neighbor, goal_node), neighbor))

    return None, None

if __name__ == "__main__":
    graph = {
        'A': [('B', 2), ('C', 4)],
        'B': [('C', 1), ('D', 7), ('E', 3)],
        'C': [('D', 2)],
        'D': [('B', 1)],
        'E': [('B', 3), ('F', 5)],
        'F': [('C', 2), ('E', 1)]
    }

    path, min_cost = bestfs(graph, 'D', 'F')
    if path:
        print(f"Shortest Path: {path}")
        print(f"Minimum Cost: {min_cost}")
    else:
        print("No path found")
