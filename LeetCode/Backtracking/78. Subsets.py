# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
 
# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans , subset = [] , []
        def backtrack(i) :
            if i == len(nums) :
                ans.append(subset[:])
                return
            # NOT include nums[i]
            backtrack(i+1)
            # include nums[i]
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
        backtrack(0)
        return ans
#               [ ]
#             /      \
#         [ ]          [1]
#        /  \          /   \
#    [ ]   [2]        [1]    [1,2]
#   / \    /  \       /  \      /  \
# [ ] [3] [2] [2,3] [1] [1,3] [1,2] [1,2,3] 

# sol2
#class Solution:
#    def subsets(self, nums: List[int]) -> List[List[int]]:
#        ans = []
#        cur = []
#        def backtrack(start) :
#            ans.append(cur[:])
#            for i in range(start , len(nums)) :
#                cur.append(nums[i])
#                backtrack(i+1)
#                cur.pop()
#        backtrack(0)
#        return ans
     
#        _____ [ ] _____
#       /         |     \
#     [1]        [2]    [3]
#     /  \        |
#   [1,2][1,3]   [2,3]
#   /
# [1,2,3]
