# You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. 
# Each minute, you may take either the leftmost character of s, or the rightmost character of s.
# Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

# Example 1:
# Input: s = "aabaaaacaabc", k = 2
# Output: 8
# Explanation: 
# Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
# Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
# A total of 3 + 5 = 8 minutes is needed. It can be proven that 8 is the minimum number of minutes needed.

# Example 2:
# Input: s = "a", k = 1
# Output: -1
# Explanation: It is not possible to take one 'b' or 'c' so return -1.

# Constraints:
# 1 <= s.length <= 10**5
# s consists of only the letters 'a', 'b', and 'c'.
# 0 <= k <= s.length

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        for c in s :
            freq[c] += 1
        if freq['a'] < k or freq['b'] < k or freq['c'] < k :
            return -1
        #print(freq)
        res = len(s)
        left = 0
        for right in range(len(s)) :
            freq[s[right]] -= 1       
            while freq[s[right]] < k :
                freq[s[left]] += 1     
                left += 1
            res = min(res, len(s) - (right-left+1))
        return res
'''
Input: s = "aabaaaacaabc", k = 2
Output: 8                  freq={'a': 8, 'b': 2, 'c': 2}
            xxx    xxxxx     
                  r
               l      at left=3 right=6  freq={'a': 4, 'b': 2, 'c': 2} 
                    
'''
