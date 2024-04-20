# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        j = 0
        zero2one = 0
        max_one = 0
        for i in range(len(nums)) :
            if nums[i] == 0 :
                zero2one += 1
            while zero2one > k :
                if nums[j] == 0 :
                    zero2one -= 1
                j += 1
            max_one = max(max_one , i-j+1)
        return max_one
