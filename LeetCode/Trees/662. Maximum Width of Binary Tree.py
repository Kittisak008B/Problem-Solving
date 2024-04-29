# Given the root of a binary tree, return the maximum width of the given tree.
# The maximum width of a tree is the maximum width among all levels.
# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), 
# where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.
# It is guaranteed that the answer will in the range of a 32-bit signed integer.

# Example 1:
#       1
#      / \ 
#     3   2
#    / \   \
#   5   3   9
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

# Example 2:
#       1
#      / \
#     3   2
#    /      \
#   5        9
#  /        /
# 6        7
# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7
# Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

# Example 3:
#      1
#     / \
#    3   2
#   /
#  5
# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width exists in the second level with length 2 (3,2).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        max_width = 1
        level = [(root , 1)]
        while level != [] :
            next_level = []
            for node , pos in level :
                if node.left :
                    next_level.append((node.left , pos*2))
                if node.right :
                    next_level.append((node.right , pos*2 + 1))
            if next_level :
                max_width = max(max_width , next_level[-1][1] - next_level[0][1] + 1)
            level = next_level
            next_level = []
        return max_width
      
