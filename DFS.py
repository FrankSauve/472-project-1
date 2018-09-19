
class DFS:

    def __init__(self, p):
        self.puzzle = p
        self.open = [p.get_position(0)] # Adds the initial position of the 0
        self.close = []

    def search(self):
        # While open is empty
        while len(self.open) != 0:
            # Remove leftmost state from open
            x = self.open.pop()

            if not self.puzzle.is_puzzle_solved():
                # Generate children of X
                children = self.puzzle.get_possible_moves()

                # Put x on closed list
                self.close.append(x)

                # Discard children of x if already in open or closed
                for child in children:
                    if child in self.open:
                        children.remove(child)
                    elif child in self.close:
                        children.remove(child)

                # Put remaining children on left end of open
                self.open.append(children)

                x, y = children[0]
                self.puzzle.move(x, y)
            else:
                return self.puzzle
