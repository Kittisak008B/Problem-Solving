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
