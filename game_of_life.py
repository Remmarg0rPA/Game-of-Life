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
            sum += try_board_coord(board, row+1, col-1)
            sum += try_board_coord(board, row+1, col)
            sum += try_board_coord(board, row+1, col+1)
            sum += try_board_coord(board, row, col-1)

            sum += try_board_coord(board, row, col+1)
            sum += try_board_coord(board, row-1, col-1)
            sum += try_board_coord(board, row-1, col)
            sum += try_board_coord(board, row-1, col+1)
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
    from os import system
    from time import sleep
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-W', '--width', type=int, help='specify width of board')
    parser.add_argument('-H', '--height', type=int, help='specify height of board')
    parser.add_argument('-C', '--use-color', action='store_true', help='use color when rendering')
    parser.add_argument('-R', '--refresh', '--clear', action='store_true', help='clear/refresh terminal between each rendering')
    parser.add_argument('-A', '--alive-threashold', type=float, help='probability of a cell not being alive when generating the board')

    args = parser.parse_args()
    width  = args.width if args.width else 60
    height = args.height if args.height else 30
    color = args.use_color
    erase = args.refresh
    alive_threashold = args.alive_threashold if args.alive_threashold else 0.5

    board = random_state(width, height, alive_threashold=alive_threashold)
    render(board, color=color)
    while True:
        board = next_board_state(board)
        render(board, color=color, erase=erase)
        sleep(0.05)
