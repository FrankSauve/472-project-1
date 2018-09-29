import os
from Puzzle import Puzzle

bfs_h1_output = open(os.path.dirname(__file__) + "/output/puzzleBFS-h1.txt", "w+")
bfs_h2_output = open(os.path.dirname(__file__) + "/output/puzzleBFS-h2.txt", "w+")


class BFS:

    def __init__(self, p):
        self.current_puzzle = p.puzzle
        self.open = [self.current_puzzle]
        self.closed = []
        self.h_option = input("\nWhich heuristic do you want to use? (1,2)\n1. Number of incorrectly place tiles\n"
                        "2. Total distance of each tile to where they should be\n")

    def search(self):
        """
        Solves the puzzle using best first search
        """

        while len(self.open) != 0:
            self.current_puzzle = self.open[0]
            self.open.remove(self.current_puzzle)
            self.closed.append(self.current_puzzle)

            print("Puzzle: " + str(self.current_puzzle))

            # Write to txt file
            pos = self.current_puzzle.index(0)
            if self.h_option == "1":
                txt_output = bfs_h1_output
            elif self.h_option == "2":
                txt_output = bfs_h2_output
            else:
                raise Exception("Invalid heuristic option.")
            Puzzle.write_to_txt(txt_output, Puzzle.get_tile_letter(pos), self.current_puzzle)

            # If the puzzle is not the in the goal state
            if not Puzzle.is_puzzle_solved(self.current_puzzle):

                # Get the possible moves sorted from best to worst
                possible_moves = Puzzle.get_possible_moves(self.current_puzzle)
                possible_scores = self.get_scores(possible_moves)
                score_move = self.get_sorted_tuples(possible_moves, possible_scores)

                # Generate the children of current puzzle
                children = []
                for sm in score_move:
                    score, move = sm
                    child = Puzzle.move(move, self.current_puzzle)
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

                # Put remaining children on right end of open because we use a priority queue
                self.open = self.open + children

            else:
                return

    def get_scores(self, moves):
        """
        Gets the heuristic score of the moves
        :param list moves: The list of possible moves
        :return list scores: The list of scores for each move
        """
        i = 0
        scores = []
        while i < len(moves):
            temp_puzzle = Puzzle.move(moves[i], self.current_puzzle)
            if self.h_option == "1":
                scores.append(self.get_h1(temp_puzzle))
            elif self.h_option == "2":
                scores.append(self.get_h2(temp_puzzle))
            else:
                raise Exception("Invalid heuristic option.")
            i = i + 1

        return scores

    @staticmethod
    def get_h1(puzzle):
        """
        Calculates heuristic h1
        :return: int a, which is the number of incorrectly placed elements
        """
        i = 0
        a = 0
        while i < len(puzzle)-1:  # len()-1 since 0 should be at the last position
            if puzzle[i] != (i+1):
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
        total_distance = 0
        for i, p in enumerate(puzzle):
            index = i + 1
            if p == 0:  # If the tile has the zero, it should be at index 12
                p = 12
            distance = p - index
            if distance < 0:  # If the distance is negative, make it positive
                distance = distance * (-1)
            total_distance = total_distance + distance
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
