# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
# Example 1:
#    1         1
#   / \       / \
#  2   3     2   3 
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:
#     1      1
#    /        \
#   2           2
# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same_tree(p , q) :
            if not p and not q :
                return True
            if (p and not q) or(q and not p) :
                return False
            if p.val != q.val :
                return False
            return same_tree(p.left , q.left) and same_tree(p.right , q.right)
        return same_tree(p , q)
      
