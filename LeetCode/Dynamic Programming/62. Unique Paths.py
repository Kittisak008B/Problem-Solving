# There is a robot on an m x n grid. The robot is initially located at the top-left corner
# (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Example 1:
# Input: m = 3, n = 7
# Output: 28

# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths =[[0]*n for _ in range(m)]
        for col in range(n) :
            paths[m-1][col] = 1
        for row in range(m) :
            paths[row][n-1] = 1
        for row in range(m-2 ,-1 ,-1) :
            for col in range(n-2 ,-1 ,-1) :
                paths[row][col] = paths[row][col+1] + paths[row+1][col]
        return paths[0][0]
'''
can move right or down

s=7+21=28
s  21 15 10 6  3  1    
7  6  5  4  3  2  1    
1  1  1  1  1  1  end
'''
