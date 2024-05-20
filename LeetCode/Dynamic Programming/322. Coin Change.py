# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin. 

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def get_result(coins , amount) :
            if amount in memo :
                return memo[amount]
            min_coin_need = float('inf')
            for coin in coins :
                if coin <= amount :
                    min_coin_need = min(min_coin_need , get_result(coins , amount - coin) + 1)
            memo[amount] = min_coin_need
            return min_coin_need

        memo = {}
        memo[0] = 0
        for coin in coins :
            if coin <= amount :
                memo[coin] = 1

        ans = get_result(coins , amount)
        if ans != float('inf') :
            return ans
        else :
            return -1
'''
Top Down DP(Memoization)
ex. coins=[1,2,5] amount=6
     {6:2}_________  min_coin_need -> min(1,2,1)+1 = 2 coin#
   1/     2|      5\
   {5:1}  {4:2}    {1:1}
  1|
   {4:2}_______________________
  1|                     2\   5\  
   {3:2} ____________    {2:1}  x
  1|          2|    5\
   {2need1} {1need1}  x
  1|
   {1 need 1 coin}
  1|
   {0 need 0 coin}  
'''

# Bottom Up DP(Tabulation)
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = []
#         for i in range(amount+1) :
#             dp.append(float('inf'))
#         dp[0] = 0

#         for i in range(1 , amount+1) :
#             for coin in coins :
#                 if coin <= i :
#                     dp[i] = min(dp[i] , dp[i-coin] + 1)
#         return dp[amount] if dp[amount] != float('inf') else -1

'''
coins = [1,2,5], amount = 6

[ 0 inf inf inf inf inf inf]
  0  1   2   3   4   5   6

i=1
[ 0  1 inf inf  inf inf inf]
  0  1   2   3   4   5   6

i=2
[ 0  1   1 inf  inf inf inf]
  0  1   2   3   4   5   6
  
i=3
[ 0  1   1   2  inf inf inf]
  0  1   2   3   4   5   6
.
.
.
dp =[ 0  1   1   2   2   1   2]
      0  1   2   3   4   5   6
'''
