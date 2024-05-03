# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
 
# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        cur = []
        def backtrack(start) :
            if cur not in ans :
                ans.append(cur[:])
            for i in range(start , len(nums)) :
                cur.append(nums[i])
                backtrack(i+1)
                cur.pop()
        backtrack(0)
        return ans
#        _____ [ ] _____
#       /         |     \
#     [1]        [2]    [2]x
#     /  \        |
#   [1,2][1,2]x   [2,2]
#   /
# [1,2,2]
