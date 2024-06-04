# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
  
# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 
# Constraints:  s consists of lowercase and/or uppercase English letters only.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        unpair_set = set()
        ans = 0
        for char in s :
            if char in unpair_set :
                ans += 2
                unpair_set.remove(char)
            else :
                unpair_set.add(char)
        if len(unpair_set) > 0 : # add one char to middle of palindrome
            ans += 1
        return ans
