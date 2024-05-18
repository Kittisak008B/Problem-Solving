# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false
 
# Constraints:
# 1 <= s.length, t.length <= 5 * 10**4
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        hm_s = {}
        hm_t = {}
        for x in s :
            if x not in hm_s :
                hm_s[x] = 0
            hm_s[x] += 1
        for y in t :
            if y not in hm_t :
                hm_t[y] = 0
            hm_t[y] += 1
        for key in hm_s :
            if key not in hm_t or hm_s[key] != hm_t[key] :
                return False
        return True
     
     
        
