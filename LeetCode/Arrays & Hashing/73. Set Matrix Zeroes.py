# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix) 
        cols = len(matrix[0])
        def mark_func(row , col , direction) :
            if 0 <= row < rows and 0 <= col < cols and matrix[row][col] != 0 :
                matrix[row][col] = '$$$'
                if direction == 'left' :
                    mark_func(row , col+1 ,'left')
                elif direction == 'right' :
                    mark_func(row , col-1 ,'right')
                elif direction == 'up' :
                    mark_func(row+1 , col ,'up')
                elif direction == 'down' :
                    mark_func(row-1 , col ,'down')
        for row in range(rows) :
            for col in range(cols) :
                if matrix[row][col] == 0 :
                    mark_func(row , col+1 ,'left')
                    mark_func(row , col-1 ,'right')
                    mark_func(row+1 , col ,'up')
                    mark_func(row-1 , col ,'down')
        for row in range(rows) :
            for col in range(cols) :
                if matrix[row][col] == '$$$' :
                    matrix[row][col] = 0
