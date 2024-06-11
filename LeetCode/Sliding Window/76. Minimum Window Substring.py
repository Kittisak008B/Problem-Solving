# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "". The testcases will be generated such that the answer is unique.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
  
# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 
# Constraints:  s and t consist of uppercase and lowercase English letters.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for char in t :
            d[char] += 1
        cur_formed = 0
        total_need = len(d)
        min_length = float('inf')
        start,end = 0 , 0
        r,l = 0 , 0
        while r < len(s) :
            char = s[r]
            if char in d :
                d[char] -= 1
                if d[char] == 0 :
                    cur_formed += 1
            while l <= r and cur_formed == total_need :
                cur_length = r - l + 1
                if cur_length < min_length :
                    min_length = cur_length
                    start = l
                    end = r + 1
                char = s[l]
                if char in d :
                    if d[char] == 0 :
                        cur_formed -= 1
                    d[char] += 1
                l += 1
            r += 1
        return s[start:end] if min_length != float('inf') else ''
      
