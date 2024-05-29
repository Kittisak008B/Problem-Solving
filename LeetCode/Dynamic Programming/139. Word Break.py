# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 
# Constraints:  s and wordDict[i] consist of only lowercase English letters.   All the strings of wordDict are unique.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)+1) :
            for j in range(i) :
                if dp[j] == True and s[j:i] in wordDict :
                    dp[i] = True
                    break
        return dp[-1]
'''
s    l e e t c o d e   wordDict = ["leet","code"]
dp T F F F T F F F T  
                   i
           j
'''
