# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
  
# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
  
# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.         Constraints: text1 and text2 consist of only lowercase English characters.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]
'''
   a c e
a  3 2 1 0 -> (abcde,e)=1 (abcde,ce)=2 (abcde,ace)=3 end -> return 3 
b  2 2 1 0 -> (bcde,e)=1 (bcde,ce)=2 (bcde,ace)=2
c  2 2 1 0 -> (cde,e)=1 (cde,ce)=2 (cde,ace)=2
d  1 1 1 0 -> (de,e)=1 (de,ce)=1 (de,ace)=1
e  1 1 1 0 -> start (e,e)=1 (e,ce)=1 (e,ace)=1
   0 0 0 0 
'''
