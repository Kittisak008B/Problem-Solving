# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 
# Constraints:  ransomNote and magazine consist of lowercase English letters.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mgz_dict = defaultdict(int)
        for char in magazine :
            if char not in mgz_dict :
                mgz_dict[char] = 0
            mgz_dict[char] += 1
        for char in ransomNote :
            if char not in mgz_dict or mgz_dict[char] <= 0 :
                return False
            mgz_dict[char] -= 1
        return True
