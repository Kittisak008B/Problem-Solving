# Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.
# For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
# Return the root of the reversed tree.
# A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.
# The level of a node is the number of edges along the path between it and the root node.

# Example 1:
#            2                    2
#          /  \                 /  \
#         3    5               5     3
#        / \   / \            / \   / \ 
#      8   13 21  34         8  13 21  34
# Input: root = [2,3,5,8,13,21,34]
# Output: [2,5,3,8,13,21,34]
# Explanation: 
# The tree has only one odd level. The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.

# Example 2:
# Input: root = [7,13,11]
# Output: [7,11,13]
# Explanation:  The nodes at level 1 are 13, 11, which are reversed and become 11, 13.

# Constraints:
# The number of nodes in the tree is in the range [1, 2**14].
# 0 <= Node.val <= 10**5
# root is a perfect binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(r1 , r2 , level) :
            if not r1 or not r2 :
                return
            if level % 2 == 0 :
                r1.val , r2.val = r2.val , r1.val
            dfs(r1.left , r2.right, level + 1)
            dfs(r1.right, r2.left , level + 1)
          
        dfs(root.left , root.right , 0)
        return root
      
