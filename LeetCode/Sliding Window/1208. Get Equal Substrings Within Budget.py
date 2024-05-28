# You are given two strings s and t of the same length and an integer maxCost.
# You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| 
# (i.e., the absolute difference between the ASCII values of the characters).

# Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. 
# If there is no substring from s that can be changed to its corresponding substring from t, return 0.

# Example 1:
# Input: s = "abcd", t = "bcdf", maxCost = 3
# Output: 3
# Explanation: "abc" of s can change to "bcd".
# That costs 3, so the maximum length is 3.

# Example 2:
# Input: s = "abcd", t = "cdef", maxCost = 3
# Output: 1
# Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:  
        max_length = 0
        cur_cost = 0
        left_pointer = 0
        for right_pointer in range(len(s)) :
            cur_cost += abs( ord(s[right_pointer]) - ord(t[right_pointer]) )
            while cur_cost > maxCost :
                cur_cost -= abs( ord(s[left_pointer]) - ord(t[left_pointer]) )
                left_pointer += 1
            max_length = max(max_length , right_pointer - left_pointer + 1)
        return max_length
