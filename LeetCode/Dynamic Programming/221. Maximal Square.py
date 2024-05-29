# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example 1:
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4

# Example 2:
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1

# Example 3:
# Input: matrix = [["0"]]
# Output: 0
 
# Constraints:  matrix[i][j] is '0' or '1'.
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_square = 0
        for row in range(len(matrix)) :
            for col in range(len(matrix[0])) :
                if row == 0 or col == 0 :
                    max_square = max(max_square , int(matrix[row][col]))
                elif matrix[row][col] == '1' :
                    matrix[row][col] = min(int(matrix[row-1][col]),int(matrix[row-1][col-1]),int(matrix[row][col-1])) +1
                    max_square = max(max_square , matrix[row][col])
        return max_square**2
'''
1 1 0   1 1 0 max_square=2 ->return 4
1 1 1 ->1 2 1
1 0 1   1 0 1
'''
