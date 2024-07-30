# You are given a string s consisting only of characters 'a' and 'b'​​​​.
# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
# Return the minimum number of deletions needed to make s balanced.

# Example 1:
# Input: s = "aababbab"
# Output: 2
# Explanation: You can either:
# Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
# Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").\

# Example 2:
# Input: s = "bbaaaaabb"
# Output: 2
# Explanation: The only solution is to delete the first two characters.
 
# Constraints:
# 1 <= s.length <= 10**5
# s[i] is 'a' or 'b'​​.

class Solution:
    def minimumDeletions(self, s: str) -> int:
        right_a = 0  
        left_b = 0
        for i in range(len(s)) :
            if s[i] == 'b' :
                left_b += 1
        ans = min(left_b , len(s)-left_b)
        for i in range(len(s)-1 , -1 , -1) :
            if s[i] == 'b' :
                left_b -= 1
            if s[i] == 'a' :
                right_a += 1
            ans = min(ans , left_b + right_a) #delete right_a and left_b
        return ans
'''
"aababbab"   left_b =4   right_a =0  ans =4
        i            3            0       3
       i             3            1       3
      i              2            1       3
     i               1            1       2
    i                1            2       2
   i                 0            2       2
  i
 i
'''
