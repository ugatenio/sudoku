import sys
from random import sample, random
from math import sqrt

class Sudoku:
    def __init__(self, size):
        self.size = size
        self.sqrt = int(sqrt(size))
        self.board = self._create_empty(size, symbol=0)
        self.raw_map = self._create_empty(size, symbol=False)
        self.col_map = self._create_empty(size, symbol=False)
        self.sqr_map = self._create_empty(size, symbol=False)

    def _create_empty(self, size, symbol):
        return [[symbol for _ in range(size)] for _ in range(size)]

    def _update_maps(self, number, location, state=True):
        self.raw_map[location[0]][number - 1] = state
        self.col_map[location[1]][number - 1] = state
        self.sqr_map[(location[0] - location[0] % self.sqrt) + ((location[1] - location[1] % self.sqrt) // self.sqrt)][number - 1] = state

    def set_number(self, number, location=(0,0)):
        self.board[location[0]][location[1]] = number
        self._update_maps(number, location, state=True)

    def get_number(self, location=(0,0)):
        return self.board[location[0]][location[1]]

    def clear(self, location=(0, 0)):
        self._update_maps(number=self.board[location[0]][location[1]], location=location, state=False)
        self.board[location[0]][location[1]] = 0

    def valid(self, number, location):
        return not self.raw_map[location[0]][number - 1] and \
               not self.col_map[location[1]][number - 1] and \
               not self.sqr_map[(location[0] - location[0] % self.sqrt) + ((location[1] - location[1] % self.sqrt) // self.sqrt)][number - 1]

    def empty(self, location):
        return self.board[location[0]][location[1]] == 0

    def __str__(self):
        return '\n'.join([str(raw) for raw in self.board])

class SudokuSolver:
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def solve(self):
        for i in range(self.sudoku.size):
            for j in range(self.sudoku.size):
                if not self.sudoku.empty(location=(i, j)):
                    continue
                for option in sample(list(range(1, self.sudoku.size + 1)), self.sudoku.size):
                    if not self.sudoku.valid(option, location=(i, j)):
                        continue
                    self.sudoku.set_number(option, location=(i,j))
                    if self.solve():
                        return True
                    self.sudoku.clear(location=(i,j))
                return False
        return True

class SudokuGenerator:
    def __init__(self, size):
        self.sudoku = Sudoku(size)
        self.threshold = 0.4

    def _solve(self):
        SudokuSolver(self.sudoku).solve()

    def _punch(self):
        for i in range(self.sudoku.size):
            for j in range(self.sudoku.size):
                if random() <= self.threshold:
                    self.sudoku.clear(location=(i,j))

    def generate(self):
        self._solve()
        self._punch()
        return self.sudoku

if __name__ == '__main__':
    size = int(sys.argv[1] or 9)
    sudoku = SudokuGenerator(size).generate()
    print(sudoku)