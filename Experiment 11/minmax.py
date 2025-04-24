# Tic-Tac-Toe using MinMax algorithm
import math

board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print(board[i * 3], '|', board[i * 3 + 1], '|', board[i * 3 + 2])
        if i < 2:
            print('--+---+--')

def check_winner(brd, player):
    win_pos = [(0,1,2), (3,4,5), (6,7,8),  # row
               (0,3,6), (1,4,7), (2,5,8),  # column
               (0,4,8), (2,4,6)]           # diagonal
    for pos in win_pos:
        if brd[pos[0]] == brd[pos[1]] == brd[pos[2]] == player:
            return True
    return False

def is_full(brd):
    '''
    Check if board is full
    '''
    return ' ' not in brd

def minimax(brd, is_maximizing):
    '''
    Min-Max function
    '''
    # giving calls to terminal function
    if check_winner(brd, 'O'):
        return 1
    elif check_winner(brd, 'X'):
        return -1
    elif is_full(brd):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                value = minimax(brd, False)
                brd[i] = ' '
                best = max(best, value)
        return best
    else:
        best = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                value = minimax(brd, True)
                brd[i] = ' '
                best = min(best, value)
        return best

def best_move():
    '''
    best move for AI
    '''
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

def play():
    print("Welcome to Tic Tac Toe!")
    print_board()
    while True:
        # Player move
        move = int(input("Enter your move X (1-9): "))
        if board[move - 1] != ' ':
            print("Invalid move!")
            continue
        board[move - 1] = 'X'

        if check_winner(board, 'X'):
            print_board()
            print("You win!")
            break

        if is_full(board):
            print_board()
            print("It's a draw!")
            break

        # AI move
        ai = best_move()
        board[ai] = 'O'
        print("\nAI played:")
        print_board()

        if check_winner(board, 'O'):
            print("AI wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play()
