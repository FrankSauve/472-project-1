import sys
import random


class Puzzle:

    def __init__(self):
        # Creates empty 4x3 2D array
        self.puzzle = [[0 for x in range(4)] for y in range(3)]

    def set_puzzle(self, p):
        """
        Populates a 4x3 2D array of the puzzle
        :param list p : list of length 12
        """
        for i, value in enumerate(p):
            if i <= 3:
                self.puzzle[0][i] = value
            elif i <= 7:
                self.puzzle[1][i % 4] = value
            elif i <= 11:
                self.puzzle[2][i % 4] = value

    def print(self):
        """
        Displays the puzzle line by line
        """
        for i in range(0, 3):
            print(self.puzzle[i])


# _________________________ Main code _________________________

# Asks the user for the initial puzzle TODO: Commented to make testing faster
# input_puzzle = input("Enter the board separated by commas: ").replace(" ", "").split(",")
input_puzzle = "0,1,2,3,4,5,6,7,8,9,10,11".split(",")

# Converts to int
input_puzzle = list(map(int, input_puzzle))

# Shuffles the puzzle TODO: Remove for release
random.shuffle(input_puzzle)

# Check if the inputted puzzle is of length 12
if len(input_puzzle) != 12:
    print("ERROR: Puzzle must have 12 tiles")
    sys.exit(-1)

puzzle = Puzzle()
puzzle.set_puzzle(input_puzzle)
puzzle.print()
