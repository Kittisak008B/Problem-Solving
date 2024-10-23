# Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.
# Two nodes of a binary tree are cousins if they have the same depth with different parents.
# Return the root of the modified tree. Note that the depth of a node is the number of edges in the path from the root node to it.

# Example 1:
#        5                   0
#       / \                 / \
#      4   9               0   0
#    /  \    \            / \    \
#   1   10    7          7   7    11    
# Input: root = [5,4,9,1,10,null,7]
# Output: [0,0,0,7,7,null,11]
# Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
# - Node with value 5 does not have any cousins so its sum is 0.
# - Node with value 4 does not have any cousins so its sum is 0.
# - Node with value 9 does not have any cousins so its sum is 0.
# - Node with value 1 has a cousin with value 7 so its sum is 7.
# - Node with value 10 has a cousin with value 7 so its sum is 7.
# - Node with value 7 has cousins with values 1 and 10 so its sum is 11.
  
# Constraints:
# The number of nodes in the tree is in the range [1, 10**5].
# 1 <= Node.val <= 10**4

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])
        level_sum = []
        while queue :
            cur_level = 0
            for _ in range(len(queue)) :
                node = queue.popleft()
                cur_level += node.val
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
            level_sum.append(cur_level)
        q = collections.deque([(root , root.val)])
        level = 0 
        while q :
            for _ in range(len(q)) :
                node , child_sum_val = q.popleft()
                node.val = level_sum[level] - child_sum_val
                child_sum_val = (node.left.val if node.left else 0 ) + (node.right.val if node.right else 0)
                if node.left :
                    q.append((node.left , child_sum_val))
                if node.right :
                    q.append((node.right , child_sum_val))
            level += 1
        return root
