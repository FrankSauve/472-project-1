import random
import os
from Puzzle import Puzzle
from DFS import DFS
from BFS import BFS

# Output files

bfs_h1_output = open(os.path.dirname(__file__) + "/output/puzzleBFS-h1.txt", "w+")
bfs_h2_output = open(os.path.dirname(__file__) + "/output/puzzleBFS-h2.txt", "w+")
a_star_h1_output = open(os.path.dirname(__file__) + "/output/puzzleAs-h1.txt", "w+")
a_star_h2_output = open(os.path.dirname(__file__) + "/output/puzzleAs-h2.txt", "w+")

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
puzzle = Puzzle(input_puzzle)

# Output result to txt file
# puzzle.write_to_txt(dfs_output, puzzle.get_tile_letter(1, 1), puzzle.puzzle)

# print('\nPossible moves: \n' + str(puzzle.get_possible_moves()))

# dfs = DFS(puzzle)
# dfs.search()

# dfs.puzzle.print()

bfs = BFS(puzzle)
bfs.search_h1()

