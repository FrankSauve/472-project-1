import os
from Puzzle import Puzzle
from DFS import DFS

# Output files TODO: These paths will go in the respecting classes
a_star_h1_output = open(os.path.dirname(__file__) + "/output/puzzleAs-h1.txt", "w+")
a_star_h2_output = open(os.path.dirname(__file__) + "/output/puzzleAs-h2.txt", "w+")

# Asks the user for the initial puzzle TODO: Commented to make testing faster
# input_puzzle = input("Enter the board separated by commas: ").replace(" ", "").split(",")
input_puzzle = "5,1,2,3,9,6,7,4,0,10,11,8".split(",")  # TODO: Remove for release

option = input("Which algorithm do you ant to use? (1,2,3)\n1. DFS \n2. BFS \n3. A*\n")

# Converts to int
input_puzzle = list(map(int, input_puzzle))

# Check if the input_puzzle is of length 12
# if len(input_puzzle) != 12:
    # raise Exception("Puzzle must have 12 tiles")

puzzle = Puzzle(input_puzzle)

if option == "1":
    dfs = DFS(puzzle)
    print("N = " + str(puzzle.get_n()) + ", M = " + str(puzzle.get_m()))
    dfs.search()
elif option == "2":
    # TODO: Put BFS here
    None
elif option == "3":
    # TODO: Put A* here
    None
else:
    raise Exception("Invalid option. Option must be (1,2,3)")



