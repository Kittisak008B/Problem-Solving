# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"] ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"] ]
# Output: 3
 
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        def dfs(row , col) :
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != '1' :
                return 
            else :
                grid[row][col] = '0'
                dfs(row+1 , col)
                dfs(row-1 , col)
                dfs(row , col+1)
                dfs(row , col-1)
              
        for row in range(len(grid)) :
            for col in range(len(grid[0])) :
                if grid[row][col] == '1' :
                    islands += 1
                    dfs(row , col)
        return islands
