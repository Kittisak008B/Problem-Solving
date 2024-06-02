# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# The answer is guaranteed to fit into a signed 32-bit integer.

# Example 1:
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

# Example 2:
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.

# Constraints:  All the values of coins are unique.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp =[ [0 for _ in range(amount +1)] for _ in range(len(coins) +1)] 
        dp[0][0] = 1
        for row in range(1 , len(coins)+1) :
            for col in range(amount +1) :
                if col - coins[row-1] >= 0 :
                    dp[row][col] = dp[row-1][col] + dp[row][col - coins[row-1]]
                else :
                    dp[row][col] = dp[row-1][col] 
        return dp[-1][-1]
'''
       | 0 1 2 3 4 5 amount
     []| 1 0 0 0 0 0 
    [1]| 1 1 1 1 1 1
  [1,2]| 1 1 2 2 3 3
[1,2,5]| 1 1 2 2 3 4 --> 4
'''

# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         dp = {}
#         def dfs(i , value) :
#             if value == amount :
#                 return 1
#             if value > amount or i >= len(coins) :
#                 return 0
#             if (i , value) in dp :
#                 return dp[(i , value)]
#             dp[(i , value)] = dfs(i , value + coins[i]) + dfs(i + 1 , value) #use this coin + skip this coin(use another coin)
#             return dp[(i , value)]
#         return dfs(0 , 0)
