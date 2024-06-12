# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward. A substring is a contiguous sequence of characters within the string.

# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 
# Constraints: s consists of lowercase English letters.

class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_palindrome_from_mid(left, right) :
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right] :
                left -= 1
                right += 1
                count += 1
            return count
        ans = 0 
        for i in range(len(s)) :
            odd = count_palindrome_from_mid(i,i)     #ex. a  aaa
            even = count_palindrome_from_mid(i,i+1)  #ex. aa  aaaa
            ans += odd + even
        return ans
