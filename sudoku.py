from sudoku_generator import SudokuGenerator

if __name__ == '__main__':
    sudoku = SudokuGenerator(9).generate()
    print(sudoku)
