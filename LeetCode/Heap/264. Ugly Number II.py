# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5. Given an integer n, return the nth ugly number.

# Example 1:
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
  
# Example 2:
# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 
# Constraints:
# 1 <= n <= 1690

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = set()
        visited.add(1)
        factors = [2,3,5]
        for _ in range(n) :
            number = heapq.heappop(heap) 
            for f in factors :
                if number*f not in visited :
                    visited.add(number*f)
                    heapq.heappush(heap , number*f)
        return number
