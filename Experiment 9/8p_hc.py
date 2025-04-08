import numpy as np
import math

def reconstruct_path(parent_map, current):
    path = [np.array(current).reshape(3, 3)]
    
    while current in parent_map:
        current, _ = parent_map[current]
        path.append(np.array(current).reshape(3, 3))

    return path[::-1]

def heuristic_row_position(state, goal_state):
    '''
    Checks if the row is in the correct configuration  
    If yes then -1 for every block in the row  
    If not then +1 for every block in the row  
    '''
    penalty = 0
    state = np.array(state).reshape((3, 3))
    goal_state = np.array(goal_state).reshape((3, 3))

    for row in range(3):
        if all(state[row, :] == goal_state[row, :]):
            penalty -= 3  # Correct row
        else:
            penalty += np.sum(state[row, :] != goal_state[row, :])

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

def heuristic_euclidean(state, goal_state):
    '''
    Euclidean distance
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

def heuristic_manhattan(state, goal_state):
    '''
    Manhattan distance: sum of vertical and horizontal distances
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

def moves(state, move_directions):
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

def choose_heuristic(choice):
    if choice == 1: return heuristic_row_position
    if choice == 2: return heuristic_position
    if choice == 3: return heuristic_euclidean
    if choice == 4: return heuristic_manhattan
    return None

def eightPuzzle(start_state, heuristic_func):
    '''
    Eight Puzzle Problem using Hill Climbing algorithm  
    Uses a vector of size 9 to figure out  
    Blank space is indicated by 0   
    Final Solution: [1, 2, 3, 4, 5, 6, 7, 8, 0]  
    '''
    goal_state = tuple([1, 2, 3, 4, 5, 6, 7, 8, 0])  
    start_state = tuple(start_state.flatten())  
    move_directions = {'Up': -3, 'Down': 3, 'Left': -1, 'Right': 1}

    current_state = start_state
    current_h = heuristic_func(current_state, goal_state)
    parent_map = {}
    steps = 0
    visited = set()

    while current_state != goal_state:
        neighbors = moves(current_state, move_directions)
        next_state = None
        best_h = current_h

        for state, move in neighbors:
            if state in visited: continue
            h = heuristic_func(state, goal_state)
            if h < best_h:
                best_h = h
                next_state = state
                chosen_move = move

        if next_state is None:
            break

        parent_map[next_state] = (current_state, chosen_move)
        current_state = next_state
        current_h = best_h
        visited.add(current_state)
        steps += 1

    if current_state == goal_state:
        return reconstruct_path(parent_map, current_state), steps
    return None, steps


if __name__ == "__main__":
    while True:
        print("Enter array of size 9 with numbers 1 to 8 (consider blank space as 0): ")
        start_state = np.array([int(x) for x in input().split()])
        if np.size(start_state) == 9: break

    print("\nSelect the Heuristic Function:")
    print("1. Row Position ")
    print("2. Position Matching ")
    print("3. Euclidean Distance ")
    print("4. Manhattan Distance ")

    choice = int(input("Enter your choice (1-4): "))
    heuristic_func = choose_heuristic(choice)
    
    path, steps = eightPuzzle(start_state, heuristic_func)
    
    if path:
        print(f"\nSolution found in {steps} steps:")
        for step in path:
            print(step, "\n")
    else:
        print("No solution found")


# 1, 2, 3, 4, 5, 6, 0, 7, 8
# 1, 2, 3, 0, 5, 6, 4, 7, 8
