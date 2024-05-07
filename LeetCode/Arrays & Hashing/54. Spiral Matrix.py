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
# sol2
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         max_row , max_col = len(matrix) , len(matrix[0])
#         row , col = 0 , 0
#         cur_direction = (0,1)
#         direction_map = {(0,1):(1,0) , (1,0):(0,-1) , (0,-1):(-1,0) , (-1,0):(0,1)} #right->down->left->up->right
#         ans = [matrix[0][0]]
#         matrix[0][0] = 'selected'

#         while len(ans) < max_row*max_col :
#             next_row = row + cur_direction[0] 
#             next_col = col + cur_direction[1]
#             if next_row == max_row or next_col == max_col or next_row < 0 or next_col < 0 or matrix[next_row][next_col] == 'selected':
#                 cur_direction = direction_map[cur_direction]
#             else :
#                 row , col = next_row , next_col
#                 ans.append(matrix[row][col])
#                 matrix[row][col] = 'selected'
#         return ans
