# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.

# Example 3:
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 
# Constraints:   s contains only lowercase English letters.   p contains only lowercase English letters, '?' or '*'.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        for col in range(1 , len(p) + 1) :  
            if p[col - 1] == '*' :
                dp[0][col] = dp[0][col - 1]
        for row in range(1 , len(s) + 1) :
            for col in range(1 , len(p) + 1) :
                if s[row - 1] == p[col - 1] or p[col - 1] == '?' :
                    dp[row][col] = dp[row - 1][col - 1]
                elif p[col - 1] == '*' :
                    dp[row][col] = dp[row - 1][col] or dp[row][col - 1]
                else :
                    dp[row][col] = False
        return dp[-1][-1]
'''
    0  1  2  3
       *  *  *  pattern
0   T  T  T  T
1 a F  T  T  T
2 a F  T  T  T
string

     0  1  2  3  4  5    
        a  ?  b  *  e  pattern
0    T  F  F  F  F  F 
1 a  F  T  F  F  F  F
2 c  F  F  T  F  F  F
3 b  F  F  F  T  T  F
4 a  F  F  F  F  T  F
5 c  F  F  F  F  T  F
6 e  F  F  F  F  T  T
string

if == ? : dp[i][j] = dp[i-1][j-1]
   *    : dp[i][j] = dp[i][j-1] or dp[i-1][j]
   !=   : F
'''
