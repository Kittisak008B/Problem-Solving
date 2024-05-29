# Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
# If the current number is even, you have to divide it by 2.
# If the current number is odd, you have to add 1 to it.
# It is guaranteed that you can always reach one for all test cases.

# Example 1:
# Input: s = "1101"
# Output: 6
# Explanation: "1101" corressponds to number 13 in their decimal representation.
# Step 1) 13 is odd, add 1 and obtain 14. 
# Step 2) 14 is even, divide by 2 and obtain 7.
# Step 3) 7 is odd, add 1 and obtain 8.
# Step 4) 8 is even, divide by 2 and obtain 4.  
# Step 5) 4 is even, divide by 2 and obtain 2. 
# Step 6) 2 is even, divide by 2 and obtain 1.  

# Example 2:
# Input: s = "10"
# Output: 1
# Explanation: "10" corressponds to number 2 in their decimal representation.
# Step 1) 2 is even, divide by 2 and obtain 1.  

class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        for i in range(len(s)-1 , 0 , -1) :
            digit = (int(s[i]) + carry ) % 2
            if digit == 0 :
                steps += 1
            elif digit == 1 :
                carry = 1
                steps += 2
        return steps + carry
'''
1101
   i digit = 1 -> carry = 1 steps = 2 (add1 & divide by 2)
  i  digit = 1 -> carry = 1 steps += 2 = 4
 i   digit = 0 -> carry = 1 steps += 1 = 5  
return steps + carry = 5 + 1 = 6
'''
