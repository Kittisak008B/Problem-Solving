# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,3,4]
        # prefix [1,1,2,6,24]
        # suffix [24,24,12,4,1]
        prefix = [1]
        for x in nums :
            prefix.append(prefix[-1]*x)
        suffix = [1]
        for x in nums[::-1] :
            suffix.append(suffix[-1]*x)
        suffix = suffix[::-1]
        ans = []
        for i in range(len(nums)) :
            ans.append(prefix[i]*suffix[i+1])
        return ans
