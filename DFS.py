import os
from Puzzle import Puzzle

dfs_output = open(os.path.dirname(__file__) + "/output/puzzleDFS.txt", "w+")


class DFS:

    def __init__(self, p):
        self.open = [p.puzzle]  # Adds the initial puzzle
        self.closed = []

    def search(self):
        """
        Performs a dept first search on the puzzle
        :return: Nothing
        """
        # While open is not empty
        while len(self.open) != 0:
            # Remove leftmost state from open
            current_puzzle = self.open[0]
            self.open.remove(current_puzzle)
            self.closed.append(current_puzzle)

            print("Puzzle: " + str(current_puzzle))
            if not Puzzle.is_puzzle_solved(current_puzzle):
                # Generate children of a
                possible_moves = Puzzle.get_possible_moves(current_puzzle)
                children = []
                for move in possible_moves:
                    child = Puzzle.move(move, current_puzzle)
                    children.append(child)

                # Remove child if it is in the open or closed list
                to_remove = []
                for child in children:
                    if child in self.open:
                        to_remove.append(child)
                    elif child in self.closed:
                        to_remove.append(child)

                for r in to_remove:
                    children.remove(r)

                # Put remaining children on left end of open
                self.open = children + self.open

                # Write to txt file
                pos = current_puzzle.index(0)
                Puzzle.write_to_txt(dfs_output, Puzzle.get_tile_letter(pos), current_puzzle)
            else:
                return
