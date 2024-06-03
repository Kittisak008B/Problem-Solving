# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2
 
# Constraints:  It's guaranteed that you can reach nums[n - 1].

class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_index = 0
        max_reach = 0
        ans = 0

        i = 0
        while i < len(nums) and cur_index < len(nums) -1 :
            max_reach = max(max_reach , nums[i] + i)
            if i == cur_index :
                cur_index = max_reach
                ans += 1
            i += 1
        return ans
'''
[2,3,1,1,4]
i=0 max_reach = 2 cur_index = 2 ans =1
i=1 max_reach = 4 cur_index = 2 ans =1
i=2 max_reach = 4 cur_index = 4 ans =2 -> return 2
'''
