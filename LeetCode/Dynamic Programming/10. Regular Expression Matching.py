# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
 
# Constraints:  s contains only lowercase English letters.  p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(1 , len(p) + 1) :
            if p[j - 1] == '*' :
                dp[0][j] = dp[0][j - 2]
        for i in range(1 , len(s) + 1) :
            for j in range(1 , len(p) + 1) :
                if s[i - 1] == p[j - 1] or p[j - 1] == '.' :
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*' :
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or s[i - 1] == p[j - 2] :
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                else :
                    dp[i][j] = False
        print(dp)
        return dp[-1][-1]
'''
p='ab*.c'   s='abbac'

     0  1  2  3  4  5
        a  b  *  .  c   pattern     #guaranteed '*', there will be a previous valid character to match.
0    T  F  F  F  F  F    
1 a  F  T  F  T  F  F 
2 b  F  F  T  T  T  F
3 b  F  F  F  T  T  F
4 a  F  F  F  F  T  F
5 c  F  F  F  F  F  T
string

if ==  . : dp[i][j] = dp[i-1][j-1]
   *     : dp[i][j] = dp[i][j-2](ex. ab*, a -> b* to '' -> a , a) 
           or dp[i][j] = dp[i-1][j] if s[i-1] == p[j-2] or p[j-2] =='.'(ex. ab* , ab -> s[i-1]=b , p[j-2]=b -> ab , ab)
   !=    : False

    0 1 2
      a *  
0   T F T 
1 a F T T
2 a F F T

    0 1 2 3 4 5 6 7 8
      a b * a * c * a
0   T F F F F F F F F
1 a F T F T F T F T F
2 a F F F F T T F T T
3 a F F F F F T F T T
'''
