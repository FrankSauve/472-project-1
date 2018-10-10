import os
from src.Puzzle import Puzzle
from src.Spot import Spot

bfs_h1_output = open(os.path.dirname(__file__) + "/../output/puzzleBFS-h1.txt", "w+")
bfs_h2_output = open(os.path.dirname(__file__) + "/../output/puzzleBFS-h2.txt", "w+")
bfs_h3_output = open(os.path.dirname(__file__) + "/../output/puzzleBFS-h3.txt", "w+")


class BFS:

    def __init__(self, p):
        self.current_puzzle = p.puzzle
        self.current_spot = Spot(self.current_puzzle)
        self.open = [self.current_spot]
        self.closed = []
        self.h_option = input("\nWhich heuristic do you want to use? (1,2,3)\n1. Number of incorrectly place tiles\n"
                        "2. Total distance of each tile to where they should be\n"
                        "3. Manhattan distance\n")

    def search(self):
        """
        Performs a best first search on the puzzle
        """
        while len(self.open) != 0:

            # If the puzzle is not the in the goal state
            if not Puzzle.is_puzzle_solved(self.current_puzzle):

                # Find the spot with the best h score
                winner_index = 0
                for i, o in enumerate(self.open):
                    if self.open[i].h < self.open[winner_index].h:
                        winner_index = i

                self.current_puzzle = self.open[0]

                # Current spot becomes the the winner
                self.current_spot = self.open[winner_index]
                self.current_puzzle = self.current_spot.puzzle

                # Remove from open current from open list
                self.remove_puzzle_from_spots_list(self.open, self.current_spot.puzzle)
                # Add to closed list
                self.closed.append(self.current_spot)

                print("Puzzle: " + str(self.current_puzzle))

                # Write to txt file
                pos = self.current_puzzle.index(0)
                if self.h_option == "1":
                    txt_output = bfs_h1_output
                elif self.h_option == "2":
                    txt_output = bfs_h2_output
                elif self.h_option == "3":
                    txt_output = bfs_h3_output
                else:
                    raise Exception("Invalid heuristic option.")
                Puzzle.write_to_txt(txt_output, Puzzle.get_tile_letter(pos), self.current_puzzle)

                # Get the possible moves sorted from best to worst
                possible_moves = Puzzle.get_possible_moves(self.current_puzzle)

                # Generate the possible moves
                possible_moves = Puzzle.get_possible_moves(self.current_puzzle)
                children = []
                for move in possible_moves:
                    child = Spot(Puzzle.move(move, self.current_puzzle))
                    child.h = self.get_h(list(child.puzzle))
                    children.append(child)

                # Remove child if it is in the open or closed list
                to_remove = []
                for child in children:
                    for o in self.open:
                        if list(child.puzzle) == list(o.puzzle):
                            to_remove.append(child)
                    for c in self.closed:
                        if list(child.puzzle) == list(c.puzzle):
                            if child not in to_remove:
                                to_remove.append(child)
                for r in to_remove:
                    children.remove(r)

                # Put remaining children on right end of open because we use a priority queue
                self.open = self.open + children

            else:
                return
        print(self.current_puzzle)

    def get_h(self, puzzle):
        """
        Gets the heuristic score of the moves
        :param list moves: The list of possible moves
        :return list scores: The list of scores for each move
        """
        if self.h_option == "1":
            scores = Puzzle.get_h1(puzzle)
        elif self.h_option == "2":
            scores = Puzzle.get_h2(puzzle)
        elif self.h_option == "3":
            scores = Puzzle.get_h3(puzzle)
        else:
            raise Exception("Invalid heuristic option.")

        return scores

    def remove_puzzle_from_spots_list(self, spots, puzzle):
        """
        Removes a puzzle from spots list
        :param list spots: List of Spot objects
        :param list puzzle: The puzzle to remove
        """
        to_remove = None
        for spot in spots:
            if list(spot.puzzle) == list(puzzle):
                to_remove = spot

        if to_remove is not None:
            self.open.remove(to_remove)