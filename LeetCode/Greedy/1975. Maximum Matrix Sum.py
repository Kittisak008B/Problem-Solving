# You are given an n x n integer matrix. You can do the following operation any number of times:
# Choose any two adjacent elements of matrix and multiply each of them by -1. Two elements are considered adjacent if and only if they share a border.
# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

# Example 1:
# Input: matrix = [[1,-1],[-1,1]]
# Output: 4
# Explanation: We can follow the following steps to reach sum equals 4:
# - Multiply the 2 elements in the first row by -1.
# - Multiply the 2 elements in the first column by -1.

# Example 2:
# Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
# Output: 16
# Explanation: We can follow the following step to reach sum equals 16:
# - Multiply the 2 last elements in the second row by -1.
 
# Constraints:
# n == matrix.length == matrix[i].length
# 2 <= n <= 250
# -10**5 <= matrix[i][j] <= 10**5

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_abs_value = float('inf')
        neg_count = 0
        for row in matrix :
            for val in row :
                if val < 0 :
                    neg_count += 1
                total_sum += abs(val)
                min_abs_value = min(min_abs_value , abs(val))
        if neg_count % 2 == 1 :
            total_sum -= min_abs_value * 2
        return total_sum
      
