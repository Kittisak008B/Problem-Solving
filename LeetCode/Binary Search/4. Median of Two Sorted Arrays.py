# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x , y = nums1 , nums2
        if len(x) > len(y) :
            x , y = y , x
        start , end = 0 , len(x)  
        while start <= end :
            partition_x = (start + end) // 2
            partition_y = ( len(x)+len(y)+1 )//2 - partition_x

            max_left_x = x[partition_x - 1] if partition_x != 0 else float('-inf')
            min_right_x = x[partition_x] if partition_x != len(x) else float('inf')
            max_left_y = y[partition_y - 1] if partition_y != 0 else float('-inf')
            min_right_y = y[partition_y] if partition_y != len(y) else float('inf')

            if max_left_x <= min_right_y and max_left_y <= min_right_x :
                if (len(x) + len(y)) % 2 == 1 :
                    return max(max_left_x , max_left_y)
                else :
                    return (max(max_left_x , max_left_y) + min(min_right_x , min_right_y)) / 2
            elif max_left_y > min_right_x :
                start = partition_x + 1
            else :
                end = partition_x - 1
'''
x = [2,8,9,10]       
y = [1,3,4,6,7,12]

start , end = 0 , len(x)
partition_x = (start + end) // 2
partition_y = (len(x)+len(y)+1)//2 - partition_x

partition_x = 2 -> partition_y = 3
      left    right
x : 2 8     | 9 10
y : 1 3 4   | 6 7 12
check 4 <= 9 and 8 <= 6 ->False -> end = partition_x - 1 -> partition_x = (0 + 3)//2 = 1 -> partition_y=4

x : 2       | 8 9 10
y : 1 3 4 6 | 7 12
check 6 <= 8 and 2 <= 7 -> True -> if len(x)+len(y)= even return (max(2,6)+min(8,7))/2 =(6+7)/2 
'''
