# Given two positive integers left and right, find the two integers num1 and num2 such that:
# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, 
# return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

# Example 1:
# Input: left = 10, right = 19
# Output: [11,13]
# Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
# The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19]. Since 11 is smaller than 17, we return the first pair.

# Example 2:
# Input: left = 4, right = 6
# Output: [-1,-1]
# Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.

# Constraints:
# 1 <= left <= right <= 10**6

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(n) :
            if n < 2 :
                return False
            if n in (2, 3, 5, 7) :
                return True
            if n % 2 == 0 or n % 3 == 0 : # Eliminate even numbers and multiples of 3
                return False  
            i = 5
            while n >= i * i :
                if n % i == 0 or n % (i + 2) == 0 :
                    return False
                i += 6  # Increment by 6 to skip unnecessary checks
            return True
        prime = []
        for i in range(left , right + 1) :
            if is_prime(i) :
                prime.append(i)
        if len(prime) < 2 :
            return [-1 , -1]
        min_gap = float('inf')
        res = [0 , 0]
        for i in range(len(prime) - 1) :
            if prime[i + 1] - prime[i] < min_gap :
                res[0] = prime[i]
                res[1] = prime[i + 1]
                min_gap = prime[i + 1] - prime[i]
        return res  #Time Complexity : O((right−left)∗√right) 
