# Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by 
# the sum of some elements in the array. Return the minimum number of patches required.

# Example 1:
# Input: nums = [1,3], n = 6
# Output: 1
# Explanation:
# Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
# Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
# Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
# So we only need 1 patch.
  
# Example 2:
# Input: nums = [1,5,10], n = 20
# Output: 2
# Explanation: The two patches can be [2, 4].

# Example 3:
# Input: nums = [1,2,2], n = 5
# Output: 0
 
# Constraints: nums is sorted in ascending order.

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch = 0
        max_cover_range = 0
        i=0
        while i < len(nums) and max_cover_range < n :
            if nums[i] <= max_cover_range + 1 :
                max_cover_range += nums[i]
                i += 1
            else :
                patch += 1
                max_cover_range += (max_cover_range+1)
        while max_cover_range < n :
            patch += 1
            max_cover_range += (max_cover_range+1)
        return patch
'''
[1,2,5,10] n = 20
range[0,0] add 1 ->cover range[0,1] 
           add 2 ->cover range[0,3]
           cant add 5 (need add 4 first)
           add 4 ->cover range[0,7]   (patch += 1)
           add 5 -> cover range[0,12]
           add 10 -> cover range[0,22]
# can add if num <= max_cover_range + 1
'''
