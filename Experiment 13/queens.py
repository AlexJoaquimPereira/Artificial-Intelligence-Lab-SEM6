# Eight queens problem
# use heuristic like how many queens attacking each other etc
# try interchanging or giving random values
# I think it's minimax or alpha beta pruning ie. advanced BnB
import math
import random

queenboard = [0 for _ in range(8)] # 1D board enough for the queens

def heuristic(k, i):
     '''
     h(x): No. of queens attacking each other. 
     '''
     value = 0
     for j in range (k-1):
          if((queenboard[j] == i) or (abs(queenboard[j]-i) == abs(j - k))):
               value = value + 1
     return value

def randomizer(k, i):
     '''
     Randomizes the board
     '''
     for j in range (k-1):
          

def eight_queens():
    '''
    Eight queens problem
    '''
    pass

if __name__ == "__main__":
     eight_queens()