# You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] 
# and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.
# A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. 
# A cell is guarded if there is at least one guard that can see it. Return the number of unoccupied cells that are not guarded.

# Example 1:
#   0 1 2 3 4 5
# 0 g w   *          * is guarded cell
# 1 * g * * w
# 2 * * w g * *
# 3 * *   * 
# Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
# Output: 7
# Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram. There are a total of 7 unguarded cells, so we return 7.

# Constraints:
# 1 <= m, n <= 10**5
# 2 <= m * n <= 10**5
# 1 <= guards.length, walls.length <= 5 * 10**4
# 2 <= guards.length + walls.length <= m * n
# guards[i].length == walls[j].length == 2
# 0 <= rowi, rowj < m
# 0 <= coli, colj < n
# All the positions in guards and walls are unique.

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def make_guard(row , col) :
            for r in range(row+1 , m) :
                if g[r][col] == 1 or g[r][col] == 2 :
                    break
                g[r][col] = 3
            for r in range(row-1 , -1 , -1) :
                if g[r][col] == 1 or g[r][col] == 2 :
                    break
                g[r][col] = 3
            for c in range(col+1 , n) :
                if g[row][c] == 1 or g[row][c] == 2 :
                    break
                g[row][c] = 3
            for c in range(col-1 , -1 , -1) :
                if g[row][c] == 1 or g[row][c] == 2 :
                    break
                g[row][c] = 3

        g = [[0]*n for _ in range(m)]
        for row , col in guards :
            g[row][col] = 1
        for row , col in walls :
            g[row][col] = 2
        for row , col in guards :
            make_guard(row , col)
        count = 0
        for row in range(len(g)) :
            for col in range(len(g[0])) :
                if g[row][col] == 0 :
                    count += 1
        return count
