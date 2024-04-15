# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        for i in range(len(nums)) :
            hm[nums[i]] = 1 + hm.get(nums[i] , 0)
        for key , value in hm.items() :
            if value > len(nums)/2 :
                return key
        return 0 
      
        # hm = defaultdict(int)
        # for i in range(len(nums)) :
        #    hm[nums[i]] += 1

        # for key , value in hm.items():
        #     if value > len(nums)/2 :
        #         return key
        # return 0
