# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
# That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected,
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def houseRobber(nums) :
            for i in range(1 , len(nums)) :
                if i == 1 :
                    nums[i] = max(nums[i] , nums[i-1])
                else :
                    nums[i] = max(nums[i]+nums[i-2] , nums[i-1])
            return nums[-1]

        if len(nums) == 1 :
            return nums[0]
        return max(houseRobber(nums[1:]) , houseRobber(nums[:-1]))

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         def houseRobber(nums) :
#             dp1 = 0
#             dp2 = 0
#             for num in nums :
#                 dp1 , dp2 = dp2 , max(dp1 + num , dp2)
#             return dp2
#         if len(nums) == 1 :
#             return nums[0]
#         return max(houseRobber(nums[1:]) , houseRobber(nums[:-1]))
