# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
# Return the minimized largest sum of the split.  A subarray is a contiguous part of the array.

# Example 1:
# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

# Example 2:
# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def min_subarray(nums , search_range_sum) :
            cur_sum = 0
            subarray = 1
            for num in nums :
                if cur_sum + num <= search_range_sum :
                    cur_sum += num
                else :
                    cur_sum = num
                    subarray += 1
            return subarray
        left = max(nums)
        right = sum(nums)
        while left < right :
            search_range_sum = left + (right-left )// 2
            if min_subarray(nums , search_range_sum) <= k :
                right = search_range_sum 
            else :
                left = search_range_sum + 1
        return left
'''
nums = [7,2,5,10,8], k = 2
7 | 2 5 10 8   largest sum = 25
7 2 | 5 10 8   -> 23
7 2 5 | 10 8   -> 18 ## minimized largest sum of the split
7 2 5 10 | 8   -> 24

largest sum of the split-> search range [max(nums) ... sum(nums)]
                                        [10 , 11 ... 31 , 32]
                                        left              right 
search_range_sum = (10+32)//2 = 21
7 2 5 | 10 8 (7+2+5)<=21 & (10+8)<=21 ->subarray = 2    2<=k ->right=21

search_range_sum =(10+21)//2 = 15
7 2 5 | 10 |8 (7+2+5)<=15 & 10 <=15 & 8<=15 -> subarray=3  3>k -> left = 15+1 = 16

search_range_sum = (16+21)//2 = 18
7 2 5 | 10 8 (7+2+5)<=18 & (10+8)<=18 ->subarray = 2    2<=k ->right=18

search_range_sum =(16+18)//2 = 17
7 2 5 | 10 |8 (7+2+5)<=17 & 10 <=17 & 8<=17 -> subarray=3  3>k -> left = 17+1 = 18 
                                              #left=18 right=18 out of while loop-> return left = 18
'''
