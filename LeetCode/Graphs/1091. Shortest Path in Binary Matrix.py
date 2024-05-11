# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
# All the visited cells of the path are 0. All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

# Example 1:
# Input: grid = [[0,1],[1,0]]
# Output: 2

# Example 2:
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

# Constraints: n == grid.length    n == grid[i].length    1 <= n <= 100    grid[i][j] is 0 or 1

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1 :
            return -1
        rows , cols = len(grid) , len(grid[0])
        queue = collections.deque()
        queue.append((0 , 0 , 1))
        visited = set()
        visited.add((0 , 0))

        while queue :
            row , col , path = queue.popleft()
            if (row , col) == (rows-1 , cols-1) :
                return path
            for d in [(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)] :
                next_row , next_col = row+d[0] , col+d[1]
                if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 0 and (next_row,next_col) not in visited :
                    visited.add((next_row , next_col))
                    queue.append((next_row , next_col , path + 1))
        return -1 
