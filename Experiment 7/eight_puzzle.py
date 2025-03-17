from queue import PriorityQueue
import numpy as np
import math

def reconstruct_path(parent_map, current):
    path = [np.array(current).reshape(3, 3)]
    
    while current in parent_map:
        current, _ = parent_map[current]
        path.append(np.array(current).reshape(3, 3))

    return path[::-1]

def moves(state, move_directions):
    """
    Generates new states after moving the blank tile.
    """
    state = np.array(state).flatten()
    zero_index = np.where(state == 0)[0][0] 
    new_states = []

    for move, shift in move_directions.items():
        new_index = zero_index + shift
        if move == "Left" and zero_index % 3 == 0: continue
        if move == "Right" and zero_index % 3 == 2: continue
        if move == "Up" and zero_index < 3: continue
        if move == "Down" and zero_index > 5: continue

        new_state = state.copy()
        new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
        new_states.append((tuple(new_state), move))

    return new_states

def heuristic_row_position(state, goal_state):
    '''
    Checks if the row is in the correct configuration  
    If yes then -1 for every block in the row  
    If not then +1 for every block in the row  
    Lower is better as priority queue used
    '''
    penalty = 0
    return penalty

def heuristic_position(state, goal_state):
    '''
    Checks if the node is in the correct position  
    If yes then -1 penalty  
    If not then +1 penalty  
    Lower is better as priority queue used
    '''
    penalty = 0
    state = np.array(state).flatten()
    goal_state = np.array(goal_state).flatten()

    for i in range(9):
        if state[i] != 0:
            if state[i] == goal_state[i]:
                penalty -= 1
            else:
                penalty += 1
    return penalty

def heuristic_euclidan(state, goal_state):
    '''
    Euclidan distance: ((x1- x2)^2 + (y1- y2)^2)^2  
    Return the distance between the numbers
    '''
    state = np.array(state).reshape((3, 3))
    goal_positions = {goal_state[i]: (i // 3, i % 3) for i in range(9)}
    distance = 0

    for i in range(3):
        for j in range(3):
            value = state[i, j]
            if value != 0:
                goal_i, goal_j = goal_positions[value]
                distance += math.sqrt((goal_i - i)**2 + (goal_j - j)**2)

    return distance

def heuristic(state, goal_state):
    '''
    Manhattan distance: |(x1- x2) + (y1- y2)|  
    Return the distance between the numbers
    '''
    state = np.array(state).reshape((3, 3))
    goal_positions = {goal_state[i]: (i // 3, i % 3) for i in range(9)}
    distance = 0

    for i in range(3):
        for j in range(3):
            value = state[i, j]
            if value != 0:
                goal_i, goal_j = goal_positions[value]
                distance += abs(goal_i - i) + abs(goal_j - j)

    return distance

def eightPuzzle(start_state):
    '''
    Eight Puzzle Problem using BestFS algorithm
    Uses a vector of size 9 to figure out  
    Blank space is indicated by 0   
    Final Solution: [1, 2, 3, 4, 5, 6, 7, 8, 0]  
    '''
    goal_state = tuple([1, 2, 3, 4, 5, 6, 7, 8, 0])  
    start_state = tuple(start_state.flatten())  

    move_directions = {'Up': -3, 'Down': 3, 'Left': -1, 'Right': 1}
    
    pri_queue = PriorityQueue()
    pri_queue.put((heuristic(start_state, goal_state), start_state, None, None))  # (h(n), state, parent, move)

    parent_map = {}
    visited = set()

    while not pri_queue.empty():
        h_value, current_state, parent, move = pri_queue.get()
        
        # print(f"Processing state:\n{np.array(current_state).reshape(3, 3)}\n") # debug

        if current_state in visited: continue

        visited.add(current_state)
        if parent is not None:
            parent_map[current_state] = (parent, move)

        if current_state == goal_state:
            return reconstruct_path(parent_map, current_state)

        for new_state, move in moves(current_state, move_directions):
            if new_state not in visited:
                pri_queue.put((heuristic(new_state, goal_state), new_state, current_state, move))

    return None

if __name__ == "__main__":
    while True:
        print("Enter array of size 9 with numbers 1 to 8 (consider blank space as 0): ")
        start_state = np.array([int(x) for x in input().split()])
        if np.size(start_state) == 9:
            break
    
    path = eightPuzzle(start_state)
    
    if path:
        print("\nSolution Path:")
        for step in path:
            print(step, "\n")
    else:
        print("No solution found")
