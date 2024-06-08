# Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.
# A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

# Example 1:
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 13
# Explanation: 
# The possible falling paths are:
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# The falling path with the smallest sum is [1,5,7], so the answer is 13.

# Example 2:
# Input: grid = [[7]]
# Output: 7

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        prev_dp = grid[-1]
        for row in range(len(grid)-2 ,-1 ,-1) :
            dp = [float('inf') for _ in range(len(grid[0]))]
            for cur_col in range(len(grid[0])) :
                for prev_col in range(len(grid[0])) :
                    if cur_col != prev_col :
                        dp[cur_col] = min(dp[cur_col] , grid[row][cur_col] + prev_dp[prev_col])
            prev_dp = dp
        return min(prev_dp)
'''
1 2 3      13 14 15
4 5 6  ->  12 12 13
7 8 9      7  8  9

_  _  _         -->   inf inf inf  dp     -->  13 14 15 prev_dp
infinfinf  dp         12  12  13   prev_dp    
7  8  9    prev_dp   
'''
