# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.    Given n, calculate F(n).

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

class Solution:
    def fib(self, n: int) -> int:
        ans = [0,1]
        for i in range(2 , n+1) :
            ans.append(ans[i-2] + ans[i-1])
        return ans[n]
      
# class Solution:
#     def fib(self, n: int) -> int:
#         memo = {0:0 ,1:1}
#         def fibo(n) :
#             if n in memo :
#                 return memo[n]
#             else :
#                 memo[n] = fibo(n-2) + fibo(n-1)
#                 return memo[n]
#         return fibo(n)
