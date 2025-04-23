# You are given an integer n. Each number from 1 to n is grouped according to the sum of its digits.
# Return the number of groups that have the largest size.

# Example 1:
# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.
  
# Example 2:
# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.
 
# Constraints: 1 <= n <= 10**4

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(x) :
            return sum(int(d) for d in str(x))
        g = defaultdict(int)
        for i in range(1 , n + 1) :
            g[digit_sum(i)] += 1
        max_size = max(g.values())
        res = sum(1 for count in g.values() if count == max_size)
        return res
'''
n = 13
digit sum 1 → [1, 10] → 2 numbers  
digit sum 2 → [2, 11] → 2 numbers  
digit sum 3 → [3, 12] → 2 numbers  
digit sum 4 → [4, 13] → 2 numbers  
digit sum 5 → [5]     → 1 number  
... digit sum 9 → [9] → 1 number     groups with largest size = 4
'''
