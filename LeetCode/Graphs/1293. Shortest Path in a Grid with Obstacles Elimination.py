# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.
# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

# Example 1:
# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

# Example 2:
# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# Explanation: We need to eliminate at least two obstacles to find such a walk.
 
# Constraints:   m == grid.length   n == grid[i].length   1 <= m, n <= 40   1 <= k <= m * n   grid[i][j] is either 0 or 1.   grid[0][0] == grid[m - 1][n - 1] == 0

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows , cols = len(grid) , len(grid[0])
        if rows == 1 and cols == 1:
            return 0
        if k >= rows + cols - 2:
            return rows + cols - 2
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = collections.deque()
        visited = set()
        queue.append((0 ,0 ,k ,0))
        visited.add((0 ,0 ,k))
        while queue :
            r , c , break_wall ,path = queue.popleft()
            if (r , c) == (rows-1 , cols-1) :
                return path
            for d in directions :
                x , y = r + d[0] , c + d[1]
                if 0 <= x < rows and 0 <= y < cols :
                    if grid[x][y] == 1 and break_wall > 0 and (x,y,break_wall-1) not in visited :
                        visited.add((x ,y ,break_wall-1))
                        queue.append((x ,y ,break_wall-1 ,path+1))
                    elif grid[x][y] == 0 and (x,y,break_wall) not in visited :
                        visited.add((x ,y ,break_wall))
                        queue.append((x ,y ,break_wall ,path+1))
        return -1
      
