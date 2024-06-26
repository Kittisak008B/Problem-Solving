# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. 
# It will automatically contact the police if two directly-linked houses were broken into on the same night.
# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

# Example 1:
#    3
#   / \
#  2    3
#   \     \
#    3     1
# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

# Example 2:
#      3
#     / \
#    4   5
#   / \    \ 
#  1   3     1
# Input: root = [3,4,5,1,3,null,1]
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root) :
            if not root :
                return (0 , 0)
            leftnode = dfs(root.left)
            rightnode = dfs(root.right)

            rob_node = root.val + leftnode[1] + rightnode[1]
            rob_without_node = max(leftnode) + max(rightnode)
            return (rob_node , rob_without_node)
        return max(dfs(root))
'''
(rob this node , rob without this node)

          3 (3+4+1 , 5+4) -> 9 
         / \
  (4,4) 4   5 (5,1)
       / \   \
      1   3   1
  (1,0)  (3,0) (1,0)
'''
