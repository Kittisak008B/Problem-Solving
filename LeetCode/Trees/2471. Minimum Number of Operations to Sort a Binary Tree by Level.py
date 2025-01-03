# You are given the root of a binary tree with unique values.
# In one operation, you can choose any two nodes at the same level and swap their values.
# Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.
# The level of a node is the number of edges along the path between it and the root node.

# Example 1:
#            1
#          /   \
#         4     3
#       /  \   / \ 
#      7   6  8   5
#            /   /
#           9   10    
# Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
# Output: 3
# Explanation:
# - Swap 4 and 3. The 2nd level becomes [3,4].
# - Swap 7 and 5. The 3rd level becomes [5,6,8,7].
# - Swap 8 and 7. The 3rd level becomes [5,6,7,8].
# We used 3 operations so return 3. It can be proven that 3 is the minimum number of operations needed.

# Constraints:
# The number of nodes in the tree is in the range [1, 10**5].
# 1 <= Node.val <= 10**5
# All the values of the tree are unique.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root]) 
        count = 0
        while q :
            level = []
            for _ in range(len(q)) :
                node = q.popleft() 
                level.append(node.val)
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            sort_level = sorted(level)
            d = {x : i for i , x in enumerate(level)}
            for i in range(len(level)) :
                while level[i] != sort_level[i] :
                    count += 1
                    j = d[sort_level[i]]
                    d[level[i]] = j
                    level[i] , level[j] = level[j] , level[i]
        return count
      
