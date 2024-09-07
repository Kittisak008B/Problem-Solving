# Given a binary tree root and a linked list with head as the first node. 
# Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.
# In this context downward path means a path that starts at some node and goes downwards.

# Example 1:
#       1
#    /      \
#   4         4 *
#    \       /
#     2     2 *
#     /    / \
#   1     6   8 *
#            / \ 
#           1   3
# Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# Explanation: Nodes in blue form a subpath in the binary Tree.  
  
# Constraints:
# The number of nodes in the tree will be in the range [1, 2500].
# The number of nodes in the list will be in the range [1, 100].
# 1 <= Node.val <= 100 for each node in the linked list and binary tree.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def helper(root , head) :
            if not head : 
                return True
            if not root : 
                return False
            if root.val == head.val:
                if helper(root.left , head.next) : 
                    return True
                if helper(root.right , head.next) : 
                    return True
            return False
        def dfs(root) :
            if not root : 
                return False
            if helper(root , head) : 
                return True
            if dfs(root.left) : return True
            if dfs(root.right) : return True
            return False
        return dfs(root)
