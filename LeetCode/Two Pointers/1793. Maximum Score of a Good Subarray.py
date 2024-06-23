# You are given an array of integers nums (0-indexed) and an integer k.
# The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.
# Return the maximum possible score of a good subarray.

# Example 1:
# Input: nums = [1,4,3,7,4,5], k = 3
# Output: 15
# Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 

# Example 2:
# Input: nums = [5,5,4,5,4,1,1,1], k = 0
# Output: 20
# Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l = k
        r = k
        min_cur = nums[k]
        max_score = nums[k]
        while l > 0 or r < len(nums)-1 :
            if l > 0 and r < len(nums)-1 :
                if nums[l-1] < nums[r+1] :
                    r += 1
                else :
                    l -= 1
            elif l==0 and r < len(nums)-1 :
                r += 1
            elif r==len(nums)-1 and l > 0 :
                l -= 1
            min_cur = min(min_cur , nums[l] , nums[r])
            max_score = max(max_score , min_cur*(r - l + 1))
        return max_score
'''
nums = [1,4,3,7,4,5], k = 3
              k
              l
              r

              min_cur 
              max_score = min_cur*(r-l+1) 
'''
