# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:
#   root                 subRoot
#     3                     4
#    / \                   / \
#   4   5                 1   2
#  / \
# 1   2
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:
#   root                 subRoot
#     3                     4
#    / \                   / \
#   4   5                 1   2
#  / \
# 1   2
#    /
#    0
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sub_tree(a , b) :
            if not a :
                return False
            if not b :
                return True
            if same_tree(a , b) :
                return True
            return sub_tree(a.left , b) or sub_tree(a.right , b)
            
        def same_tree(a , b) :
            if not a and not b :
                return True
            if (a and not b) or (b and not a) :
                return False
            if a.val != b.val :
                return False
            return same_tree(a.left , b.left) and same_tree(a.right , b.right)

        return sub_tree(root , subRoot)
      
