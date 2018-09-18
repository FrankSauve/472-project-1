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
        for i in range(3):
            print(self.puzzle[i])

    def get_possible_moves(self):
        """
        Returns (x,y) coordinates of possible positions of the 0 tile
        """
        x, y = self.get_position(0)
        moves = []

        if x > 0:
            moves.append((x - 1, y))
        if y > 0:
            moves.append((x, y - 1))
        if x < 3:
            moves.append((x + 1, y))
        if y < 3:
            moves.append((x, y + 1))

        return moves

    def get_position(self, value):
        """
        Returns the (x,y) coordinates of the value
        :param int value : The value of the tile (0, 11)
        """
        for x in range(3):
            for y in range(4):
                if self.puzzle[x][y] == value:
                    return x, y

    def get_tile_letter(self, x, y):
        """
        Returns the letter of the tile of the given (x,y) coordinate
        :param int x : The index of the row
        :param int y L The index of the col
        """
        letter = ""
        if x == 0:
            if y == 0:
                letter = "a"
            elif y == 1:
                letter = "b"
            elif y == 2:
                letter = "c"
            elif y == 3:
                letter = "d"
        elif x == 1:
            if y == 0:
                letter = "e"
            elif y == 1:
                letter = "f"
            elif y == 2:
                letter = "g"
            elif y == 3:
                letter = "h"
        elif x == 2:
            if y == 0:
                letter = "i"
            elif y == 1:
                letter = "j"
            elif y == 2:
                letter = "k"
            elif y == 3:
                letter = "l"

        if letter == "":
            raise Exception("Invalid (x,y) coordinates.")

        return letter
