# You are given a string s. You can convert s to a palindrome by adding characters in front of it.
# Return the shortest palindrome you can find by performing this transformation.

# Example 1:
# Input: s = "aacecaaa"
# Output: "aaacecaaa"

# Example 2:
# Input: s = "abcd"
# Output: "dcbabcd"
 
# Constraints:
# 0 <= s.length <= 5 * 10**4
# s consists of lowercase English letters only.

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # def reverse_string(word) :
        #     s = [char for char in word]
        #     i = 0
        #     j = len(s) - 1
        #     while i < j :
        #         s[i] , s[j] = s[j] , s[i]
        #         i += 1
        #         j -= 1
        #     return ''.join(s)
        # def check_palin(s,left,right) :
        #     while left <= right :
        #         if s[left] != s[right] :
        #             return False
        #         left += 1
        #         right -= 1
        #     return True
        # if not s :
        #     return ''
        # left = 0
        # for right in range(len(s)-1 , -1 , -1) :
        #     if check_palin(s,left,right) :
        #         to_copy = s[right+1:]
        #         return reverse_string(to_copy) + s
        
        reversed_string = s[::-1]  
        for i in range(len(s)) : # Iterate through the string to find the longest palindromic prefix
            if s[: len(s) - i] == reversed_string[i:] :
                return reversed_string[:i] + s
        return ''
