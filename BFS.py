import os
from Puzzle import Puzzle

bfs_h1_output = open(os.path.dirname(__file__) + "/output/puzzleBFS-h1.txt", "w+")
bfs_h2_output = open(os.path.dirname(__file__) + "/output/puzzleBFS-h2.txt", "w+")


class BFS:

    def __init__(self, p):
        self.currentPuzzle = p.puzzle
        self.visited = [self.currentPuzzle]

    def search_h1(self):
        """
        The heuristic h(n) is equivalent to the number of incorrectly placed items (excluding 0)
        :return:
        """
        print(self.currentPuzzle)
        print(len(self.currentPuzzle))

        possible_moves = Puzzle.get_possible_moves(self.currentPuzzle)
        possible_move_scores = self.check_moves_h1(possible_moves)
        print("Possible moves: "+str(possible_moves)+", h1(n)'s for moves: "+str(possible_move_scores))

        # TODO: Actually do the algorithm

        return True

    def check_moves_h1(self, moves):

        i = 0
        h1_scores = []
        while i < len(moves):
            tempPuzzle = Puzzle.temp_move(moves[i], self.currentPuzzle)
            h1_scores.append(self.get_h1(tempPuzzle))
            i = i + 1

        return h1_scores

    def get_h1(self, puzzle):
        """
        calculates heuristic h1
        :return: int a, which is the number of incorrectly placed elements
        """
        i = 0
        a = 0
        while i < len(puzzle)-1:  # len()-1 since 0 should be at the last position
            if puzzle[i] != (i+1):
                a = a + 1
            i = i + 1
        return a

    def search_h2(self):  # TODO: Create a heuristic h2
        return False
