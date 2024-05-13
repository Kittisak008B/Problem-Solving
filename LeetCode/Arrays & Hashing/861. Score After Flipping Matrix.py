# You are given an m x n binary matrix grid. A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
# Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
# Return the highest possible score after making any number of moves (including zero moves).

# Example 1:
# Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

# Example 2:
# Input: grid = [[0]]
# Output: 1

# Constraints:  m == grid.length   n == grid[i].length    1 <= m, n <= 20     grid[i][j] is either 0 or 1.
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        for row in range(rows) :
            if grid[row][0] == 0 :
                for col in range(cols) :
                    if grid[row][col] == 0 :
                        grid[row][col] = 1
                    else :
                        grid[row][col] = 0
        for col in range(cols) :
            num_1_incol = 0
            for row in range(rows) :
                if grid[row][col] == 1 :
                    num_1_incol += 1
            if num_1_incol < rows/2 :
                for row in range(rows) :
                    if grid[row][col] == 0 :
                        grid[row][col] = 1
                    else :
                        grid[row][col] = 0
        ans = 0
        for row in range(rows) :
            for col in range(cols) :
                if grid[row][col] == 1 :
                    ans += 2**(cols - col - 1)
        return ans
