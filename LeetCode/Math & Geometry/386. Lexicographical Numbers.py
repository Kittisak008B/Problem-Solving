# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

# Example 1:
# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

# Example 2:
# Input: n = 2
# Output: [1,2]

# Constraints:
# 1 <= n <= 5 * 10**4

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        cur_num = 1
        while len(res) < n :
            res.append(cur_num)
            if cur_num * 10 <= n :
                cur_num *= 10
            elif (cur_num + 1 <= n) and (cur_num % 10 != 9) :
                cur_num += 1
            else :
                while (cur_num + 1 > n) or (cur_num % 10 == 9) :
                    cur_num //= 10
                cur_num += 1
        return res
