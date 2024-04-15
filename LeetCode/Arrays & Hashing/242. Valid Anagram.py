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
        for i in range(len(s)) :
            hm_s[s[i]] = 1 + hm_s.get(s[i] , 0)
            hm_t[t[i]] = 1 + hm_t.get(t[i] , 0)
        for key in hm_s :
            if hm_s[key] != hm_t.get(key , 0) :
                return False
        return True

        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # return sorted_s == sorted_t

        # if len(s) != len(t):
        #     return False
        # counter = {}
        # for char in s:
        #     counter[char] = counter.get(char, 0) + 1
        # for char in t:
        #     if char not in counter or counter[char] == 0:
        #         return False
        #     counter[char] -= 1
        # return True
