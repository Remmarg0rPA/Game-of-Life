#!/usr/bin/python3
from game_of_life import next_board_state

# TODO: there's a lot of repeated code here. Can
# you move some of into reusable functions to
# make it shorter and neater?

def check_state(expexted, actual, num):
    if expected == actual:
        print(f"PASSED {num}")
    else:
        print(f"FAILED {num}!")
        print("Expected:")
        print(expected)
        print("Actual:")
        print(actual)


if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state1 = next_board_state(init_state1)
    check_state(expected_next_state1, actual_next_state1, 1)

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state2 = next_board_state(init_state2)
    check_state(expected_next_state2, actual_next_state2, 2)
