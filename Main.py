import os
from Puzzle import Puzzle
from DFS import DFS

# Output files TODO: These paths will go in the respective classes
a_star_h1_output = open(os.path.dirname(__file__) + "/output/puzzleAs-h1.txt", "w+")
a_star_h2_output = open(os.path.dirname(__file__) + "/output/puzzleAs-h2.txt", "w+")

# Asks the user for the initial puzzle TODO: Commented to make testing faster
# input_puzzle = input("Enter the board separated by commas: ").replace(" ", "").split(",")
# input_puzzle = "5,1,2,3,9,6,7,4,0,10,11,8".split(",")  # TODO: Remove for release
input_puzzle = "1,0,3,7,5,2,6,4,9,10,11,8".split(",")

option = input("Which algorithm do you want to use? (1,2,3)\n1. DFS \n2. BFS \n3. A*\n")

# Converts to int
input_puzzle = list(map(int, input_puzzle))

puzzle = Puzzle(input_puzzle)

if len(puzzle.puzzle) < 2:
    raise Exception("Invalid puzzle size: Puzzles must be at least two tiles large.\nExiting Program...")
puzzle.goal_gen()
if not puzzle.is_puzzle_solvable():
    option_continue = input("This puzzle may not be solvable, do you want to continue? (Y/N)\n")
    if option_continue == 'N' or option_continue == 'n':
        print("Exiting Program...")
        exit()
print("\nExecuting search...\n\n")

puzzle.set_rows_and_columns()

if option == "1":
    dfs = DFS(puzzle)
    dfs.search()
elif option == "2":
    # TODO: Put BFS here
    None
elif option == "3":
    # TODO: Put A* here
    None
else:
    raise Exception("Invalid option. Option must be (1,2,3)")



