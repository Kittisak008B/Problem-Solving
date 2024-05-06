# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path. Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Example 1:
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Example 2:
#           -10
#            / \
#           9   20
#               / \
#              15  7
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]
        def dfs(root) :
            if not root :
                return 0
            left = max(0 , dfs(root.left))
            right = max(0 , dfs(root.right))
            ans[0] = max(ans[0] , left + right + root.val)
            return max(left , right) + root.val
        dfs(root)
        return ans[0]
# ex.     5      
#        / \                              
#      10   15                              
#     / \   / \                                                   
#    2  -1  3  -4
#       / \
#      5   8    max = 40
