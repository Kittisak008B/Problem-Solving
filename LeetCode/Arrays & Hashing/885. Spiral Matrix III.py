# You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.
# You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.
# Return an array of coordinates representing the positions of the grid in the order you visited them.

# Example 1:
# Input: rows = 1, cols = 4, rStart = 0, cStart = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]

# Example 2:
# Input: rows = 5, cols = 6, rStart = 1, cStart = 4
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        #right->down->left->up->right
        #1,1,2,2,3,3,4,4,5,5,6,6,...   steps += 1 every2directions

        ans = [[rStart,cStart]]
        row , col = rStart , cStart
        steps = 1

        def is_valid(row , col) :
            if row >= 0 and row < rows and col >= 0 and col < cols :
                return True
            return False

        while len(ans) < rows*cols :
            for _ in range(steps) :
                row , col = row , col+1 #right
                if is_valid(row , col) :
                    ans.append([row , col])
            for _ in range(steps) :
                row , col = row+1 , col #down
                if is_valid(row , col) :
                    ans.append([row , col])
            steps += 1

            for _ in range(steps) :
                row , col = row , col-1 #left
                if is_valid(row , col) :
                    ans.append([row , col])
            for _ in range(steps) :
                row , col = row-1 , col #up
                if is_valid(row , col) :
                    ans.append([row , col])
            steps +=1
        return ans

# class Solution:
#     def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
#         directions = [(0,1),(1,0),(0,-1),(-1,0)]
#         num_steps = 1
#         result = []
#         r , c = rStart , cStart
#         d = 0
#         while len(result) < rows*cols :
#             for _ in range(2) :
#                 for _ in range(num_steps) :
#                     if 0 <= r < rows and 0 <= c < cols :
#                         result.append([r , c])
#                     if len(result) ==  rows*cols :
#                         return result
#                     r += directions[d][0]
#                     c += directions[d][1]
#                 d = (d+1)%4
#             num_steps += 1
#         return result
