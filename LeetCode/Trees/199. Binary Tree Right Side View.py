# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:
#     1
#    / \ 
#   2   3
#    \   \
#     5   4
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:
# Input: root = [1,null,3]
# Output: [1,3]

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = [root]
        next_q = []
        while queue and root :
            for node in queue :
                if node.left :
                    next_q.append(node.left)
                if node.right :
                    next_q.append(node.right)
            ans.append(node.val)
            queue = next_q
            next_q = []
        return ans 
      
