# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n+1) :
            ans.append(ans[i//2] + i%2)
        return ans
# 0	 0000  0
# 1	 0001  1
# 2	 0010  1
# 3	 0011  2
# 4	 0100  1
# 5	 0101  2
# 6  0110  2
# 7	 0111  3
# 8	 1000  1
# 9	 1001  2
# 10 1010  2
# 11 1011  3
# 12 1100  2
# 13 1101  3
# 14 1110  3
# 15 1111  4
