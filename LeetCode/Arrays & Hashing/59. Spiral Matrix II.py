# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

# Example 1:
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

# Example 2:
# Input: n = 1
# Output: [[1]]

# Constraints: 1 <= n <= 20

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1 :
            return [[1]]
        matrix = [[0]*n for _ in range(n)]
        min_row , max_row = 0 , len(matrix)
        min_col , max_col = 0 , len(matrix[0])
        x = 1
        row = 0
        while min_row < max_row and min_col < max_col :
            for col in range(min_col , max_col) :
                matrix[row][col] = x
                x += 1
            min_row += 1
            for row in range(min_row , max_row) :
                matrix[row][col] = x
                x += 1
            max_col -= 1
            if  min_row < max_row and min_col < max_col :
                for col in  range(max_col-1 , min_col-1 , -1) :
                    matrix[row][col] = x
                    x += 1
                max_row -= 1
                for row in range(max_row-1 , min_row-1 , -1) :
                    matrix[row][col] = x
                    x += 1
                min_col += 1
        return matrix
      
