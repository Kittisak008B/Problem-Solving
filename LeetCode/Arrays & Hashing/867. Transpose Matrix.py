# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]

# Example 2:
# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows , cols = len(matrix) , len(matrix[0])
        ans = [[0]*rows for _ in range(cols)]
        for row in range(rows) :
            for col in range(cols) :
                ans[col][row] = matrix[row][col]
        return ans
      
