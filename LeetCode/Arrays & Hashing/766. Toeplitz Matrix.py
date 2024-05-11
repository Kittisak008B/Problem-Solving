# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false. A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

# Example 1:
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]  Output: true
# Explanation:
# In the above grid, the diagonals are: "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]". In each diagonal all elements are the same, so the answer is True.

# Example 2:
# Input: matrix = [[1,2],[2,2]]  Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        rows , cols = len(matrix) , len(matrix[0])
        def not_same_diag(row , col) :
            val = matrix[row][col]
            while 0 <= row < rows and 0 <= col < cols :
                if matrix[row][col] != val :
                    return True
                row += 1
                col += 1
            return False
          
        for col in range(cols) :
            if not_same_diag(0 , col) :
                return False
        for row in range(1 , rows) :
            if not_same_diag(row , 0) :
                return False
        return True
      
