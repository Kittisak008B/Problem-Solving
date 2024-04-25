# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
  
# Example 1:
#      1
#    /   \
#   2     3
#  / \
# 4   5
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2:
# Input: root = [1,2]
# Output: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def check_height(root) :
            if not root :
                return 0
            left_height = check_height(root.left) 
            right_height = check_height(root.right)

            diameter = left_height + right_height
            ans[0] = max(ans[0] , diameter)
            return 1 + max(left_height , right_height)

        check_height(root)
        return ans[0]
      
