# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(1 , len(nums)) :
            for j in range(i) :
                if nums[j] < nums[i] :
                    dp[i] = max(dp[i] , dp[j] + 1)
        return max(dp)
    '''
      [10,9,2,5,3,7,101,18]
                         i
                     j      
   dp [1 ,1,1,2,2,3, 4 , 4]
    '''
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         tails = [0 for _ in range(len(nums))]    #O(N*log(N))
#         size = 0 
#         for x in nums :
#             i , j = 0 , size
#             while i != j :
#                 m = (i+j)//2
#                 if tails[m] < x :
#                     i = m + 1
#                 else :
#                     j = m
#             tails[i] = x
#             size = max(size , i + 1)
#         return size
'''
nums = [10,9,2,5,3,7,101,18]
                         
tails = 10
        9  
        2
        2 5
        2 3
        2 3 7
        2 3 7 101
        2 3 7 18
'''
