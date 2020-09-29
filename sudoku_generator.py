from sudoku_board import SudokuBoard
from sudoku_solver import SudokuSolver
from random import random

class SudokuGenerator:
    def __init__(self, size):
        self.sudoku = SudokuBoard(size)
        self.threshold = 0.5

    def _solve(self):
        SudokuSolver(self.sudoku).solve()

    def _punch(self):
        for i in range(self.sudoku.size):
            for j in range(self.sudoku.size):
                if random() <= self.threshold:
                    self.sudoku.clear(location=(i,j))

    def generate(self):
        self._solve()
        # self._punch()
        return self.sudoku
