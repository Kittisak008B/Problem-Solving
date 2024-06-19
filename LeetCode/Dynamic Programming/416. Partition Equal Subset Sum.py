# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0 : #array cannot be partitioned into equal sum subsets.
            return False
        dp = {}
        def dfs(i , sum_subset) :
            if i >= len(nums) :
                return sum_subset == total/2
            if sum_subset == total/2 :
                return True
            if sum_subset > total/2 :
                return False
            if (i , sum_subset) in dp :
                return dp[(i , sum_subset)]
            dp[(i , sum_subset)] = dfs(i+1 , sum_subset + nums[i]) or dfs(i+1 , sum_subset)
            return dp[(i , sum_subset)] 
        return dfs(0 , 0)
'''
nums = [1,5,11,5]
        i       

           /        \ 
          1          0         i=0
         / \       /   \  
       1+5   1     5     0     i=1
      / \   / \   / \   / \ 
    17  6  12  1 16  5 11  0   i=2
    F   |  F   | F   |  T  |
       / \    / \   / \   / \
      11  6  6   1 10  5  5  0 i=3
      T   
'''
