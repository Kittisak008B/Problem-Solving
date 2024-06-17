# Given a non-negative integer c, decide whether there're two integers a and b such that a**2 + b**2 = c.

# Example 1:
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5

# Example 2:
# Input: c = 3
# Output: false
 
# Constraints:  0 <= c <= 2**31 - 1

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0 
        b = int(sqrt(c))  
        while a <= b :
            sum_of_square = a**2 + b**2
            if sum_of_square < c :
                a += 1
            elif sum_of_square > c :
                b -= 1
            else :
                return True
        return False
