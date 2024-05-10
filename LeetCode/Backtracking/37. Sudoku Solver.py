# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

# Example 1:
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'
# It is guaranteed that the input board has only one solution.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
      
        def is_valid(row , col , str_num) :
            for j in range(9) :
                if board[row][j] == str_num :
                    return False
                if board[j][col] == str_num :
                    return False
                if board[3*(row//3) + j//3][3*(col//3) + j%3]  == str_num :
                    return False
            return True

        def solve_sdk(row , col) :
            if row == len(board) :
                return True
            elif col == len(board[0]) :
                return solve_sdk(row+1 , 0)
            elif board[row][col] != '.' :
                return solve_sdk(row , col+1)
            else :
                for i in range(1 , 10) :
                    if is_valid(row , col , str(i)) :
                        board[row][col] = str(i)
                        if solve_sdk(row , col+1) :
                            return solve_sdk(row , col+1)
                        board[row][col] = '.'
            return False          
        solve_sdk(0,0)