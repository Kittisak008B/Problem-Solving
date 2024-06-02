# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
# with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
 
# Constraints:   nums[i] is either 0, 1, or 2.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        b = len(nums) -1 
        while w <= b :
            if nums[w] == 2 :
                nums[w] ,nums[b] = nums[b] ,nums[w]
                b -=1
            elif nums[w] == 0 :
                nums[w] ,nums[r] = nums[r] ,nums[w]
                w += 1
                r += 1
            else :
                w += 1           
'''
[2 ,0 ,2 ,1 ,1 ,0 ,1]
r,w                b
 1  0  2  1  1  0  2
r,w             b
 r  w           b
 0  1  2  1  1  0  2
    r  w        b
 0  1  0  1  1  2  2
    r  w     b
 0  0  1  1  1  2  2
       r  w  b
       r    w,b
       r     b  w                       
'''
