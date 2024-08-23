# You are given an m x n binary grid grid where 1 represents land and 0 represents water. 
# An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.
# The grid is said to be connected if we have exactly one island, otherwise is said disconnected.
# In one day, we are allowed to change any single land cell (1) into a water cell (0). Return the minimum number of days to disconnect the grid.

# Example 1:
# Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 2
# Explanation: We need at least 2 days to get a disconnected grid. Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
  
# Example 2:
# Input: grid = [[1,1]]
# Output: 2
# Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
 
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 30
# grid[i][j] is either 0 or 1.

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        def dfs(r , c , visited) :
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == 0) :
                return
            visited.add((r,c))
            for nei_r , nei_c in [(r+1,c) , (r-1,c) , (r,c+1) , (r,c-1)] :
                dfs(nei_r , nei_c , visited)
        def count_island() :
            visited = set()
            count = 0
            for r in range(rows) :
                for c in range(cols) :
                    if grid[r][c] == 1 and (r , c) not in visited :
                        dfs(r , c , visited)
                        count += 1
            return count 
        if count_island() != 1 :
            return 0
        for r in range(rows) :
            for c in range(cols) :
                if grid[r][c] == 1 :
                    grid[r][c] = 0 
                    if count_island() != 1 :
                        return 1 
                    grid[r][c] = 1
        return 2
      