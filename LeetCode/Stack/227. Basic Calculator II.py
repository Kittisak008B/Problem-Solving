# Given a string s which represents an expression, evaluate this expression and return its value. 
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:
# Input: s = "3+2*2"
# Output: 7

# Example 2:
# Input: s = " 3/2 "
# Output: 1

# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        pre_op = '+'
        num = 0
        for i in range(len(s)) :
            c = s[i]
            if c.isdigit() :
                num = num*10 + int(c)
            if c in {"+", "-", "*", "/"} or i == len(s)-1 :
                if pre_op == '+' :
                    stack.append(num)
                elif pre_op == '-' :
                    stack.append(-num)
                elif pre_op == '*' :
                    stack[-1] *= num
                elif pre_op == '/' :
                    stack[-1] = int(stack[-1] / num)
                num = 0
                pre_op = c
        ans = 0
        for x in stack :
            ans += x 
        return ans
      
