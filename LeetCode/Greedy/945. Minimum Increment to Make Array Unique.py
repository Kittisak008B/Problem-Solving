# You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
# Return the minimum number of moves to make every value in nums unique.
# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:
# Input: nums = [1,2,2]
# Output: 1
# Explanation: After 1 move, the array could be [1, 2, 3].

# Example 2:
# Input: nums = [3,2,1,2,1,7]
# Output: 6
# Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums) - 1) :
            if nums[i] >= nums[i+1] :
                diff = nums[i] - nums[i+1] + 1
                ans += diff
                nums[i+1] += diff
        return ans
'''
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ans = 66
'''
