# Given two arrays nums1 and nums2. Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.
# A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters 
# without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

# Example 1:
# Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# Output: 18
# Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
# Their dot product is (2*3 + (-2)*(-6)) = 18.

# Example 2:
# Input: nums1 = [3,-2], nums2 = [2,-6,7]
# Output: 21
# Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
# Their dot product is (3*7) = 21.

# Example 3:
# Input: nums1 = [-1,-1], nums2 = [1,1]
# Output: -1
# Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
# Their dot product is -1.

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1) < 0 and min(nums2) > 0 :
            return max(nums1)*min(nums2)
        if max(nums2) < 0 and min(nums1) > 0 :
            return max(nums2)*min(nums1)
        dp = {}
        def dfs(i , j) :
            if i == len(nums1) or j == len(nums2) :
                return 0
            if (i , j) in dp :
                return dp[(i , j)]
            dot_product = max(nums1[i]*nums2[j] + dfs(i+1 , j+1) , dfs(i+1 , j) , dfs(i , j+1))
            dp[(i , j)] = dot_product
            return dp[(i , j)]
        return dfs(0 , 0)


# class Solution:
#     def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
#         if max(nums1) < 0 and min(nums2) > 0 :
#             return max(nums1)*min(nums2)
#         if max(nums2) < 0 and min(nums1) > 0 :
#             return max(nums2)*min(nums1)
#         if len(nums1) > len(nums2) :
#             nums1 , nums2 = nums2 , nums1
#         dp = [[0 for _ in range(len(nums1)+1)] for _ in range(len(nums2)+1)]
#         for row in range(len(nums2)-1 , -1 , -1) :
#             for col in range(len(nums1)-1 , -1 , -1) :
#                 dp[row][col] = max(nums2[row]*nums1[col] +dp[row+1][col+1] , dp[row+1][col] , dp[row][col+1])
#         return dp[0][0]
'''
       idx0   1   2  
          3  -2      nums1
idx     
0    2    21  12  0
1   -6    21  12  0
2    7    21  0   0
3         0   0   0 
    nums2
'''

# class Solution:    # bottom up space optimized
#     def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
#         if max(nums1) < 0 and min(nums2) > 0 :
#             return max(nums1)*min(nums2)
#         if max(nums2) < 0 and min(nums1) > 0 :
#             return max(nums2)*min(nums1)
#         if len(nums1) > len(nums2) :
#             nums1 , nums2 = nums2 , nums1
#         dp = [0 for _ in range(len(nums1)+1)]
#         for row in range(len(nums2)-1 , -1 ,-1) :
#             cur_dp = [0 for _ in range(len(nums1)+1)]
#             for col in range(len(nums1)-1 , -1 ,-1) :
#                 cur_dp[col] = max(nums2[row]*nums1[col] + dp[col+1] , dp[col] , cur_dp[col+1]) 
#             dp = cur_dp
#         return dp[0]
'''
       idx0   1   2  
          3  -2      nums1
idx     
0    2    21  12  0                                                    cur_dp  dp
1   -6    21  12  0                                      cur_dp        dp
2    7    21  0   0      cur_dp = [0 , 0 , 0]->[21,0,0]->dp=[21,0,0]
3         0   0   0      dp = [0 , 0 , 0]
    nums2
'''
