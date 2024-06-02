# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like 
# (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

# Example 2:
# Input: prices = [1]
# Output: 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2 :
            return 0
        dp = {}
        def dfs(i , can_buy) :
            if i >= len(prices) :
                return 0
            if (i , can_buy) in dp :
                return dp[(i , can_buy)]
            if can_buy :
                buy = dfs(i+1 , False) - prices[i]
                cooldown = dfs(i+1 , True)
                dp[(i , can_buy)] = max(buy , cooldown)
            else :
                sell = dfs(i+2 , True) + prices[i]
                cooldown = dfs(i+1 , False)
                dp[(i , can_buy)] = max(sell , cooldown)
            return dp[(i , can_buy)]
        return dfs(0 , True)

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) < 2 :
#             return 0
#         buy = [0 for _ in range(len(prices))]
#         max_Profit = [0 for _ in range(len(prices))]
#         buy[0] = prices[0]
#         buy[1] = min(prices[0] , prices[1])
#         max_Profit[0] = 0
#         max_Profit[1] = max(max_Profit[0] , prices[1] - prices[0])

#         for i in range(2 , len(prices)) :
#             buy[i] = min(buy[i-1] , prices[i] - max_Profit[i-2])
#             max_Profit[i] = max(max_Profit[i-1] , prices[i] - buy[i-1])

#         return max_Profit[-1]
'''
    prices = [1, 2, 3, 0, 2]
              b  s  c  b  s
    buy    = [1, 1, 1,-1,-1]
    
max_Profit = [0, 1, 2, 2, 3]
------------------------------
     price = [1, 2, 3, 0, 2, 1, 2, 3, 0, 1, 6]
              b        b              b
       buy = [1, 1, 1,-1,-1,-1,-1,-1,-3,-3,-3]
                               
max_Profit = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 9]
'''
