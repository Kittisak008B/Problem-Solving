# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# Constraints:
# 1 <= s.length <= 3 * 10**5
# s consist of printable ASCII characters.

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = 'aeiouAEIOU'
        l = 0
        r = len(s) - 1
        while l < r :
            if s[l] in vowels and s[r] in vowels :
                s[l] , s[r] = s[r] , s[l]
                l += 1
                r -= 1
            elif s[l] not in vowels :
                l += 1
            elif s[r] not in vowels :
                r -= 1
        return ''.join(s)
      
