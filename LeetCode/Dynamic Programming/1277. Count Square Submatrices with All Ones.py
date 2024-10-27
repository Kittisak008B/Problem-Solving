# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
  
# Example 1:
# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation: There are 10 squares of side 1.  There are 4 squares of side 2.  There is 1 square of side 3.  Total number of squares = 10 + 4 + 1 = 15.

# Example 2:
# Input: matrix = 
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation: There are 6 squares of side 1.  There is 1 square of side 2.  Total number of squares = 6 + 1 = 7.
 
# Constraints:
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = {}
        def dfs(i , j) :
            if i >= len(matrix) or j >= len(matrix[0]) :
                return 0
            if (i , j) in dp :
                return dp[(i , j)]
            if matrix[i][j] == 1 :
                if i != 0 and j != 0 :
                    left = dfs(i-1 , j)
                    above = dfs(i , j-1)
                    diagonal = dfs(i-1 , j-1)
                    dp[(i ,j)] = min(left , above , diagonal) + 1
                else :
                    dp[(i ,j)] = 1
            else :
                dp[(i ,j)] = 0
            return dp[(i ,j)]
        res = 0
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                res += dfs(i , j)
        return res
'''
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

0 1 1 1
1 1 2 2
0 1 2 3  sum = 15
'''
