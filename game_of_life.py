#!/usr/bin/python3
import random
from os import system
from time import sleep
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
    width, height = len(board[0]), len(board)
    next_board = dead_state(width, height)

    def try_board_coord(board, row, col):
        try:
            if row < 0 or col < 0:
                return 0
            return board[row][col]
        except:
            return 0

    for row in range(len(board)):
        for col in range(len(board[0])):
            sum = 0
            sum += board[row+1][col-1] if row < height-1 and col > 0 else 0
            sum += board[row+1][col] if row < height-1 else 0
            sum += board[row+1][col+1] if row < height-1 and col < width-1 else 0
            sum += board[row][col-1] if col > 0 else 0

            sum += board[row][col+1] if col < width-1 else 0
            sum += board[row-1][col-1] if row > 0 and col > 0 else 0
            sum += board[row-1][col] if row > 0 else 0
            sum += board[row-1][col+1] if row > 0 and col < width-1 else 0
            if sum == 0 or sum == 1:
                next_board[row][col] = 0
            elif sum == 2:
                next_board[row][col] = 1 if board[row][col] == 1 else 0
            elif sum == 3:
                next_board[row][col] = 1
            else:
                next_board[row][col] = 0

    return next_board


def render(board, *, color=False, alive = '#', dead = '-', erase=False):
    width = len(board[0])
    height = len(board)

    if erase:
        system('clear')
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


if __name__ == '__main__':
    board = random_state(70,35, alive_threashold=0.7)
    render(board, color=True)
    while True:
        board = next_board_state(board)
        render(board, color=True, erase=True)
        sleep(0.05)
