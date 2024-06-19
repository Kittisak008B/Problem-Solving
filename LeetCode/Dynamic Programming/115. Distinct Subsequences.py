# Given two strings s and t, return the number of distinct subsequences of s which equals t.
# The test cases are generated so that the answer fits on a 32-bit signed integer.

# Example 1:
# Input: s = "rabbbit", t = "rabbit"
# Output: 3

# Example 2:
# Input: s = "babgbag", t = "bag"
# Output: 5

# Constraints:  s and t consist of English letters.

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def dfs(i , j) :
            if j >= len(t) :
                return 1
            if i >= len(s) :
                return 0
            if (i , j) in dp :
                return dp[(i , j)]
            if s[i] == t[j] :
                dp[(i , j)] = dfs(i+1 , j+1) + dfs(i+1 , j)
                return dp[(i , j)]
            else :
                dp[(i , j)] = dfs(i+1 , j)
                return dp[(i , j)]
        return dfs(0 , 0)
'''
s="xaa" , t="a"
   i         j
    i        j
     i         j ->1 (use "_a_")
     
     i       j
      i        j ->1 (use "__a")

s = "rabbbit", t = "rabbit"
     rabb it
     rab bit
     ra bbit
     
s = "babgbag", t = "bag"
     ba g
     ba    g
     b    ag
       b  ag
         bag
'''

# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s) + 1)]
#         for row in range(len(s) + 1) :
#             dp[row][0] = 1
#         for row in range(1 , len(s) + 1) :
#             for col in range(1 , len(t) + 1) :
#                 dp[row][col] += dp[row-1][col]
#                 if s[row-1] == t[col-1] :
#                     dp[row][col] += dp[row-1][col-1]
#         return dp[row][col]
'''
       r a b b i t   t
     0 1 2 3 4 5 6
  0  1 0 0 0 0 0 0 
r 1  1 1 0 0 0 0 0 
a 2  1 1 1 0 0 0 0 
b 3  1 1 1 1 0 0 0 
b 4  1 1 1 2 1 0 0
b 5  1 1 1 3 3 0 0
i 6  1 1 1 3 3 3 0
t 7  1 1 1 3 3 3 3

s
'''
