# Given a string s, return the longest palindromicsubstring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
  
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
 
# Constraints:  s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome_from_mid(s ,left ,right) :
            while left >= 0 and right < len(s) and s[left] == s[right] :
                left -= 1
                right += 1
            return s[left+1 : right]
        ans = ''
        for i in range(len(s)) :
            odd_sub = palindrome_from_mid(s ,i ,i)
            if len(odd_sub) > len(ans) :
                ans = odd_sub
            even_sub = palindrome_from_mid(s ,i ,i+1)
            if len(even_sub) > len(ans) :
                ans = even_sub
        return ans
      
