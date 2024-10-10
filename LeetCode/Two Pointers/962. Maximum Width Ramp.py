# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.
# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

# Example 1:
# Input: nums = [6,0,8,2,1,5]
# Output: 4
# Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.

# Example 2:
# Input: nums = [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 
# Constraints:
# 2 <= nums.length <= 5 * 10**4
# 0 <= nums[i] <= 5 * 10**4

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        right_max = [0] * len(nums)
        right_max[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1) :
            right_max[i] = max(right_max[i + 1], nums[i])
        res = 0
        l = 0
        for r in range(len(nums)) :
            while right_max[r] < nums[l] :
                l += 1
            res = max(res , r-l)
        return res
      
