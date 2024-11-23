# You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:
# A stone '#'     A stationary obstacle '*'     Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. 
# Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. 
# Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.
# It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.
# Return an n x m matrix representing the box after the rotation described above.

# Example 1:
# Input: box = [["#",".","#"]]
# Output: [["."],
#          ["#"],
#          ["#"]]
         
# Example 3:
# Input: box = [["#","#","*",".","*","."],
#               ["#","#","#","*",".","."],
#               ["#","#","#",".","#","."]]
# Output: [[".","#","#"],
#          [".","#","#"],
#          ["#","#","*"],
#          ["#","*","."],
#          ["#",".","*"],
#          ["#",".","."]]
 
# Constraints:
# m == box.length
# n == box[i].length
# 1 <= m, n <= 500
# box[i][j] is either '#', '*', or '.'

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        box_copy = box[:]
        rows = len(box_copy)
        cols = len(box_copy[0])
        for r in range(rows) :
            pointer = cols - 1
            for c in range(cols-1 , -1 , -1) :
                if box_copy[r][c] == '#' :
                    box_copy[r][c] , box_copy[r][pointer] = box_copy[r][pointer] , box_copy[r][c]
                    pointer -= 1
                elif box_copy[r][c] == '*' :
                    pointer = c - 1
        rotated_box = []
        for c in range(cols) :
            col = []
            for r in range(rows-1 , -1 , -1) :
                col.append(box_copy[r][c])
            rotated_box.append(col)
        return rotated_box
      
