# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Example 1:
#        1
#       / \ 
#      3   2
#     / \    \
#    5   3    9
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]

# Constraints:
# The number of nodes in the tree will be in the range [0, 104].
# -2**31 <= Node.val <= 2**31 - 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []
        res = []
        q = collections.deque([root])
        while q :
            max_val = float('-inf')
            for _ in range(len(q)) :
                node = q.popleft()
                max_val = max(max_val , node.val)
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            res.append(max_val)
        return res
      
