from random import sample

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
