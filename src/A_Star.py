import os
from src.Spot import Spot
from src.Puzzle import Puzzle

a_star_h1_output = open(os.path.dirname(__file__) + "/../output/puzzleAs-h1.txt", "w+")
a_star_h2_output = open(os.path.dirname(__file__) + "/../output/puzzleAs-h2.txt", "w+")
a_star_h3_output = open(os.path.dirname(__file__) + "/../output/puzzleAs-h3.txt", "w+")


class AStar:

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
        Performs A* search on the puzzle
        """
        while len(self.open) != 0:
            # If the puzzle is not the in the goal state
            if not Puzzle.is_puzzle_solved(self.current_puzzle):

                # Find the spot with the best F score
                winner_index = 0
                for i, o in enumerate(self.open):
                    if self.open[i].f < self.open[winner_index].f:
                        winner_index = i

                # Current spot becomes the the winner
                self.current_spot = self.open[winner_index]
                self.current_puzzle = self.current_spot.puzzle

                # Remove from open current from open list
                self.remove_puzzle_from_spots_list(self.open, self.current_spot.puzzle)
                # Add to closed list
                self.closed.append(self.current_spot)
                
                # Write to txt file
                pos = self.current_puzzle.index(0)
                if self.h_option == "1":
                    txt_output = a_star_h1_output
                elif self.h_option == "2":
                    txt_output = a_star_h2_output
                elif self.h_option == "3":
                    txt_output = a_star_h3_output
                else:
                    raise Exception("Invalid heuristic option.")
                Puzzle.write_to_txt(txt_output, Puzzle.get_tile_letter(pos), self.current_puzzle)

                # Generate the possible moves
                possible_moves = Puzzle.get_possible_moves(self.current_puzzle)
                children = []
                for move in possible_moves:
                    child = Spot(Puzzle.move(move, self.current_puzzle))
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

                # Loop through all the neighbors
                for neighbor in children:
                    found_in_close = False
                    for c in self.closed:
                        if list(neighbor.puzzle) == list(c.puzzle):
                            found_in_close = True  # Continue to the next neighbor

                    if not found_in_close:
                        temp_g = self.current_spot.g + 1  # Increment g(n)

                        found_in_open = False
                        for o in self.open:
                            if list(neighbor.puzzle) == list(o.puzzle):
                                if temp_g < neighbor.g:
                                    # Give new g score, because I got there faster than the previous path
                                    neighbor.g = temp_g
                                found_in_open = True
                        if not found_in_open:
                            neighbor.g = temp_g
                            self.open.append(neighbor)

                    # Calculate f(n) of neighbor
                    neighbor.h = Puzzle.get_h3(list(neighbor.puzzle))
                    neighbor.f = neighbor.g + neighbor.h

            else:
                return  # Puzzle is solved

            print(self.current_spot.puzzle)

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
