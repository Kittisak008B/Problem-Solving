# A message containing letters from A-Z can be encoded into numbers using the following mapping:
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above
# (there may be multiple ways). For example, "11106" can be mapped into:
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.
# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

# Example 2:
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Example 3:
# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 
# Constraints:  s contains only digits and may contain leading zero(s).

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0' :
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2 , len(s) + 1) :
            if s[i-1] == '0' :
                if s[i-2] == '1' or s[i-2] == '2' :
                    dp[i] = dp[i-2]
                else :
                    return 0
            else :
                if s[i-2] == '1' or (s[i-2] == '2' and int(s[i-1]) <= 6) :
                    dp[i] = dp[i-2] + dp[i-1]
                else :
                    dp[i] = dp[i-1]
        return dp[-1]
'''
code  1 0 1 2
dp  1 1 1 1 2 

code '1'   : 1
     '10'  : 10
     '101' : 10 , 1
     '1012': 10 , 1 , 2
             10 , 12
-----------------------
code   1 2 7 2 1
dp   1 1 2 2 2 4

code '1'    : 1
     '12'   : 1,2
              12  
     '127'  : 1,2,7 
              12,7
     '1272' : 1,2,7,2 
              12,7,2
     '12721': 1 , 2 , 7 , 2 , 1
              1 , 2 , 7 , 2 , 1
              12, 7 , 2 , 1
              1 , 2 , 7 , 21
              12, 7 , 21
'''
