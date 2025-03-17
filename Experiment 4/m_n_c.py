from queue import PriorityQueue


def reconstructPath(path):
    '''
    Formats the path into a readable sequence of steps
    '''
    steps = []
    for i, state in enumerate(path):
        missionaries_left, cannibals_left, boat = state
        missionaries_right = missionaries - missionaries_left
        cannibals_right = cannibals - cannibals_left
        steps.append(f"Step {i} = L: ({missionaries_left}, {cannibals_left}) | R: ({missionaries_right}, {cannibals_right}) | Boat: {boat}")
    return '\n'.join(steps)


def dfs_rule(next, visited, missionaries, cannibals, boat, capacity):
    '''
    Generate all possible states from the current state
    '''
    x, y, boat = next
    possible_states = []

    # Rules
    # forbidden: x < y except when x == 0
    # allowed x >= y
    # moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)] # 3M3C
    moves = [(m, c) for m in range(capacity + 1) 
             for c in range(capacity + 1) 
             if 1 <= m + c <= capacity]  # generalized

    for m, c in moves:
        if boat == 'L':
            new_state = (x - m, y - c, 'R')
        else:
            new_state = (x + m, y + c, 'L')

        # rule check
        left_m, left_c = new_state[:2]
        right_m, right_c = missionaries - left_m, cannibals - left_c

        if (0 <= left_m <= missionaries and 0 <= left_c <= cannibals and
            (left_m == 0 or left_m >= left_c) and  # Left side
            (right_m == 0 or right_m >= right_c) and  # Right side
            new_state not in visited):
            possible_states.append(new_state)

    return possible_states


def missionaries_cannibals(missionaries: int, cannibals: int, capacity: int):
    '''
    Depth First Search adapted for missionaries and cannibals  
    missionaries: no. of missionaires on L  
    cannibals: no. of cannibals on L  
    We are dealing with nos on L as R can be inferred  
    '''
    stack = [(missionaries, cannibals, 'L')]
    visited = set()
    visited.add((missionaries, cannibals, 'L'))
    path = []

    while stack:
        next = stack.pop()
        path.append(next)
        
        if next == (0, 0, 'R'):  # goal state ie. all have reached the right side
            return reconstructPath(path)

        direction = next[-1]
        for new in dfs_rule(next, visited, missionaries, cannibals, direction, capacity):
            if new not in visited:
                stack.append(new)
                visited.add(new)

    return "No solution found"


if __name__ == "__main__":
    missionaries = int(input("Number of missionaries: "))
    cannibals = int(input("Number of cannibals: "))
    capacity = int(input("Capacity of boat: "))

    path = missionaries_cannibals(missionaries, cannibals, capacity)
    print("Solution:\n", path)
