goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
first_step = True


class Puzzle:

    def __init__(self, p):
        # Creates empty 4x3 2D array
        self.puzzle = p
        if len(p) == 12:
            self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]  # Goal state of the puzzle
        else:
            self.goal_gen()
        if not self.is_puzzle_solvable():
            print("Puzzle is not solvable.\nExiting Program...")
            exit()

    def is_puzzle_solvable(self):
        """
        Checks the puzzle to see whether it is solvable using the sum of permutation inversions method
        :return: boolean
        """
        permutation_inversions = []

        i = 0
        while i < len(self.puzzle):
            current_val = self.puzzle[i];
            right_placements = 0

            j = i + 1
            while j < len(self.puzzle):
                if current_val > self.puzzle[j]:
                    right_placements += 1
                j += 1

            i += 1
            permutation_inversions.append(right_placements)

        if sum(permutation_inversions) % 2 == 0:
            return True
        else:
            return False

    def goal_gen(self):
        """
        Modifies the goal state for non 12-tiled puzzles
        """

        self.goal = []
        i = 0
        while i < len(self.puzzle):
            if i == len(self.puzzle)-1:
                self.goal.append(0)
            else:
                self.goal.append(i + 1)
            i += 1

    # TODO: Make a method to find GCD for a given non 12 puzzle to get NxM measurements

    @staticmethod
    def is_puzzle_solved(puzzle):
        """
        Returns whether or not the puzzle is in the goal state
        :return boolean
        """
        global goal
        return puzzle == goal

    @staticmethod
    def write_to_txt(file, letter, puzzle):
        """
        Write the letter and the current state of the puzzle to a txt file
        :param file: File to write to
        :param str letter: The letter of the tile of the current move
        :param list puzzle: The current state of the puzzle after the move
        """
        global first_step
        if first_step:
            letter = "0"
            first_step = False
        file.write(letter + " " + str(puzzle) + "\n")

    @staticmethod
    def get_possible_moves(puzzle):  # TODO: Modify indices to be non 12-tile based
        """
        Returns (x,y) coordinates of possible positions for the 0 tile.
        Ordered clockwise as the requirements state they should be
        :param list puzzle: The current state of the puzzle
        :return list moves: The list of possible moves as (x,y) coordinates
        """
        pos = puzzle.index(0)
        moves = []

        if pos >= 4:  # up
            moves.append(pos - 4)
        if (pos >= 4 and pos <= 6) or (pos >= 8 and pos <= 10):  # up-right
            moves.append(pos - 3)
        if pos % 4 != 3:  # right
            moves.append(pos + 1)
        if (pos >= 0 and pos <= 2) or (pos >= 4 and pos <= 6):  # down-right
            moves.append(pos + 5)
        if pos <= 7:  # down
            moves.append(pos + 4)
        if (pos >= 1 and pos <= 3) or (pos >= 5 and pos <= 7):  # down-left
            moves.append(pos + 3)
        if pos % 4 != 0:  # left
            moves.append(pos - 1)
        if (pos >= 5 and pos <= 7) or (pos >= 9 and pos <= 11): # up-left
            moves.append(pos - 5)

        return moves

    @staticmethod
    def move(new_pos, puzzle):
        """
        Returns the puzzle after a move
        :param int new_pos: New position of the 0
        :param list puzzle: Current state of the puzzle
        :return list new_puzzle: 2D array of the puzzle after the move
        """
        new_puzzle = list(puzzle)
        current_pos = puzzle.index(0)
        value = puzzle[new_pos]
        new_puzzle[current_pos] = value
        new_puzzle[new_pos] = 0
        return new_puzzle

    @staticmethod
    def get_tile_letter(pos):
        """
        Returns the letter of the tile of the given (x,y) coordinate
        :param int pos : The number of the tile to search
        :return str letter: The letter of tile at (x,y)
        """
        letter = ""
        if pos == 0:
            letter = "a"
        if pos == 1:
            letter = "b"
        if pos == 2:
            letter = "c"
        if pos == 3:
            letter = "d"
        if pos == 4:
            letter = "e"
        if pos == 5:
            letter = "f"
        if pos == 6:
            letter = "g"
        if pos == 7:
            letter = "h"
        if pos == 8:
            letter = "i"
        if pos == 9:
            letter = "j"
        if pos == 10:
            letter = "k"
        if pos == 11:
            letter = "l"

        if letter == "":
            raise Exception("Invalid position.")

        return letter
