# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character  ,  Delete a character  ,  Replace a character
 
# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# Example 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
 
# Constraints:  word1 and word2 consist of lowercase English letters.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        for col in range(len(word1) + 1) :
            dp[0][col] = col
        for row in range(len(word2) + 1) :
            dp[row][0] = row
        for row in range(1 , len(word2) + 1) :
            for col in range(1 , len(word1) + 1) :
                if word1[col - 1] == word2[row - 1] :
                    dp[row][col] = dp[row-1][col-1]
                else :
                    dp[row][col] = 1 + min(dp[row-1][col-1] , dp[row-1][col] , dp[row][col-1]) 
        return dp[row][col]

'''
    ''  h  o  r  s  e   word1
''  0   1  2  3  4  5 
r   1   1  2  2  3  4
o   2   2  1  2  3  4
s   3   3  2  2  2  3 --> ans 3
word2
'''
