import math

goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
rows = 0
columns = 0
first_step = True


class Puzzle:

    def __init__(self, p):
        self.puzzle = p

    def set_rows_and_columns(self):
        """
        Assigns the number of rows and columns that the puzzle should have given its length into the rows and columns global variables
        """
        global rows
        global columns

        columns = self.get_n()
        rows = self.get_m()

    def is_puzzle_solvable(self):
        """
        Checks the puzzle to see whether it is solvable using the sum of permutation inversions method
        :return: boolean
        """
        permutation_inversions = []

        i = 0
        while i < len(self.puzzle):
            current_val = self.puzzle[i]
            right_placements = 0

            j = i + 1
            while j < len(self.puzzle):
                if (current_val > self.puzzle[j]) and (self.puzzle[j] != 0):
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

        global goal
        goal = []
        i = 0
        while i < len(self.puzzle):
            if i == len(self.puzzle)-1:
                goal.append(0)
            else:
                goal.append(i + 1)
            i += 1

    def get_m(self):
        """
        This method returns the number of rows in a tile puzzle
        :param list puzzle: the puzzle's current state
        :return: int m: the number of rows for the puzzle
        """

        length = float(len(self.puzzle))
        n = int(math.sqrt(length))
        if n ** 2 == int(length):  # check square case
            return n
        while n > 0:
            m = length / n
            if m.is_integer():
                return n
            n -= 1

    def get_n(self):
        """
        This method returns the number of columns in a tile puzzle
        :param list puzzle: the puzzle's current state
        :return: int n: the number of columns for the puzzle
        """
        return int(len(self.puzzle) / self.get_m())

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
    def get_possible_moves(puzzle):
        """
        Returns (x,y) coordinates of possible positions for the 0 tile.
        Ordered clockwise as the requirements state they should be
        :param list puzzle: The current state of the puzzle
        :return list moves: The list of possible moves as (x,y) coordinates
        """
        pos = puzzle.index(0)
        moves = []

        if pos >= columns:  # up
            moves.append(pos - columns)
        if pos >= columns and pos % columns != (columns - 1):  # up-right
            moves.append(pos - (columns - 1))
        if pos % columns != (columns - 1):  # right
            moves.append(pos + 1)
        if (len(puzzle) > pos + columns + 1) and (pos % columns != (columns - 1)):  # down-right
            moves.append(pos + (columns + 1))
        if pos < len(puzzle) - columns:  # down
            moves.append(pos + columns)
        if (pos < len(puzzle) - columns) and (pos % columns > 0):  # down-left
            moves.append(pos + (columns - 1))
        if pos % columns > 0:  # left
            moves.append(pos - 1)
        if (pos >= columns) and (pos % columns > 0):  # up-left
            moves.append(pos - (columns + 1))

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
        Returns the letter of the tile of the given pos
        :param int pos : The number of the tile to search
        :return str letter: The letter of tile at pos
        """
        return str(chr(97+pos))

    @staticmethod
    def get_h1(puzzle):
        """
        Calculates heuristic h1
        :return: int a, which is the number of incorrectly placed elements
        """
        i = 0
        a = 0
        while i < len(puzzle) - 1:  # len()-1 since 0 should be at the last position
            if puzzle[i] != (i + 1):
                a = a + 1
            i = i + 1
        return a

    @staticmethod
    def get_h2(puzzle):
        """
        Calculates heuristic h2: The sum of the distances of where each tile should be
        :param list puzzle: Current state of the puzzle
        :return: int total_distance: Sum of the distances of where the tile should be
        """
        i = 0
        distance = 0
        total_distance = 0

        while i < len(puzzle):

            if puzzle[i] != (i + 1):  # If a tile doesn't have the value of it's goal state
                current_location = i
                current_location_mod = i % columns
                if puzzle[i] == 0 and i != len(puzzle) - 1:  # Check 0 case
                    goal_location = len(puzzle) - 1
                    goal_location_mod = goal_location % columns
                else:
                    goal_location = puzzle[i] - 1
                    goal_location_mod = goal_location % columns
                distance = 0

                while current_location < goal_location:  # Current location is above the goal location
                    if current_location_mod < goal_location_mod and goal_location - columns < current_location:  # x+1
                        current_location += 1
                        current_location_mod += 1
                    elif current_location_mod < goal_location_mod:  # x+c+1
                        current_location += columns + 1
                        current_location_mod += 1
                    elif current_location_mod == goal_location_mod:  # x+c
                        current_location += columns
                    else:  # x+c-1
                        current_location += columns - 1
                        current_location_mod -= 1
                    distance += 1

                while current_location > goal_location:
                    if current_location_mod < goal_location_mod:  # x-c+1
                        current_location -= columns - 1
                        current_location_mod += 1
                    elif current_location_mod == goal_location_mod:  # Current column is same as goal column
                        current_location -= columns
                    elif current_location_mod > goal_location_mod and goal_location + columns > current_location:  # x-1
                        current_location -= 1
                        current_location_mod -= 1
                    else:  # x-c-1
                        current_location -= columns + 1
                        current_location_mod -= 1
                    distance += 1

            total_distance += distance
            distance = 0
            i = i + 1
        return total_distance

    @staticmethod
    def get_h3(puzzle):
        """
        Calculates heuristic h2: The Manhattan distance of each tile
        :param list puzzle: Current state of the puzzle
        :return: int total_distance: Sum of the distances of where the tile should be
        """
        total_distance = 0
        for i, p in enumerate(puzzle):
            index = i + 1
            if p == 0:  # If the tile has the zero, it should be at index n
                p = len(puzzle)

            # Current x of the tile
            curr_x = index % columns
            if curr_x == 0:  # If its 0 make it column
                curr_x = columns

            # Current y of the tile
            curr_y = math.ceil(index / columns)

            # Goal x position of tile
            goal_x = p % columns
            if goal_x == 0:  # If its 0 make it column
                goal_x = columns

            # Goal y position of tile
            goal_y = math.ceil(p / columns)

            # Total absolute Manhattan distance
            total_distance += abs(goal_x - curr_x) + abs(goal_y - curr_y)

        return total_distance

    @staticmethod
    def get_sorted_tuples(moves, scores):
        """
        Gets the sorted (score, move) tuples
        :param list moves: Possible moves
        :param list scores: Heuristic scores for the moves
        :return list tuples: Sorted list of (score, move) tuples
        """
        tuples = []
        for i in range(len(moves)):
            tuples = tuples + [(scores[i], moves[i])]
        tuples.sort()
        return tuples