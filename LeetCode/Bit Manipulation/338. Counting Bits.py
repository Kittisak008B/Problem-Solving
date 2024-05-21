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
        dp = [0]*(n+1)
        dp[0] = 0
        offset = 1
        for i in range(1 , n+1) :
            if offset*2 == i :
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
'''
n       binary   num_of_1
0	 0000     0
1	 0001     1    1+dp[n-1]
2	 0010     1    1+dp[n-2]
3	 0011     2    1+dp[n-2]
4	 0100     1    1+dp[n-4]
5	 0101     2    1+dp[n-4]
6        0110     2    1+dp[n-4]
7	 0111     3    1+dp[n-4]
8	 1000     1    1+dp[n-8]
9	 1001     2
'''
