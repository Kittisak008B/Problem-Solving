# You are given a 0-indexed string s and a dictionary of words dictionary. 
# You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. 
# There may be some extra characters in s which are not present in any of the substrings.
# Return the minimum number of extra characters left over if you break up s optimally.

# Example 1:
# Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. 
# There is only 1 unused character (at index 4), so we return 1.

# Example 2:
# Input: s = "sayhelloworld", dictionary = ["hello","world"]
# Output: 3
# Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. 
# The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
 
# Constraints:
# 1 <= s.length <= 50
# 1 <= dictionary.length <= 50
# 1 <= dictionary[i].length <= 50
# dictionary[i] and s consists of only lowercase English letters , dictionary contains distinct words

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = {}
        word_set = set(dictionary)
        def dfs(i) :
            if i == len(s) :
                return 0
            if i in dp :
                return dp[i]
            res = 1 + dfs(i + 1) #skip a character
            for j in range(i , len(s)) :
                if s[i:j+1] in word_set :
                    res = min(res , dfs(j+1))
            dp[i] = res
            return dp[i]
        return dfs(0)
'''
s = "leetscode", dictionary = ["leet","code","leetcode"]

         dfs(0)  
       /        \
                Try s[0:4]="leet" (valid)
                         |
                      dfs(4)
                    Skip "s" (1 extra character) res=1+dfs(5)
                          |
                         dfs(5)
                    Try s[5:9]="code" (valid)
                           |
                          dfs(9) -> Return 0 (End of string)     
'''
