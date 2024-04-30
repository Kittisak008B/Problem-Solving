# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
  
# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:

        def fibo(n, memo={}) :
            if n <= 1 :
                return n
            if n in memo :
                return memo[n]    
            memo[n] = fibo(n-1, memo) + fibo(n-2 , memo)
            return memo[n]

        return fibo(n+1, {})
# 1 : 1
# 2 : 2 , 1+1
# 3 : 2+1 , 1+1+1 , 1+2
# 4 : 2+1+1 , 1+1+1+1 , 1+2+1 , 2+2 , 1+1+2
# 1 2 3 5 8 13
