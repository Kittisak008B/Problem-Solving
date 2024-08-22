# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2. Given an integer num, return its complement.

# Example 1:
# Input: num = 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

# Example 2:
# Input: num = 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 
# Constraints: 1 <= num < 2**31

class Solution:
    def findComplement(self, num: int) -> int:
        ones = 0
        copy = num
        while copy :
            ones <<= 1
            ones += 1
            copy >>= 1
        return ones ^ num
'''
101
111 xor 101 = 010


copy = num = 101  
ones = 00 -> 01 copy = 10
ones = 010 -> 011 copy = 1
ones = 0110 -> 0111 copy = 0
0111 xor 101 = 0010
'''
