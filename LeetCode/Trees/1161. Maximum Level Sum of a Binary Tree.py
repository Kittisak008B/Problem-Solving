# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

# Example 1:
#       1
#      / \
#     7   0
#    / \
#   7  -8
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.

# Example 2:
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        ans =[]
        queue = [root]
        next_q = []
        while queue :
            level = []
            sum = 0
            for node in queue :
                if node.left :
                    next_q.append(node.left)
                if node.right :
                    next_q.append(node.right)
                level.append(node.val)
            for x in level :
                sum += x
            ans.append(sum)
            queue = next_q
            next_q = []
            level = []
        max_val = ans[0]
        ind = 0
        for i in range(len(ans)) :
            if ans[i] > max_val :
                max_val = ans[i]
                ind = i
        return ind + 1
      
