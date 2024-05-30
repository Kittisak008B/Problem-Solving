# Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy. Return true if n is a happy number, and false if not.

# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Example 2:
# Input: n = 2
# Output: false

class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n) :
            value = 0
            while n > 0 :
                digits = n % 10 
                value += digits**2
                n //= 10
            return value
        seen = set()
        while n != 1 :
            n = helper(n)
            if n in seen :
                return False
            seen.add(n)
        return True
'''
n=19
seen={82 68 100 1} -> True
-------
n=2
seen={4 16 37 58 89 145 42 20 4} -> 4 already in seen -> has loop (can't be 1) -> False
'''
