from collections import deque
import numpy as np

def bfs_rule(next, visited):
    """
    Generate all possible states from the current state
    """
    x, y = next
    possible_states = []
    
    # fill jug A
    if (4, y) not in visited: 
        possible_states.append((4, y))
    
    # empty jug A
    if (0, y) not in visited: 
        possible_states.append((0, y))
    
    # fill jug B
    if (x, 3) not in visited: 
        possible_states.append((x, 3))
    
    # empty jug B
    if (x, 0) not in visited: 
        possible_states.append((x, 0))
        
    # if x + y > 3
    if x + y > 3 and (x + y - 3, 3) not in visited:
        possible_states.append((x + y - 3, 3))
    
    # if x + y <= 3
    if x + y <= 3 and (0, x + y) not in visited:
        possible_states.append((0, x + y))
        
    # if x + y > 4
    if x + y > 4 and (4, x + y - 4) not in visited:
        possible_states.append((4, x + y - 4))
    
    # if x + y <= 4
    if x + y <= 4 and (x + y, 0) not in visited:
        possible_states.append((x + y, 0))
        
    return possible_states
    

def bfs(a:int, b:int):
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
        if next == (2, 0): 
            return path
        
        for new in bfs_rule(next, visited):
            if new not in visited:
                queue.append(new)
                visited.add(new)
    
    return None
        

if __name__ == "__main__":
    jug_a = 0
    jug_b = 0
    capacity_a = int(input("Capacity of jug A: "))
    capacity_b = int(input("Capacity of jug b: "))
    print("Traversed path: ", bfs(jug_a, jug_b))
