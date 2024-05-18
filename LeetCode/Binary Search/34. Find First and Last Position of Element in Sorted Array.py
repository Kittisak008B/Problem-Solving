# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].   You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
 
# Constraints:  nums is a non-decreasing array.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def start_index(arr , target) :
            if arr[0] == target :
                return 0
            i = 0
            j = len(arr) - 1
            while i <= j :
                mid = (i+j)//2
                if arr[mid] == target and arr[mid - 1] < target :
                    return mid
                elif arr[mid] < target :
                    i = mid + 1
                elif arr[mid] > target :
                    j = mid - 1
                else :
                    j = mid - 1
            return -1
          
        def end_index(arr , target) :
            if arr[-1] == target :
                return len(arr) - 1
            i = 0
            j = len(arr) - 1
            while i <= j :
                mid = (i+j)//2
                if arr[mid] == target and arr[mid + 1] > target :
                    return mid
                elif arr[mid] > target :
                    j = mid - 1
                elif arr[mid] < target :
                    i = mid + 1
                else :
                    i = mid + 1
            return -1
          
        if len(nums) == 0 or target > nums[-1] or target < nums[0] :
            return [-1,-1]
        return [start_index(nums , target) , end_index(nums , target)]
      
