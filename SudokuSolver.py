class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def solve_sudoku(self):
        if self.solve():
            self.print_board()
        else:
            print("No solution found for the Sudoku puzzle.")

    def solve(self):
        row, col = self.find_empty_cell()

        if row == -1:
            return True

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    def find_empty_cell(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return -1, -1

    def is_valid(self, row, col, num):
        return (
            self.is_row_valid(row, num)
            and self.is_column_valid(col, num)
            and self.is_box_valid(row - row % 3, col - col % 3, num)
        )

    def is_row_valid(self, row, num):
        for col in range(9):
            if self.board[row][col] == num:
                return False
        return True

    def is_column_valid(self, col, num):
        for row in range(9):
            if self.board[row][col] == num:
                return False
        return True

    def is_box_valid(self, start_row, start_col, num):
        for row in range(3):
            for col in range(3):
                if self.board[row + start_row][col + start_col] == num:
                    return False
        return True

    def print_board(self):
        for row in range(9):
            for col in range(9):
                print(self.board[row][col], end=" ")
            print()

def main():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    solver = SudokuSolver(board)
    solver.solve_sudoku()

if __name__ == "__main__":
    main()
