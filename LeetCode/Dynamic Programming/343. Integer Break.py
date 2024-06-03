# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
# Return the maximum product you can get.

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.

# Example 2:
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        def dfs(i) :
            if i in dp :
                return dp[i]
            if i == n :
                dp[i] = 0
            else :
                dp[i] = i
            for j in range(1 , i) :
                val = dfs(j) * dfs(i-j)  
                dp[i] = max(dp[i] , val)
            return dp[i]
        return dfs(n)
'''
   __ 4__
 /    |   \
1,3  2,2  3,1 
'''
