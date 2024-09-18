# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string instead of an integer.

# Example 1:
# Input: nums = [10,2]
# Output: "210"

# Example 2:
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
 
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10**9

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        sorted_numbers = sorted(nums, key=lambda x: str(x) * 10, reverse=True)
        ans = ''.join(str(i) for i in sorted_numbers)
        return ans if ans[0] != '0' else '0'
'''
Multiplying by 10 works because it creates a large enough string for lexicographical comparison
nums = [3,30,34,5,9]
str(30)*10 = '30303030303030303030'
str(3)*10 = '3333333333'  
str(34)*10 = '34343434343434343434'
str(5)*10 = '5555555555'
str(9)*10 = '9999999999'

'9999999999'>'5555555555'>'34343434343434343434'>'3333333333'>'30303030303030303030'
sorted_numbers = [9, 5, 34, 3, 30]
'''
