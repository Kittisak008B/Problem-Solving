# Given an m x n integers matrix, return the length of the longest increasing path in matrix.
# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

# Example 1:
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].

# Example 2:
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

# Example 3:
# Input: matrix = [[1]]
# Output: 1

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows , cols = len(matrix) , len(matrix[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        path = {}
        ans = 1
        def dfs(row , col) :
            if (row , col) in path :
                return path[(row , col)]
            path[(row , col)] = 1
            for d in directions :
                next_row , next_col = row +d[0] , col +d[1]
                if 0 <= next_row < rows and 0 <= next_col < cols and matrix[next_row][next_col] > matrix[row][col] :
                    path[(row ,col)] = max(path[(row ,col)] , 1 + dfs(next_row , next_col))
            return path[(row , col)]

        for row in range(rows) :
            for col in range(cols) :
                ans = max(ans , dfs(row , col))
        return ans
      
