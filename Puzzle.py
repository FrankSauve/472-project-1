goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
class Puzzle:

    def __init__(self, p):
        # Creates empty 4x3 2D array
        self.puzzle = p
        self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]  # Goal state of the puzzle


    @staticmethod
    def is_puzzle_solved(puzzle):
        """
        Returns whether or not the puzzle is in the goal state
        :return boolean
        """
        global goal
        if puzzle == goal:
            return True
        else:
            return False

    def write_to_txt(self, file, letter, puzzle):
        """
        Write the letter and the current state of the puzzle to a txt file
        :param file: File to write to
        :param str letter: The letter of the tile of the current move
        :param list puzzle: The current state of the puzzle after the move
        """
        file.write(letter + " " + str(puzzle) + "\n")

    @staticmethod
    def get_possible_moves(puzzle):
        """
        Returns (x,y) coordinates of possible positions for the 0 tile.
        Ordered clockwise as the requirements state they should be
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
        if (pos >= 5 and pos <= 7) or (pos >= 9 and pos <= 11):
            moves.append(pos - 5)

        return moves

    @staticmethod
    def temp_move(new_pos, puzzle):
        """
        Returns the puzzle after a potential move
        :param new_x: New row position of the 0
        :param new_y: New col position of the 0
        :return list new_puzzle: 2D array of the puzzle after the move
        """
        new_puzzle = puzzle
        current_pos = puzzle.index(0)
        value = puzzle[new_pos]
        new_puzzle[current_pos] = value
        new_puzzle[new_pos] = 0
        return new_puzzle

    @staticmethod
    def get_tile_letter(pos):
        """
        Returns the letter of the tile of the given (x,y) coordinate
        :param int x : The index of the row
        :param int y L The index of the col
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
            raise Exception("Invalid (x,y) coordinates.")

        return letter
