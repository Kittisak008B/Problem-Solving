# Given two integers a and b, return the sum of the two integers without using the operators + and -.
# Example 1:
# Input: a = 1, b = 2
# Output: 3

# Example 2:
# Input: a = 2, b = 3
# Output: 5
 
# Constraints:  -1000 <= a, b <= 1000
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # print(getsizeof(0)*8) #python use a lot of bits ?
        mask = 0xffffffff
        # print('Bytes:', getsizeof(mask) ,'Bits:', getsizeof(mask)*8)
        while (b & mask) > 0 :
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry
        return (a & mask) if b != 0 else a
'''
a=2 , b=3 -> ans=5
10     11

while b != 0 
carry = 100
a = 10^11=01
b = 100

carry = 01&100 = 0
a = 01^100 = 101
b = 0 --> return a = 101 = 5 
'''
