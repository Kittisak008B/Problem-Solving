# You have n dice, and each dice has k faces numbered from 1 to k.
# Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

# Example 1:
# Input: n = 1, k = 6, target = 3
# Output: 1
# Explanation: You throw one die with 6 faces.  There is only one way to get a sum of 3.
  
# Example 2:
# Input: n = 2, k = 6, target = 7
# Output: 6
# Explanation: You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

# Example 3:
# Input: n = 30, k = 30, target = 500
# Output: 222616187
# Explanation: The answer must be returned modulo 109 + 7.

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        memo = {}
        def dfs(n , target) :
            if target <= 0 or target > (n * k) :
                return 0
            if n == 1 and target <= k :
                return 1
            if (n , target) in memo :
                return memo[(n , target)]
            ways = 0
            for val in range(1 , k + 1) :
                ways = (ways + dfs(n-1 , target - val) ) % mod
                memo[(n , target)] = ways
            return memo[(n , target)]
        return dfs(n,target)
'''
dfs(n=2,target=7) k=6
ways += dfs(n=1,target=6,5,4,3,2,1,0)
dfs(1,0) = 0
dfs(1,1) = 1
dfs(1,2) = 1
dfs(1,3) = 1
dfs(1,4) = 1
dfs(1,5) = 1
dfs(1,6) = 1 ways = 6
'''

# class Solution:
#     def numRollsToTarget(self, n: int, k: int, target: int) -> int:
#         mod = 10**9 + 7
#         dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
#         dp[0][0] = 1
#         for row in range(n+1) :
#             for col in range(target+1) :
#                 for val in range(1 , k+1) :
#                     if col - val >= 0 :
#                         dp[row][col] = ( dp[row][col] + dp[row-1][col-val] ) % mod
#         return dp[-1][-1]
'''
ex.2 Input: n = 2, k = 6, target = 7

  0 1 2 3 4 5 6 7 target  k=6
0 1 0 0 0 0 0 0 0 
1 0 1 1 1 1 1 1 1
2 0 0 1 2 3 4 5 6
n
'''
