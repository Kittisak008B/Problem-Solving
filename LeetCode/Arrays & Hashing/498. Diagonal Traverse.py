# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

# Example 1:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]

# Example 2:
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows , cols = len(mat) , len(mat[0])
        ans = []
        traverse_up = True
        row , col = 0 , 0
        while len(ans) < rows*cols :
            if traverse_up :
                while 0 <= row < rows and 0 <= col < cols :
                    ans.append(mat[row][col])
                    row -= 1
                    col += 1
                if col == cols :
                    row += 2
                    col -= 1
                    traverse_up = False
                else :
                    row += 1
                    traverse_up = False
            elif not traverse_up :
                while 0 <= row < rows and 0 <= col < cols :
                    ans.append(mat[row][col])
                    row += 1
                    col -= 1
                if row == rows :
                    col += 2
                    row -= 1
                    traverse_up = True
                else :
                    col += 1
                    traverse_up = True
        return ans
      
