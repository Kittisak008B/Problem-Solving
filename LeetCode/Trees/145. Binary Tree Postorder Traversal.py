# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:
# 1
#  \
#   2
#  /
# 3
# Input: root = [1,null,2,3]
# Output: [3,2,1]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []
        stack = [root]
        result = []
        while stack :
            node = stack.pop()
            result.append(node.val)
            if node.left :
                stack.append(node.left)
            if node.right :
                stack.append(node.right)
        return result[::-1]
      
