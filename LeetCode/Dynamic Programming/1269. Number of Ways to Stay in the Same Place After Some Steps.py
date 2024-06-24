# You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 
# 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).
# Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0 after exactly steps steps. 
# Since the answer may be too large, return it modulo 10**9 + 7.

# Example 1:
# Input: steps = 3, arrLen = 2
# Output: 4
# Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
# Right, Left, Stay
# Stay, Right, Left
# Right, Stay, Left
# Stay, Stay, Stay
  
# Example 2:
# Input: steps = 2, arrLen = 4
# Output: 2
# Explanation: There are 2 differents ways to stay at index 0 after 2 steps
# Right, Left
# Stay, Stay

# Example 3:
# Input: steps = 4, arrLen = 2
# Output: 8

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = {}
        def dfs(place , steps) :
            if place < 0 or place >= arrLen :
                return 0
            if steps == 0 :
                return place == 0
            if (place , steps) in dp :
                return dp[(place , steps)]
            ans = dfs(place+1 , steps-1) + dfs(place , steps-1) + dfs(place-1 , steps-1)
            dp[(place , steps)] = ans 
            return dp[(place , steps)]
        return dfs(0 , steps)%(10**9 +7)
''' 
steps = 3 arrLen = 2
        arr -> _ _   
              place

              (place , steps)
        _________ (0 , 3)_________________________________
      r/                              s|                 l\
   (1,2)______                     ___(0,2)_____________    x ->cant go left 
  r/   s|     l\                 r/          s|        l\ 
  x (1,1)__    (0,1)_______     (1,1)__      (0,1)______  x 
   r/  s| l\       r/ s|  l\    r/ s| l\       r/  s|  l\
   x (1,0) (0,0) (1,0)(0,0) x (2,0)(1,0)(0,0) (1,0) (0,0) x
       x     ok    x    ok      x    x   ok     x     ok  
'''
