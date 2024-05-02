# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Example 2:
# Input: n = 1
# Output: [["Q"]]
 
# Constraints:
# 1 <= n <= 9

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board =[['.']*n for _ in range(n)]
        ans = []
        def is_safe(row , col) :
            for i in range(col) : #check _
                if board[row][i] == 'Q' :
                    return False
            for i in range(row) : #check |
                if board[i][col] == 'Q' :
                    return False
            i,j = row,col
            while i>=0 and j>=0 : #check \
                if board[i][j] == 'Q' :
                    return False
                i -= 1
                j -= 1
            i,j = row,col
            while j<n : #check /
                if board[i][j] == 'Q' :
                    return False
                i -= 1
                j += 1
            return True

        def backtrack(row) :
            if row == n :
                ans.append([''.join(x) for x in board])
                return
            for col in range(n) :
                if is_safe(row , col) :
                    board[row][col] = 'Q'
                    backtrack(row+1)
                    board[row][col] = '.'
        backtrack(0)
        return ans
      
