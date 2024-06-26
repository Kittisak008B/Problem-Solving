# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_s1 = [0] *26
        counts_s2 = [0] *26
        if len(s1) > len(s2) :
            return False
        for i in range(len(s1)) :
            counts_s1[ord(s1[i]) - ord("a")] += 1
            counts_s2[ord(s2[i]) - ord("a")] += 1
        if counts_s1 == counts_s2 :
                return True
        for i in range(len(s1) , len(s2)) :
            counts_s2[ord(s2[i]) - ord("a")] += 1
            counts_s2[ord(s2[i - len(s1)]) - ord("a")] -= 1
            if counts_s1 == counts_s2 :
                return True
        return False

  
