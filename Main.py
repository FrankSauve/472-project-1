import sys
import random
from Puzzle import Puzzle

# Asks the user for the initial puzzle TODO: Commented to make testing faster
# input_puzzle = input("Enter the board separated by commas: ").replace(" ", "").split(",")
input_puzzle = "1,0,3,7,5,2,6,4,9,10,11,8".split(",")  # TODO: Remove for release

# Converts to int
input_puzzle = list(map(int, input_puzzle))

# Shuffles the puzzle TODO: Remove for release
# random.shuffle(input_puzzle)

# Check if the input_puzzle is of length 12
if len(input_puzzle) != 12:
    raise Exception("Puzzle must have 12 tiles")

print('Initial puzzle state:')
puzzle = Puzzle()
puzzle.set_puzzle(input_puzzle)
puzzle.print()

print('\nPossible moves: \n' + str(puzzle.get_possible_moves()))
# print(puzzle.get_tile_letter(1, 1))
