# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

# Example 2:
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp= [[0 for _ in range(len(prices))] for _ in range(k + 1)]
        for r in range(1, k + 1) :
            effective_buyprice = prices[0]
            for c in range(1 , len(prices)) :
                no_trans = dp[r][c-1]
                dp[r][c] = max(no_trans , prices[c] - effective_buyprice)
                effective_buyprice = min(effective_buyprice , prices[c] - dp[r-1][c])         
        return dp[-1][-1]
      
# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         dp= [[0 for _ in range(len(prices))] for _ in range(k + 1)]
#         for r in range(1, k + 1) :
#             for c in range(1 , len(prices)) :
#                 no_trans = dp[r][c-1]
#                 complete_trans = 0
#                 for buy_day in range(c) :
#                     complete_trans = max(complete_trans , prices[c] - prices[buy_day] + dp[r-1][buy_day])
#                 dp[r][c] = max(no_trans , complete_trans)
#         return dp[-1][-1]   -> Time Limit Exceeded   Time:O(K*N*N) Space:O(K*N)
'''
   0 1 2 3 4 5 6 7  day
   3 2 6 5 0 3 1 5  price
0  0 0 0 0 0 0 0 0 
1  0 0 4 4 4 4 4 5
2  0 0 4 4 4 7 7 9
3  0 0 4 4 4 7 7 11
k (transactions)

no transaction : dp[r][c] = dp[r][c-1]
complete k transaction this day : for buy_day = 0 to day - 1 -> dp[r][c] = price[c] - price[buy_day] + dp[r-1][buy_day]

r,c=1,1 : no trans=0 , complete 1 trans@day1  2-3=-1 max(0,-1)= 0
r,c=1,2 : no trans=0 , complete 1 trans@day2  buy_day@day0 6-3= 3 buy_day@day1 6-2= 4 max(4,3,0)= 4
r,c=1,3 : no trans=4 , complete 1 trans@day3  max(5-3 ,5-2, 5-6 ,4) = 4
...
r,c=1,5 : no trans=4 , complete 1 trans@day5 buy_day@day0 5-3=2 ... buy_day@day4 5-0=5 max(5-3,5-2,5-6,5-0,5-3,5-1,4)=5

r,c=2,1 : no trans=0 , complete 2 trans@day1 2-3+0=-1 max(-1,0)=0
r,c=2,2 : no trans=0 , complete 2 trans@day2 buy_day@day0 6-3+0=3 buy_day@day1 6-2+0=4 max(4,3,0) = 4
...
r,c=2,5 : no trans=4 , complete 2 trans@day5 buy@day0 3-3+0=0 buy@day1 3-2+0=1 buy@day2 3-6+4=1 buy@day3 3-5+4=2 buy@day4 3-0+4=7
                       max(7,2,1,1,0,4) = 7
...
r,c=3,7
'''

# Memoization
# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         dp = {}
#         def dfs(i , can_buy , trans_remain) :
#             if i >= len(prices) or trans_remain == 0 :
#                 return 0
#             if (i , can_buy , trans_remain) in dp :
#                 return dp[(i , can_buy , trans_remain)]
#             if can_buy :
#                 buy = dfs(i + 1 , False , trans_remain) - prices[i]
#                 cooldown = dfs(i + 1 , True , trans_remain)
#                 dp[(i , can_buy , trans_remain)] = max(buy , cooldown)
#             else :
#                 sell = dfs(i + 1 , True , trans_remain -  1) + prices[i]
#                 cooldown = dfs(i + 1 , False , trans_remain)
#                 dp[(i , can_buy , trans_remain)] = max(sell , cooldown)
#             return dp[(i , can_buy , trans_remain)]
#         return dfs(0 , True , k)
