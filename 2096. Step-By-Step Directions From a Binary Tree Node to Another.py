# You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. 
# You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
# Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. 
# Each letter indicates a specific direction:
# 'L' means to go from a node to its left child node.
# 'R' means to go from a node to its right child node.
# 'U' means to go from a node to its parent node.
# Return the step-by-step directions of the shortest path from node s to node t.

# Example 1:
# Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
# Output: "UURL"
# Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

# Constraints:
# The number of nodes in the tree is n.
# 2 <= n <= 10**5
# 1 <= Node.val <= n
# All the values in the tree are unique.
# 1 <= startValue, destValue <= n
# startValue != destValue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def get_path(node , path , target):
            if not node :
                return []
            if node.val == target :
                return path
            if node.left :
                path.append('L')
                res = get_path(node.left , path , target)
                if res :
                    return res
                path.pop()
            if node.right :
                path.append('R')
                res = get_path(node.right , path , target)
                if res :
                    return res
                path.pop()
            return []      
        start_path = get_path(root , [] , startValue)
        dest_path = get_path(root , [] , destValue)
 
        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i] :
            i += 1
        ans = ''
        ans += 'U'*len(start_path[i:]) + ''.join(dest_path[i:])
        return ans
      
