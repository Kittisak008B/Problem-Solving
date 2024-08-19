# There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:
# Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

# Example 1:
# Input: n = 3
# Output: 3
# Explanation: Initially, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
  
# Example 2:
# Input: n = 1
# Output: 0
 
# Constraints:
# 1 <= n <= 1000

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1 :
            return 0
        dp = {}
        def dfs(cur_length , paste_length) : #return min steps 
            if cur_length == n :
                return 0
            if cur_length > n :
                return float('inf')
            if (cur_length , paste_length) in dp :
                return dp[(cur_length , paste_length)]
            copy_and_paste = 2 + dfs(cur_length * 2 , cur_length)
            paste_only = 1 + dfs(cur_length + paste_length , paste_length)
            dp[(cur_length , paste_length)] = min(copy_and_paste , paste_only)
            return dp[(cur_length , paste_length)]
        return 1 + dfs(1,1)
'''
n=3  
                A  steps=1          
              (1,1) -> (cur_length , paste_length)
        paste/    \copy+paste steps+=2 -> steps=3
            AA     AA          
  steps=2 (2,1)     (2,1) 
     paste/  \copy+paste
         AAA  AAAA 
steps=3 (3,1) (4,2) steps=4
'''
