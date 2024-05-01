# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        cur = []
        def backtrack(open_p , close_p) :
            if open_p == close_p == n :
                ans.append(''.join(cur))
                return 
            if open_p < n :
                cur.append('(')
                backtrack(open_p +1 , close_p)
                cur.pop()
            if close_p < open_p :
                cur.append(')')
                backtrack(open_p , close_p +1)
                cur.pop()
        backtrack(0 , 0)
        return ans
#                                    [   ]
#                                    ['(']
#              ['((']                               ['()']
#     ['(((']          ['(()']                      ['()('] 
#    ['((()']     ['(()(']   ['(())']          ['()(('] ['()()'] 
#   ['((())']    ['(()()']   ['(())(']         ['()(()'] ['()()('] 
#  ['((()))']   ['(()())']   ['(())()']        ['()(())'] ['()()()'] 
