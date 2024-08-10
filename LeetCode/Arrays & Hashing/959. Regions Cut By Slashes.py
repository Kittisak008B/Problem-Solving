# An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. 
# These characters divide the square into contiguous regions.
# Given the grid grid represented as a string array, return the number of regions. Note that backslash characters are escaped, so a '\' is represented as '\\'.

# Example 1:
# Input: grid = [" /","/ "]
# Output: 2

# Example 2:
# Input: grid = [" /","  "]
# Output: 1

# Example 3:
# Input: grid = ["/\\","\\/"]
# Output: 5
# Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
 
# Constraints:
# n == grid.length == grid[i].length
# 1 <= n <= 30
# grid[i][j] is either '/', '\', or ' '.

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        m , n = len(grid) , len(grid[0])
        nr , nc = 3*m , 3*n
        grid2 = [[0 for _ in range(nc)] for _ in range(nr)]   #DFS on upscaled grid
        for r in range(m):
            for c in range(n):
                r2 , c2 = r*3 , c*3
                if grid[r][c] == '/' :
                    grid2[r2][c2+2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2] = 1
                elif grid[r][c] == '\\' :
                    grid2[r2][c2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2+2] = 1
        def dfs(r , c):
            if r < 0 or r == nr or c < 0 or c == nc or grid2[r][c] :
                return 
            grid2[r][c] = 1
            dfs(r+1 , c)
            dfs(r-1 , c)
            dfs(r , c+1)
            dfs(r , c-1)
        ans = 0
        for i in range(nr):
            for j in range(nc):
                if grid2[i][j] == 0 :
                    dfs(i , j)
                    ans += 1
        return ans
