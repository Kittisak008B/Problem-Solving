# There is a strange printer with the following two special properties:
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
# Given a string s, return the minimum number of turns the printer needed to print it.

# Example 1:
# Input: s = "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".

# Example 2:
# Input: s = "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
 
# Constraints:
# 1 <= s.length <= 100
# s consists of lowercase English letters.

class Solution:
    def strangePrinter(self, s: str) -> int:
        dp = {}
        def dfs(i, j) :
            if i > j :
                return 0
            if i == j :
                return 1
            if (i, j) in dp :
                return dp[(i, j)]
            res = 1 + dfs(i + 1 , j)
            for k in range(i + 1 , j + 1) : # explore for s[i:k] and s[k+1:j+1]
                if s[k] == s[i] :
                    res = min(res , dfs(i , k - 1) + dfs(k + 1 , j))
            dp[(i, j)] = res
            return dp[(i, j)]
        return dfs(0 , len(s) - 1)
'''
aabbaa    -> aaaaaa -> aabbaa -> 2     k -> print everything before and after k section 
i    j -> 1 + abbaa -> 1+1 + bbaa ->not minimun
 k     -> a + bbaa -> 1+2 =3
    k  -> aabb +  a -> 2+1 =3
     k -> aabba
          i   j
           k    -> a + bba -> 1+2=3
              k -> aabb
                   i  j
                    k  -> a + bb -> 1 + 1 = 2 #minimun

aaaaaa
i    j
 k     -> a + aaaa
  k    -> aa + aaa
   k   -> aaa + aa
    k  -> aaaa + a
     k -> aaaaa
          i   j
              k -> aaaa
                      k -> aaa
                             k -> aa
                                   k -> a -> 1
'''
