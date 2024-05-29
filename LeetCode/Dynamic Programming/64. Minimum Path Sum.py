# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

# Example 1:
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)) :
            for col in range(len(grid[0])) :
                if row == 0 and col != 0 :
                    grid[row][col] += grid[row][col-1]
                elif col == 0 and row != 0 :
                    grid[row][col] += grid[row-1][col]
                elif row != 0 and col != 0 :
                    grid[row][col] += min(grid[row-1][col] , grid[row][col-1])
        return grid[row][col]
'''
1 3 1    1 4 5
1 5 1 -> 2 7 6 
4 2 1    6 8 7
'''
