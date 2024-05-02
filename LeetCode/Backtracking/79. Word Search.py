# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row , col , idx):
            if idx == len(word):
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[idx]:
                return False
            temp = board[row][col]
            board[row][col] = 'selected'
            if backtrack(row+1, col, idx+1) or backtrack(row-1, col, idx+1) or backtrack(row, col+1, idx+1) or backtrack(row, col-1, idx+1):
                return True
            board[row][col] = temp
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row , col , 0):
                    return True
        return False
