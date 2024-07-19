# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

# Example 1:
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

# Example 2:
# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= n, m <= 50
# 1 <= matrix[i][j] <= 10**5.
# All elements in the matrix are distinct.

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = []
        for r in range(len(matrix)) :
            r_min = float('inf')
            for c in range(len(matrix[0])):
                r_min = min(r_min , matrix[r][c])
            row_min.append(r_min)
        col_max = []
        for c in range(len(matrix[0])) :
            c_max = float('-inf')
            for r in range(len(matrix)) :
                c_max = max(c_max , matrix[r][c])
            col_max.append(c_max)
        Lucky_num = []
        for r in range(len(matrix)) :
            for c in range(len(matrix[0])) :
                if matrix[r][c] == row_min[r] and matrix[r][c] == col_max[c] :
                    Lucky_num.append(matrix[r][c])
        return Lucky_num
