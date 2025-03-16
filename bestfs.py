from queue import PriorityQueue

def reconstructPath(node, parent_map):
    """Reconstructs the path from goal to start"""
    path = []
    while node is not None:
        path.append(node)
        node = parent_map.get(node)  # Move to parent
    path.reverse()
    return " -> ".join(path)  # Corrected path format


def bestfs(graph, start_node, goal_node):
    """
    Best-First Search (graph, start_node, goal_node)
    graph: dictionary with costs (edge_cost)
    """
    priQueue = PriorityQueue()
    priQueue.put((0, start_node, None))  # (cost, node, parent)
    
    visited = set()
    parent_map = {}  # Store parent nodes

    while not priQueue.empty():
        cost, current_node, parent = priQueue.get()
        
        if current_node in visited:
            continue  # Skip if already visited
        
        visited.add(current_node)
        parent_map[current_node] = parent  # Track parent

        # Debug print
        print(f"Processing: {current_node}, Cost: {cost}")

        if current_node == goal_node:
            return reconstructPath(current_node, parent_map)

        for neighbor, edge_cost in graph.get(current_node, []):
            if neighbor not in visited:
                priQueue.put((edge_cost, neighbor, current_node))  # Push with cost

    return None  # No path found


if __name__ == "__main__":
    graph = {
        'A': [('B', 2), ('C', 4)],
        'B': [('C', 1), ('D', 7), ('E', 3)],
        'C': [('D', 2)],
        'D': [('B', 1)],
        'E': [('B', 3), ('F', 5)],
        'F': [('C', 2), ('E', 1)]
    }
    
    start = 'D'
    goal = 'A'

    path = bestfs(graph, start, goal)
    print("Shortest Path:", path if path else "No path found")
