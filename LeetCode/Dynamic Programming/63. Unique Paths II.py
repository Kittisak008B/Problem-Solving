# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 109.

# Example 1:
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

# Example 2:
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
 
# Constraints:  obstacleGrid[i][j] is 0 or 1.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [0]*cols
        dp[cols-1] = 1

        for row in range(rows-1 ,-1 ,-1) :
            for col in range(cols-1 ,-1 ,-1) :
                if obstacleGrid[row][col] == 1 :
                    dp[col] = 0
                elif col + 1 < cols :
                    dp[col] += dp[col + 1]
        return dp[0]
'''
s=1+1=2
s 1 1
1 x 1
1 1 e

dp =[0,0,1]
row,col = 2,2 dp=[0,0,1]
          2,1 dp=[0,1,1]
          2,0 dp=[1,1,1]
          1,2 dp=[1,1,1]
          1,1 dp=[1,0,1]
          1,0 dp=[1,0,1]
          0,2 dp=[1,0,1]
          0,1 dp=[1,1,1]
          0,0 dp=[2,1,1]
'''
