# You are given an m x n integer matrix matrix with the following two properties:
# -Each row is sorted in non-decreasing order.
# -The first integer of each row is greater than the last integer of the previous row.
  
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = m*n - 1
        while i <= j :
            middle = (i+j) // 2
            row = middle // n
            column = middle % n
            if matrix[row][column] < target :
                i = middle + 1
            elif matrix[row][column] > target :
                j = middle - 1
            else :
                return True
        return False
