# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
# Note:
# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# The transaction fee is only charged once for each stock purchase and sale.

# Example 1:
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

# Example 2:
# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2 :
            return 0
        dp = {}
        def dfs(i , state) : #state = True -> can buy or cooldown , state = False : can sell or cooldown
            if i >= len(prices) :
                return 0
            if (i , state) in dp :
                return dp[(i , state)]
            if state :
                buy = dfs(i+1 , not state) - prices[i]
                cooldown = dfs(i+1 , state)
                dp[(i , state)] = max(buy , cooldown)
            else :
                sell = dfs(i+1 , not state) + prices[i] - fee
                cooldown = dfs(i+1 , state)
                dp[(i , state)] = max(sell , cooldown)
            return dp[(i , state)]
        return dfs(0, True)
      
