# Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.
# The closest is defined as the absolute difference minimized between two integers.

# Example 1:
# Input: n = "123"
# Output: "121"

# Example 2:
# Input: n = "1"
# Output: "0"    Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 
# Constraints:
# 1 <= n.length <= 18
# n consists of only digits.
# n does not have leading zeros.
# n is representing an integer in the range [1, 10**18 - 1].

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def half_mirroring_to_palindrome(half , even) :
            res = half
            if not even :
                half //= 10 
            while half > 0 :
                res = res * 10 + half % 10
                half //= 10
            return res   
        if int(n) < 10 :
            if int(n) == 0 :
                return '1'
            else:
                return str(int(n) - 1)
        k = len(n)//2 if len(n) % 2 == 1 else len(n)//2 - 1
        first_half = int(n[: k + 1])
        candidates = []
        candidates.append(half_mirroring_to_palindrome(first_half , len(n)%2 == 0))
        candidates.append(half_mirroring_to_palindrome(first_half + 1 , len(n)%2 == 0))
        candidates.append(half_mirroring_to_palindrome(first_half - 1 , len(n)%2 == 0))
        candidates.append(10**(len(n)- 1) - 1)
        candidates.append(10**len(n) + 1)
        diff = float('inf')
        res = 0
        for cand in candidates :
            if cand != int(n) : # not including itself
                cur_diff = abs(cand - int(n))
                if cur_diff < diff :
                    diff = cur_diff
                    res = cand
                elif cur_diff == diff :
                    res = min(res , cand)
        return str(res)
'''
candidates
- go down N/2 digits add 1 or subtract 1 or do nothing then mirroring the first half
- go down 1 digits and make them all 999.. or go up 1 digits 10...01

12345 -> 123 -> 12321
         123 + 1 -> 12421
         123 - 1 -> 12221
         9999
         100001

123 -> 12 -> 121
       12 - 1 -> 11 -> 111
       12 + 1 -> 13 -> 131
       99
       1001
            
11 -> 1 -> 11 x -> not including itself
      0 -> 0
      2 -> 22
      9
      101
'''
