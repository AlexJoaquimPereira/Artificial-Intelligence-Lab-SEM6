import math

board = [' ' for _ in range(9)]

def is_winner(board, player):
    '''
    Hardcoded winning combinations
    '''
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # row
        [0,3,6], [1,4,7], [2,5,8],  # column
        [0,4,8], [2,4,6]            # diagonal
    ]
    for pos in win_conditions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_terminal(board):
    '''
    Implictly returns True if we have a winner else False
    '''
    return is_winner(board, 'X') or is_winner(board, 'O') or ' ' not in board

def utility(board):
    if is_winner(board, 'X'): return -1
    if is_winner(board, 'O'): return 1
    return 0

def minimax(j, is_max):
    '''
    Generalized minimax function
    '''
    if is_terminal(j):
        return utility(j)

    if is_max:
        v = -math.inf
        for i in range(9):
            if j[i] == ' ':
                j[i] = 'O'
                v = max(v, minimax(j, False))
                j[i] = ' '
        return v
    else:
        v = math.inf
        for i in range(9):
            if j[i] == ' ':
                j[i] = 'X'
                v = min(v, minimax(j, True))
                j[i] = ' '
        return v

def best_move(board):
    '''
    Best move for AI (it will always win/draw)
    '''
    best_val = -math.inf
    move = -1
    for i in range(9): # branching factor is always 9 for tictactoe
        if board[i] == ' ':
            board[i] = 'O'
            # display(board) # prints the next step thinking
            move_val = minimax(board, False) # since AI is minimizing player
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

def display(board):
    for i in range(3):
        print(board[i * 3], '|', board[i * 3 + 1], '|', board[i * 3 + 2])
        if i < 2:
            print('--+---+--')

def play():
    print("Welcome to Tic Tac Toe!")
    print("You are X, AI is O")
    while True:
        display(board)
        if is_terminal(board):
            break
        pos = int(input("Enter position (1-9): "))
        pos = pos - 1
        if board[pos] == ' ':
            board[pos] = 'X'
        else:
            print("Invalid move.")
            continue
        if is_terminal(board):
            break
        ai_move = best_move(board)
        board[ai_move] = 'O'

    display(board)
    if is_winner(board, 'X'):
        print("Player wins!")
    elif is_winner(board, 'O'):
        print("AI wins!")
    else:
        print("Draw!")

if __name__ == "__main__":
    play()