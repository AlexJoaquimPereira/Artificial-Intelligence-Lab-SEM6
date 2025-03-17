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

def NewGen(next, priQueue:PriorityQueue):
    '''
    New generation function
    '''
    priQueue.pop(next)
    for neighbor in graph.get(next, []):
        priQueue.append(neighbor)
    
    return priQueue

def HillClimbing(graph, start_node, goal_node):
    """
    Hill Climbing algorithm(graph, start_node, goal_node) with heuristic function
    """
    priQueue = PriorityQueue()
    priQueue.put((heuristic(start_node, goal_node), start_node))
    parent_map = {start_node: None}  # Stores parent for path reconstruction
    cost_map = {start_node: 0}  # Stores mincost to reach each node
    
    curr_node = start_node
    _, next_node = NewGen(curr_node, priQueue)
    
    while heuristic(curr_node) < heuristic(next_node):
        curr_node = next_node
        _, next_node = NewGen(curr_node, priQueue)
    
    if next_node == goal_node:
        return reconstructPath(next_node, parent_map, cost_map)
    else: return None, None

if __name__ == "__main__":
    graph = {
        'A': [('B', 2), ('C', 4)],
        'B': [('C', 1), ('D', 7), ('E', 3)],
        'C': [('D', 2)],
        'D': [('B', 1)],
        'E': [('B', 3), ('F', 5)],
        'F': [('C', 2), ('E', 1)]
    }

    path, min_cost = HillClimbing(graph, 'A', 'F')
    if path:
        print(f"Shortest Path: {path}")
        print(f"Minimum Cost: {min_cost}")
    else:
        print("No path found")
