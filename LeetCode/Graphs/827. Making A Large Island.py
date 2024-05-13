# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
# Return the size of the largest island in grid after applying this operation. An island is a 4-directionally connected group of 1s.

# Example 1:
# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

# Example 2:
# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

# Example 3:
# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
 
# Constraints:  grid[i][j] is either 0 or 1.
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        island = {}
        island_id = -1
        def island_area(row , col) :
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1 :
                area = 1
                grid[row][col] = island_id
                for d in directions :
                    area += island_area(row + d[0] , col + d[1])
                return area
            else :
                return 0

        for row in range(rows) :
            for col in range(cols) :
                if grid[row][col] == 1 :
                    island[island_id] = island_area(row , col)
                    island_id -= 1
                  
        max_area = 0
        for row in range(rows) :
            for col in range(cols) :
                if grid[row][col] == 0 :
                    area = 1
                    neighbour_island = set()
                    for d in directions :
                        r , c = row +d[0] ,col +d[1]
                        if 0 <= r < rows and 0 <= c < cols and grid[r][c] != 0 :
                            neighbour_island.add(grid[r][c])
                    for island_id in neighbour_island :
                        area += island[island_id]
                    max_area = max(max_area , area)
        if max_area == 0 :
            return rows*cols
        else :
            return max_area
          
