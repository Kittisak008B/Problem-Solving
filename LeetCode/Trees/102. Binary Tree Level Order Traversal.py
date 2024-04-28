# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:
#     3
#    / \
#   9  20
#      / \
#     15  7
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        ans = []
        queue = [root]
        next_q = []
        while queue :
            level = []
            for node in queue :
                level.append(node.val)
                if node.left :
                    next_q.append(node.left)
                if node.right :
                    next_q.append(node.right)
            ans.append(level)
            queue = next_q
            next_q = []
            level = []
        return ans
      
