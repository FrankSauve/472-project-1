

class Spot:

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.g = 0
        self.h = 0
        self.f = 0
        self.previous = None

    @staticmethod
    def get_spots(moves):
        s = []
        for move in moves:
            s.append(Spot(move))

        return s
