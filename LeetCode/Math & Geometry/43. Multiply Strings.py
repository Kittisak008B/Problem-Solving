# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
 
# Constraints:
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0 for _ in range(len(num1) + len(num2))]
        for i in range(len(num1)-1 ,-1,-1) :
            for j in range(len(num2)-1 ,-1,-1) :
                temp = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0')) + res[i+j+1]
                res[i+j+1] = temp%10
                res[i+j] += temp//10
        for i in range(len(res)) :
            if res[i] != 0 :
                return ''.join(map(str , res[i:]))
        return '0'   
'''
       4 5 6
       1 2 3
       
[0,5,6,0,8,8]
'''
