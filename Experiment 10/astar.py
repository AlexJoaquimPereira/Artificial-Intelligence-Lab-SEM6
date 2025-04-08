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
    '''
    Heuristic values inferred from Manhattan dist. of handwritten graph
    '''
    heuristic_values = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 0
    }
    return heuristic_values.get(node, float('inf'))

def a_star(graph, start_node, goal_node):
    """
    A* Search (graph, start_node, goal_node)
    """
    priQueue = PriorityQueue()
    priQueue.put((0 + heuristic(start_node, goal_node), start_node))  # (f = g + h, node) where initial g = 0
    parent_map = {start_node: None}
    cost_map = {start_node: 0}
    visited = set()

    while not priQueue.empty():
        f_value, current = priQueue.get()

        if current in visited:
            continue

        visited.add(current)

        if current == goal_node:
            return reconstructPath(current, parent_map, cost_map)

        for neighbor, edge_cost in graph.get(current, []):
            if neighbor not in visited:
                new_cost = cost_map[current] + edge_cost  # g(n)
                total_cost = new_cost + heuristic(neighbor, goal_node)  # f(n) = g(n) + h(n)

                if neighbor not in cost_map or new_cost < cost_map[neighbor]:
                    cost_map[neighbor] = new_cost
                    parent_map[neighbor] = current
                    priQueue.put((total_cost, neighbor))

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

    path, min_cost = a_star(graph, 'F', 'D')
    if path:
        print(f"Shortest Path: {path}")
        print(f"Minimum Cost: {min_cost}")
    else:
        print("No path found")
