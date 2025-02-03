from collections import deque
import numpy as np

def bfs_rule(next, visited, capacity_a, capacity_b):
    """
    Generate all possible states from the current state
    """
    x, y = next
    possible_states = []
    
    # fill jug A
    if (capacity_a, y) not in visited: 
        possible_states.append((capacity_a, y))
    
    # empty jug A
    if (0, y) not in visited: 
        possible_states.append((0, y))
    
    # fill jug B
    if (x, capacity_b) not in visited: 
        possible_states.append((x, capacity_b))
    
    # empty jug B
    if (x, 0) not in visited: 
        possible_states.append((x, 0))
        
    # if x + y > capacity_b
    if x + y > capacity_b and (x + y - capacity_b, capacity_b) not in visited:
        possible_states.append((x + y - capacity_b, capacity_b))
    
    # if x + y <= capacity_b
    if x + y <= capacity_b and (0, x + y) not in visited:
        possible_states.append((0, x + y))
        
    # if x + y > capacity_a
    if x + y > capacity_a and (capacity_a, x + y - capacity_a) not in visited:
        possible_states.append((capacity_a, x + y - capacity_a))
    
    # if x + y <= capacity_a
    if x + y <= capacity_a and (x + y, 0) not in visited:
        possible_states.append((x + y, 0))
        
    return possible_states
    

def bfs(a:int, b:int, capacity_a, capacity_b, water_in_a):
    '''
    Breadth First Search adapted for water jug problem
    '''
    queue = deque([(a, b)])
    visited = set()
    visited.add((a, b))
    path = []
    
    while queue:
        next = queue.popleft()
        path.append(next)
        # print("New state: ", next, ="\n")
        # print(*queue, sep=", ")
        if next == (water_in_a, 0): # goal state
            return path
        
        for new in bfs_rule(next, visited, capacity_a, capacity_b):
            if new not in visited:
                queue.append(new)
                visited.add(new)
    
    return None
        

if __name__ == "__main__":
    jug_a = 0
    jug_b = 0
    capacity_a = int(input("Capacity of jug A: "))
    capacity_b = int(input("Capacity of jug b: "))
    water_in_a = int(input("Amount of water you want in A: "))
    path = bfs(jug_a, jug_b, capacity_a, capacity_b, water_in_a)
    print("Solution: ", path)