# Given an array of integers nums and an integer limit, 
# return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

# Example 1:
# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.

# Example 2:
# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4 
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

# Example 3:
# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        longest = 0
        min_heap = []
        max_heap = []
        l = 0
        for r in range(len(nums)) :
            heapq.heappush(min_heap , (nums[r],r))
            heapq.heappush(max_heap , (-nums[r],r))

            while min_heap[0][1] < l :
                heapq.heappop(min_heap)
            while max_heap[0][1] < l :
                heapq.heappop(max_heap)

            if abs(max_heap[0][0]+min_heap[0][0]) <= limit :
                longest = max(longest , r-l+1)
            else :
                l += 1
        return longest
'''
nums = [8,2,4,7,3], limit = 4
            l   
                r
two heap min_heap = [8]             max_heap = [-8]          ->ok longest = 1 (8)
         min_heap = [2 , 8]         max_heap = [-8 -2]       ->not ok max_abs_diff > 4  pop 8
         min_heap = [2 , 4 , 8]     max_heap = [-4 , -2]     ->ok longest = 2 (2,4)
         min_heap = [2 , 4 , 7 , 8] max_heap = [-7, -4 , -2] ->not ok pop 2
         min_heap = [3 , 4 , 7 , 8] max_heap = [-7, -4 , -2] ->ok longest = 3 (4,7,3)
'''
