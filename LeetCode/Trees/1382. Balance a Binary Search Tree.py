# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

# Example 1:
#           1
#             \ 
#               2                    2                3
#                 \          ->     / \     or       /  \
#                   3              1   3            1    4
#                     \                 \            \   
#                      4                 4            2
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
  
# Example 2:
# Input: root = [2,1,3]
# Output: [2,1,3]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root , value) :
            if not root :
                return
            inorder(root.left , value)
            value.append(root.val)
            inorder(root.right , value)
        value = []
        inorder(root , value)

        def built_bst(left , right) :
            if left > right : return None
            mid = (left + right)//2
            root = TreeNode(value[mid])
            root.left = built_bst(left , mid -1)
            root.right = built_bst(mid +1 , right)
            return root
        return built_bst(0 , len(value)-1)
'''
root = [1,null,2,null,3,null,4,null,null]

inorder -> value = [1,2,3,4]
built_bst -> root = [2,1,3,null,null,null,4]
'''
