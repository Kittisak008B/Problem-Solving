# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. 
# You may return the answer in any order.
# The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 10**4.

# Example 1:
# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2

# Example 2:
# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
 
# Constraints:
# 1 <= expression.length <= 20
# expression consists of digits and the operator '+', '-', and '*'.
# All the integer values in the input expression are in the range [0, 99].
# The integer values in the input expression do not have a leading '-' or '+' denoting the sign.

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        dp = {}
        def dfs(expr) :
            if expr in dp :
                return dp[expr]
            res = []
            for i, char in enumerate(expr) :
                if char in "+-*" :
                    left = dfs(expr[:i])
                    right = dfs(expr[i+1:])
                    for l in left :
                        for r in right :
                            if char == '+' :
                                res.append(l + r)
                            elif char == '-' :
                                res.append(l - r)
                            else:
                                res.append(l * r)
            if not res :
                res.append(int(expr))
            dp[expr] = res
            #print(dp)
            return dp[expr]
        return dfs(expression)
'''                             
               ______ 2*3-4*5______
              /          |         \     
           2*(3-4*5) (2*3)-(4*5)  (2*3-4)*5       
       left c right       c           /\ c
               /  \      -14         /  \
          3-(4*5) (3-4)*5        2*(3-4) (2*3)-4 
           c           c          c           c
      this path       -10        -10          10
2*(3-(4*5))= -34
'''
