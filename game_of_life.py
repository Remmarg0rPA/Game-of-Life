#!/usr/bin/python3
import random
from colorama import init, Fore, Back, Style
init()

def dead_state(width, height):
    board = [[0 for col in range(width)] for row in range(height)]
    return board


def random_state(width, height, alive_threashold=0.5):
    board = [[1 if random.random() > alive_threashold else 0 for col in range(width)] for row in range(height)]
    return board


def next_board_state(board):
    '''
    1. Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
    2. Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
    3. Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
    4. Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
    '''
    next_board = dead_state(len(board[0]), len(board))

    def try_board_coord(board, row,col):
        try:
            return board[row][col]
        except:
            return 0

    for row in range(len(board)):
        for col in range(len(board[0]):
            sum = 0
            sum += try_board_coord(board, row+1, col-1)
            sum += try_board_coord(board, row+1, col)
            sum += try_board_coord(board, row+1, col+1)
            sum += try_board_coord(board, row, col-1)
            sum += try_board_coord(board, row, col)
            sum += try_board_coord(board, row, col+1)
            sum += try_board_coord(board, row-1, col-1)
            sum += try_board_coord(board, row-1, col)
            sum += try_board_coord(board, row-1, col+1)
            if sum in (0,1):
                next_board[row][col] = 0
            elif sum in (2,3):
                next_board[row][col] = 1 if (board[row][col] or sum == 3) else 0
            else:
                next_board[row][col] = 0

    return next_board


def render(board, *, color=False, alive = '#', dead = '-'):
    width = len(board[0])
    height = len(board)

    for row in range(height):
        for col in range(width):
            c = board[row][col]
            if c:
                if color:
                    print(Fore.GREEN, Back.GREEN, alive, end='', sep='')
                else:
                    print(alive, end='')
            else:
                if color:
                    print(Fore.BLACK, Back.BLACK, dead, end='', sep='')
                else:
                    print(dead, end='')
            print(Style.RESET_ALL, end='')
        print()



render(random_state(60,30, alive_threashold=0.8), color=True)
