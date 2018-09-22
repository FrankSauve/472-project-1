import os
from Puzzle import Puzzle

dfs_output = open(os.path.dirname(__file__) + "/output/puzzleDFS.txt", "w+")

class DFS:

    def __init__(self, p):
        self.open = [p.puzzle]  # Adds the initial puzzle
        self.closed = []

    def search(self):
        # While open is not empty
        # while len(self.open) != 0:
        i = 0
        while i < 15:
            # Remove leftmost state from open
            a = self.open[0]
            self.open.remove(a)
            self.closed.append(a)

            print(a)
            if not Puzzle.is_puzzle_solved(a):
                # Generate children of a
                possible_moves = Puzzle.get_possible_moves(a)
                print("Closed before: " + str(self.closed))

                children = []
                for move in possible_moves:
                    child = Puzzle.temp_move(move, a)
                    children.append(list(child))

                print("children: " + str(children))
                # Put a on closed list

                # Discard children of a if already in open or closed

                for element1 in children:
                    for o in self.open:
                        if element1 == o:
                            children.remove(element1)
                            break

                for element2 in children:
                    for c in self.closed:
                        if element2 == c:
                            children.remove(element2)
                            break


                print("children after remove" + str(children))

                # Put remaining children on left end of open
                self.open = children + self.open

                print("OPEN: " + str(self.open))
                print("CLOSED: " + str(self.closed))
                print("\n")
                i = i + 1
                pos = a.index(0)
                Puzzle.write_to_txt(dfs_output, Puzzle.get_tile_letter(pos), a)
            else:
                return
