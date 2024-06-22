# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

# Example 1:
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

# Example 2:
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
  
# Example 3:
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = 0
        ans = 0
        l = 0
        m = 0
        for r in range(len(nums)) :
            if nums[r] % 2 == 1 :
                odd += 1
            while odd > k :
                m += 1
                l = m
                odd -= 1
            if odd == k :
                while nums[m] % 2 == 0 :
                    m += 1
                ans += m - l + 1
        return ans
'''
                  r
nums = [2,2,1,1,2,1,1], k = 3
        l
            m     
        odd = 3
        ans += m-l+1 = 2-0+1 = 3  (2 2 1 1 2 1 , 2 1 1 2 1 , 1 1 2 1)
                    r
nums = [2,2,1,1,2,1,1], k = 3
        l
            m     
        odd = 4
                    r
nums = [2,2,1,1,2,1,1], k = 3
              l
              m       
        odd = 3
        ans += 1  (1 2 1 1)
'''
