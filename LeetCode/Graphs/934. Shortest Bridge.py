You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
# You may change 0's to 1's to connect the two islands to form one island. Return the smallest number of 0's you must flip to connect the two islands.

# Example 1:
# Input: grid = [[0,1],[1,0]]
# Output: 1

# Example 2:
# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2

# Example 3:
# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1

# Constraints:   n == grid.length == grid[i].length    2 <= n <= 100    grid[i][j] is either 0 or 1.    There are exactly two islands in grid.
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        directions = [(1,0) , (-1,0) , (0,1) , (0,-1)]
        visited_island = set()
      
        def get_island(row , col) :
            if row < 0 or row == rows or col < 0 or col == cols or (row , col) in visited_island or grid[row][col] != 1 :
                return 
            visited_island.add((row , col))
            for d in directions :
                get_island(row + d[0] , col + d[1])   
              
        def shortest_bridge() :
            queue = collections.deque()
            distances = {}
            for r , c in visited_island :
                distances[(r , c)] = 0
                queue.append((r , c))
            while queue :
                r , c = queue.popleft()
                for d in directions :
                    x , y = r + d[0] , c + d[1]
                    if 0 <= x < rows and 0 <= y < cols :
                        if grid[x][y] == 1 and (x , y) not in distances :
                            return distances[(r , c)]
                        if grid[x][y] == 0 and (x , y) not in distances :
                            distances[(x , y)] = distances[(r , c)] + 1
                            queue.append((x , y))
            return -1

        for row in range(rows) :
            for col in range(cols) :
                if grid[row][col] == 1 :
                    get_island(row , col)
                    return shortest_bridge()
                  
