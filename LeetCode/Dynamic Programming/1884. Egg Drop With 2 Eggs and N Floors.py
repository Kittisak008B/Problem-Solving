# You are given two identical eggs and you have access to a building with n floors labeled from 1 to n.
# You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.
# In each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.
# Return the minimum number of moves that you need to determine with certainty what the value of f is.

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: We can drop the first egg from floor 1 and the second egg from floor 2.
# If the first egg breaks, we know that f = 0.
# If the second egg breaks but the first egg didn't, we know that f = 1.
# Otherwise, if both eggs survive, we know that f = 2.

class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(2+1)]
        for i in range(1 , n+1) :
            dp[1][i] = i
        dp[2][1] = 1
        for floor in range(2 , n+1) :
            c = float('inf')
            for drop in range(1 , floor+1) :
                c = min(c , 1 + max(dp[1][drop - 1] , dp[2][floor - drop]) )
            dp[2][floor] = c
        return dp[2][-1]     
'''
   0  1  2  3  4  5 floor
0  0  0  0  0  0  0
1  0  1  2  3  4  5        minimum moves to find out which floor to drop an egg from so that it breaks.
2  0  1  2  2  3  3
egg

2 eggs  1 floor : have 1 floor only 1 move to find out
---
2 eggs  2 floors :if drop 1 egg from floor1 -> if it breaks-> move = 1 + 0 
                                               if it doesnt breaks -> you have 2eggs and 1 floor to find out ->move= 1+1 = 2
                                            # 1+max(0 , 1) = 2
                  if drop 1 egg from floor2 -> if breaks-> you have 1 egg and 1 floor to find out ->move = 1 + 1 = 2
                                               if doesnt breaks -> you find out -> move = 1 + 0
                                            # 1+max(1,0) = 2
                  min(2 , 2) = 2
---
2 eggs 3 floors :if drop 1 egg from floor1 -> if breaks ->find out->move = 1 + 0
                                              if doesnt breaks -> have 2eggs and 2 floors to find -> move = 1 + 2 = 3 
                                           # 1 + max(0,2) = 3 
                 if drop 1 egg from floor2 -> if breaks-> have 1 egg and 1 floor to find -> move = 1 + 1 = 2
                                              if doesnt breaks -> have 2 egg and 1 floor to find -> move = 1 + 1 =2
                                           # 1 + max(1,1) = 2
                 if drop 1 egg from floor3 -> if breaks-> have 1 egg 2 floors to find -> move = 1 + 2 = 3
                                              if doest breaks -> find out -> move = 1 + 0
                                           # 1 + max(2,0) = 3
                 min(3,2,3) = 2
---
2 eggs 4 floors : if drop 1egg from floor1 -> if breaks ->find out -> move = 1 + 0
                                              if doesnt breaks -> have 2 eggs 3 floors to find -> move= 1 + 2 = 3
                                           # 1 + max(0 , 2) = 3
                  if drop 1egg from floor2 -> if breaks -> have 1 egg 1 floor to find -> move = 1 + 1 = 2
                                              if doesnt breaks -> have 2 eggs 2 floors -> move = 1 + 2 = 3
                                           # 1 + max(1 , 2) = 3
                  if drop 1egg from floor3 -> if breaks -> have 1 egg 2 floors -> move = 1 + 2 = 3
                                              if doesnt breaks -> have 2 eggs 1 floors -> move = 1 + 1 = 2
                                           # 1 + max(2 , 1) = 3
                  if drop 1egg from floor4 -> if breaks -> have 1 egg 3 floors -> move = 1 + 3 = 4
                                              if doesnt breaks -> find out -> move = 1 + 0
                                           # 1 + max(3 , 0) = 4
                  min(3,3,3,4) = 3
---
2 eggs 5 floors : if drop 1egg from floor1 -> if breaks ->find out -> move = 1 + 0
                                              if doesnt breaks -> have 2 eggs 4 floors to find -> move= 1 + 3 = 4
                                           # 1 + max(0 , 3) = 4
                  if drop 1egg from floor2 -> if breaks -> have 1 egg 1 floor to find -> move = 1 + 1 = 2
                                              if doesnt breaks -> have 2 eggs 3 floors -> move = 1 + 2 = 3
                                           # 1 + max(1 , 2) = 3
                  if drop 1egg from floor3 -> if breaks -> have 1 egg 2 floors -> move = 1 + 2 = 3
                                              if doesnt breaks -> have 2 eggs 2 floors -> move = 1 + 2 = 3
                                           # 1 + max(2 , 2) = 3
                  if drop 1egg from floor4 -> if breaks -> have 1 egg 3 floors -> move = 1 + 3 = 4
                                              if doesnt breaks -> have 2 eggs 1 floor -> move = 1 + 1 = 2
                                           # 1 + max(3 , 1) = 4
                  if drop 1egg from floor5 -> if breaks -> have 1 egg 4 floors -> move = 1 + 4 = 5
                                              if doesnt breaks -> find out -> move = 1 + 0
                                           # 1 + max(4 , 0) = 5      
                  min(4,3,3,4,5) = 3
'''
