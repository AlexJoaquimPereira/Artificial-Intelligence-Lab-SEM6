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


def bestfs(graph, start_node, goal_node):
    """
    Best-First Search (graph, start_node, goal_node)
    graph: dictionary with added costs (edge_cost)
    """
    priQueue = PriorityQueue()
    priQueue.put((0, start_node))
    visited = set()
    parent_map = {start_node: None}  # Stores parent for path reconstruction
    cost_map = {start_node: 0}  # Stores mincost to reach each node
    
    while not priQueue.empty():
        cost, next = priQueue.get()
        
        if next in visited: continue
        
        visited.add(next)

        if next == goal_node:
            return reconstructPath(next, parent_map, cost_map)
        
        for neighbor, edge_cost in graph.get(next, []):
            new_cost = cost + edge_cost
            if neighbor not in cost_map or new_cost < cost_map[neighbor]:  
                cost_map[neighbor] = new_cost
                parent_map[neighbor] = next
                priQueue.put((new_cost, neighbor))

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
    
    path, min_cost = bestfs(graph, 'A', 'F')
    if path:
        print(f"Shortest Path: {path}")
        print(f"Minimum Cost: {min_cost}")
    else:
        print("No path found")
