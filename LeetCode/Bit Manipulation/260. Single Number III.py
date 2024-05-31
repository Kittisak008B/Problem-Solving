# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
# Find the two elements that appear only once. You can return the answer in any order.
# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

# Example 1:
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
  
# Example 2:
# Input: nums = [-1,0]
# Output: [-1,0]

# Example 3:
# Input: nums = [0,1]
# Output: [1,0]
 
# Constraints:  Each integer in nums will appear twice, only two integers will appear once.

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n

        diff_bit = 1
        while (xor & diff_bit) == 0 :
            diff_bit = diff_bit << 1

        num_1 = 0
        for n in nums:
            if (n & diff_bit) != 0 :
                num_1 ^= n
    
        return [num_1, num_1^xor]
'''
[1,2,1,3,2,5]
xor = 3 ^ 5 = 011 ^ 101 = 110 = 6

diff_bit = 010

num_1 = 0 : n = 2,3,2 & diffbits != 0 -> num_1 ^ 010 ^ 011 ^ 010 = 011 = 3 
num_2 = 011 ^ 110 = 101 = 5
'''
