# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

# Example 1:
# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.
  
# Example 2:
# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".

# Example 3:
# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def check_palindrome(w) :
            i = 0
            j = len(w) -1
            while i < j :
                if w[i] != w[j] :
                    return False
                i += 1
                j -= 1
            return True
        for w in words :
            if check_palindrome(w) :
                return w
        return ''
