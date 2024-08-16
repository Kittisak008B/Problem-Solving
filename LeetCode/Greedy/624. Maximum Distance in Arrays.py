# You are given m arrays, where each array is sorted in ascending order.
# You can pick up two integers from two different arrays (each array picks one) and calculate the distance. 
# We define the distance between two integers a and b to be their absolute difference |a - b|. Return the maximum distance.

# Example 1:
# Input: arrays = [[1,2,3],[4,5],[1,2,3]]
# Output: 4
# Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
  
# Example 2:
# Input: arrays = [[1],[1]]
# Output: 0

# Constraints:
# m == arrays.length
# 2 <= m <= 10**5
# 1 <= arrays[i].length <= 500
# -10**4 <= arrays[i][j] <= 10**4
# arrays[i] is sorted in ascending order. There will be at most 10**5 integers in all the arrays.

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min = arrays[0][0]
        cur_max = arrays[0][-1]
        max_dist = 0
        for arr in arrays[1:] :
            max_dist = max(max_dist , max(arr[-1] - cur_min , cur_max - arr[0]))
            cur_min = min(cur_min , arr[0])
            cur_max = max(cur_max , arr[-1])
        return max_dist
