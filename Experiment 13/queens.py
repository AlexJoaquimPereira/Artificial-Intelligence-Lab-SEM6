# Eight queens problem
# use heuristic like how many queens attacking each other etc
# try interchanging or giving random values
# I think it's minimax or alpha beta pruning ie. advanced BnB
import math
import random

# Board for the queen ie queenboard[6] = 2 -> second queen in 6th row
# 1D board enough for the queens
queenboard = [0 for _ in range(8)]

def print_board(board):
    '''
    Display board with queens
    '''
    for row in range(8):
        line = ""
        for col in range(8):
            if board[col] == row:
                line += " Q "
            else:
                line += " + "
        print(line)

def heuristic(board):
    '''
    h(x): No. of queens attacking each other. 
    '''
    value = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                value += 1
    return value

def randomizer(board):
    '''
    Give two random nos corresponding to rows
    Use these two nos to interchange queens and check if the heuristic is lower
    if yes then this is the new board
    else randomize again
    '''
    a, b = random.sample(range(8), 2)
    board[a], board[b] = board[b], board[a]

def eight_queens():
    '''
    Eight queens problem
    '''
    global queenboard
    max_iterations = 1000
    current_h = heuristic(queenboard)
    iterations = 0

    while current_h != 0 and iterations < max_iterations:
        new_board = queenboard[:]
        randomizer(new_board)
        new_h = heuristic(new_board)

        if new_h < current_h:
            queenboard = new_board
            current_h = new_h

        iterations += 1
        print(f"\nIteration {iterations}:")
        print_board(queenboard)

    if current_h == 0:
        print("\nSolution Found:")
        print(queenboard)
        print_board(queenboard)
    else:
        print("\nFailed to find solution.")
        print("Unoptimal board state:")
        print(queenboard) # in the list form
        print_board(queenboard)

if __name__ == "__main__":
    print("Enter the eight positions (0 to 7):")
    
    while True:
          inputs = list(map(int, input().split()))
          if len(inputs) == 8 and all(0 <= x <= 7 for x in inputs):
               queenboard = inputs
               break
          else:
               print("Invalid input. Enter exactly 8 integers between 0 and 7.")

    print("\nInitial Board:")
    print_board(queenboard)
    
    eight_queens()
