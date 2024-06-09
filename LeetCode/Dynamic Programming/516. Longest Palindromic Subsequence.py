# Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

# Example 1:
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".

# Example 2:
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
 
# Constraints:  s consists only of lowercase English letters.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)) :
            dp[i][i] = 1
        for length in range(2 , len(s) + 1) :
            for i in range(len(s)+1 - length) :
                j = i + length - 1
                if s[i] == s[j] :
                    dp[i][j] = 2 + dp[i+1][j-1]
                else :
                    dp[i][j] = max(dp[i][j-1] , dp[i+1][j])
        return dp[0][-1]
'''
'bbbab'
   0  1  2  3  4  j
0  1  2  3  3  4
1     1  2  2  3
2        1  1  3
3           1  1
4              1
i

length = 1  Longest Palindromic Subsequence = 1
---
length = 2
'b b b a b'
 0 1 2 3 4 idx
 i j             'bb' = 2 +dp[1][0] = 2+0 = 2
   i j           'bb' = 2 +dp[2][1] = 2+0 = 2
     i j         'ba' = max btw 'b' & 'a' = 1
       i j       'ab' = max btw 'a' & 'b' = 1
---
length = 3
'b b b a b'
 0 1 2 3 4 idx
 i   j           'bbb' : b==b -> 2 + dp[1][1] = 2+1 = 3
   i   j         'bba' : b!=a -> max(dp[1][2] , dp[2][3]) = max btw 'bb' & 'ba' = 2
     i   j       'bab' : b==b -> 2 + dp[3][3] = 2+1 = 3
---
length = 4
'b b b a b'
 0 1 2 3 4 idx
 i     j         'bbba' : b!=a -> max(dp[0][2] , dp[1][3]) = max btw 'bbb' & 'bba' = 3
   i     j       'bbab' : b==b -> 2 + dp[2][3] = 2+1 = 3
---
length = 5
'b b b a b'
 0 1 2 3 4 idx
 i       j       'bbbab' : b==b -> 2 + dp[1][3] = 2+2 = 4
'''
