# Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.
# Return the result as a list of indices representing the starting position of each interval (0-indexed). 
# If there are multiple answers, return the lexicographically smallest one.

# Example 1:
# Input: nums = [1,2,1,2,6,7,5,1], k = 2
# Output: [0,3,5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

# Constraints:
# 1 <= nums.length <= 2 * 10**4
# 1 <= nums[i] < 2**16
# 1 <= k <= floor(nums.length / 3)

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        dp = {}
        def dfs(idx , used) :
            if used == 3 :
                return (0 , [])
            if idx + k - 1 >= len(nums) :
                return (0 , [])
            if (idx , used) in dp :
                return dp[(idx , used)]
            take_sum , take_idx = dfs(idx + k , used + 1)
            take_sum += sum(nums[idx:idx + k])
            skip_sum , skip_idx = dfs(idx + 1 , used)
            if take_sum >= skip_sum :
                dp[(idx , used)] = (take_sum , [idx] + take_idx)
                return dp[(idx , used)]
            else :
                dp[(idx , used)] = (skip_sum , skip_idx)
                return dp[(idx , used)]
        res = dfs(0 , 0)
        return res[1]
      
