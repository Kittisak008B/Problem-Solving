# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left, max_right = [0]*n, [0]*n
        left, right = 0, 0
        for i in range(n) :
            j = -i -1
            left = max(left , height[i])
            right = max(right , height[j])
            max_left[i] = left
            max_right[j] = right
        final_list = [0]*n
        for i in range(len(height)) :
            final_list[i] = min(max_left[i],max_right[i]) - height[i]
        ans = 0
        for x in final_list :
            ans += x
        return ans
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6    
# max_left =                [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
# max_right =               [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
# min(max_left,max_right) = [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
# final_list =              [0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0]
