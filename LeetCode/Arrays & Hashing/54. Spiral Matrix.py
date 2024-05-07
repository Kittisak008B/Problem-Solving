# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],
#                  [4,5,6],
#                  [7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        min_row , min_col = 0 , 0
        max_row , max_col = len(matrix) , len(matrix[0])
        ans = []
        row = 0
        while min_row < max_row and min_col < max_col :
            for col in range(min_col , max_col) : #right
                ans.append(matrix[row][col])
            min_row += 1
            for row in range(min_row , max_row) : #down
                ans.append(matrix[row][col])
            max_col -= 1
            if min_row < max_row and min_col < max_col :
                for col in range(max_col-1 , min_col-1 , -1) : #left
                    ans.append(matrix[row][col])
                max_row -= 1
                for row in range(max_row-1 , min_row-1 , -1) : #up
                    ans.append(matrix[row][col])
                min_col += 1
        return ans
      
