# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). 
# An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
# Return the number of islands in grid2 that are considered sub-islands.

# Example 1:
# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

# Constraints:
# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] and grid2[i][j] are either 0 or 1.

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(row , col) :
            if row < 0 or row >= len(grid2) or col < 0 or col >= len(grid2[0]) or grid2[row][col] ==0 :
                return  
            grid2[row][col] = 0
            dfs(row+1 , col)
            dfs(row-1 , col)
            dfs(row , col+1)
            dfs(row , col-1)
        for r in range(len(grid2)) :
            for c in range(len(grid2[0])) :
                if grid2[r][c] == 1 and grid1[r][c] == 0 :
                    dfs(r,c) #remove grid2 that does not intersect with grid1
        sub_islands = 0
        for r in range(len(grid2)) :
            for c in range(len(grid2[0])) :
                if grid2[r][c] == 1 :
                    dfs(r , c) #remove grid2 islands
                    sub_islands += 1 
        return sub_islands
      
