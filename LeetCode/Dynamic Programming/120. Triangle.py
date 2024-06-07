# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally,
# if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

# Example 1:
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

# Example 2:
# Input: triangle = [[-10]]
# Output: -10
 
# Constraints:   triangle[0].length == 1    triangle[i].length == triangle[i - 1].length + 1

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(triangle)+1)] for _ in range(len(triangle)+1)]
        for row in range(len(triangle)-1 ,-1 ,-1) :
            for col in range(row +1) :
                dp[row][col] = min(dp[row +1][col] , dp[row +1][col +1]) + triangle[row][col]
        return dp[0][0]
'''
2
3 4
6 5 7
4 1 8 3     

11 0  0  0  0
9  10 0  0  0
7  6  10 0  0
4  1  8  3  0
0  0  0  0  0
'''
