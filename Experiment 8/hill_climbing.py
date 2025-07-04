def reconstructPath(node, parent_map, cost_map):
    path = []
    total_cost = cost_map.get(node, 0)
    while node is not None:
        path.append(node)
        node = parent_map.get(node)
    path.reverse()
    return " -> ".join(path), total_cost

def heuristic(node):
    heuristic_values = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 0
    }
    return heuristic_values.get(node, float('inf'))

def HillClimbing(graph, start_node, goal_node):
    current = start_node
    parent_map = {current: None}
    cost_map = {current: 0}

    while True:
        current_h = heuristic(current)
        neighbors = graph.get(current, [])

        best_neighbor = None
        best_h = float('inf')
        best_cost = 0

        for neighbor, cost in neighbors:
            h = heuristic(neighbor)
            if h < best_h:
                best_h = h
                best_neighbor = neighbor
                best_cost = cost

        # Only move if neighbor has a better heuristic
        if best_neighbor and best_h < current_h:
            parent_map[best_neighbor] = current
            cost_map[best_neighbor] = cost_map[current] + best_cost
            current = best_neighbor

            if current == goal_node:
                return reconstructPath(current, parent_map, cost_map)
        else:
            break

    return None, None

# Example usage
if __name__ == "__main__":
    graph = {
        'A': [('B', 2), ('C', 4)],
        'B': [('C', 1), ('D', 7), ('E', 3)],
        'C': [('D', 2)],
        'D': [('B', 1)],
        'E': [('B', 3), ('F', 5)],
        'F': [('C', 2), ('E', 1)]
    }

    path, cost = HillClimbing(graph, 'A', 'C')
    if path:
        print(f"Path: {path}")
        print(f"Cost: {cost}")
    else:
        print("No path found")
