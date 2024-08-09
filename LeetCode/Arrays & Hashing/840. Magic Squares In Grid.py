# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
# Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?
# Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

# Example 1:
# Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# Output: 1
# Explanation: 
# The following subgrid is a 3 x 3 magic square:
# 4 3 8
# 9 5 1
# 2 7 6
# while this one is not:
# 3 8 4
# 5 1 9
# 7 6 2
# In total, there is only one magic square inside the given grid.
  
# Example 2:
# Input: grid = [[8]]
# Output: 0
 
# Constraints:  row == grid.length     col == grid[i].length     1 <= row, col <= 10     0 <= grid[i][j] <= 15

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def ismagic(row , col) :
            value = set()
            for i in range(row , row + 3) :
                for j in range(col , col + 3) :
                    if grid[i][j] in value or not(1 <= grid[i][j] <= 9) :
                        return 0
                    value.add(grid[i][j])
            for i in range(row , row + 3) :
                if (grid[i][col] + grid[i][col+1] + grid[i][col+2]) != 15 :
                    return 0
            for j in range(col , col + 3) :
                if (grid[row][j] + grid[row+1][j] + grid[row+2][j]) != 15 :
                    return 0
            if ((grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2] != 15) or 
            (grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col] != 15) ):
                return 0
            return 1
        res = 0
        for row in range(len(grid) -2) :
            for col in range(len(grid[0]) -2) :
                if ismagic(row , col):
                    res += 1
        return res
      
