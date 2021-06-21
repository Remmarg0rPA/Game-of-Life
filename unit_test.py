#!/usr/bin/python3
from game_of_life import next_board_state

# TODO: there's a lot of repeated code here. Can
# you move some of into reusable functions to
# make it shorter and neater?

def check_state(expected, actual, num):
    if expected == actual:
        print(f"PASSED {num}")
    else:
        print(f"FAILED {num}!")
        print("Expected:")
        for r in expected:
            print('\t', r)
        print("Actual:")
        for a in actual:
            print('\t', a)


if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state = next_board_state(init_state)
    check_state(expected_next_state, actual_next_state, 1)

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state = next_board_state(init_state)
    check_state(expected_next_state, actual_next_state, 2)

    # TEST 3: dead cells with exactly 1 neighbors
    # should be dead.
    init_state = [
        [0,0,0],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state = next_board_state(init_state)
    check_state(expected_next_state, actual_next_state, 3)

    # TEST 4: alive cells with more than 3 neighbors
    # should be dead.
    init_state = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]
    expected_next_state = [
        [1,0,1],
        [0,0,0],
        [1,0,1]
    ]
    actual_next_state = next_board_state(init_state)
    check_state(expected_next_state, actual_next_state, 4)
