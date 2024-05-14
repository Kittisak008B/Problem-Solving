# In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
# Return the maximum amount of gold you can collect under the conditions:
# Every time you are located in a cell you will collect all the gold in that cell.
# From your position, you can walk one step to the left, right, up, or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has some gold.

# Example 1:
# Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
# Output: 24
# Explanation:
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])

        def dfs(row ,col ,visited) :
            if row < 0 or row == rows or col < 0 or col == cols or grid[row][col] == 0 or (row,col) in visited :
                return 0
            visited.add((row ,col))
            gold = grid[row][col]
            for d in [(1,0),(-1,0),(0,1),(0,-1)] :
                x , y = row + d[0] , col + d[1]
                gold = max(gold , grid[row][col] + dfs(x ,y ,visited))
            visited.remove((row ,col))
            return gold

        ans = 0
        for row in range(rows) :
            for col in range(cols) :
                if grid[row][col] > 0 :
                    ans = max(ans ,dfs(row , col , set()))
        return ans

# class Solution:
#     def getMaximumGold(self, grid: List[List[int]]) -> int:
#         rows , cols = len(grid) , len(grid[0])

#         def dfs(row ,col) :
#             if row < 0 or row == rows or col < 0 or col == cols or grid[row][col] == 0 :
#                 return 0
#             temp = grid[row][col]
#             grid[row][col] = 0
#             gold = 0
#             for d in [(1,0),(-1,0),(0,1),(0,-1)] :
#                 x , y = row + d[0] , col + d[1]
#                 gold = max(gold , temp + dfs(x ,y))

#             grid[row][col] = temp
#             return gold

#         ans = 0
#         for row in range(rows) :
#             for col in range(cols) :
#                if grid[row][col] > 0 :
#                     ans = max(ans ,dfs(row , col))
#         return ans
