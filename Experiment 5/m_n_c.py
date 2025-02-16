from collections import deque

def dfs_rule(state, visited, missionaries, cannibals, capacity):
    """
    Generate all possible states from the current state
    """
    x, y, boat = state
    possible_states = []
    
    # Generate moves dynamically based on boat capacity
    moves = [(m, c) for m in range(capacity + 1) for c in range(capacity + 1) if 1 <= m + c <= capacity]

    for m, c in moves:
        if boat == 'L':  # Move from Left to Right
            new_state = (x - m, y - c, 'R')
        else:  # Move from Right to Left
            new_state = (x + m, y + c, 'L')

        # Validity Checks
        left_m, left_c = new_state[:2]
        right_m, right_c = missionaries - left_m, cannibals - left_c

        if (0 <= left_m <= missionaries and 0 <= left_c <= cannibals and
            0 <= right_m <= missionaries and 0 <= right_c <= cannibals and
            (left_m == 0 or left_m >= left_c) and  # Left bank condition
            (right_m == 0 or right_m >= right_c) and  # Right bank condition
            new_state not in visited):
            possible_states.append(new_state)

    return possible_states
    

def missionaries_cannibals(missionaries, cannibals, capacity):
    """
    Depth First Search adapted for generalized missionaries and cannibals problem
    """
    stack = [(missionaries, cannibals, 'L')]
    visited = set()
    visited.add((missionaries, cannibals, 'L'))
    path = []

    while stack:
        state = stack.pop()
        path.append(state)

        if state == (0, 0, 'R'):  # Goal state: all reached Right side
            return path  

        for new_state in dfs_rule(state, visited, missionaries, cannibals, capacity):
            if new_state not in visited:
                stack.append(new_state)
                visited.add(new_state)

    return None


if __name__ == "__main__":
    missionaries = int(input("Enter number of missionaries: "))
    cannibals = int(input("Enter number of cannibals: "))
    capacity = int(input("Enter boat capacity: "))
    
    path = missionaries_cannibals(missionaries, cannibals, capacity)
    
    if path:
        print("Solution Path:", path)
    else:
        print("No solution found.")
