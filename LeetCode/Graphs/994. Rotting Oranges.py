# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Constraints:  grid[i][j] is 0, 1, or 2.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        rows , cols = len(grid) , len(grid[0])
        ans = 0
        for row in range(rows) :
            for col in range(cols) :
                if grid[row][col] == 2 :
                    queue.append((row,col))
        while queue :
            for _ in range(len(queue)) :
                cur_x , cur_y = queue.popleft()
                for d in directions :
                    next_x , next_y = cur_x + d[0] , cur_y + d[1]
                    if next_x >=0 and next_x < rows and next_y >=0 and next_y < cols and grid[next_x][next_y] == 1:
                        queue.append((next_x , next_y))
                        grid[next_x][next_y] = 2
            if queue :
                ans += 1
        for row in range(rows) :
            for col in range(cols) :
                if grid[row][col] == 1 :
                    return -1
        return ans
