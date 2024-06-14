# Alice and Bob take turns playing a game, with Alice starting first.
# Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.
# Also, if a player cannot make a move, he/she loses the game.
# Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

# Example 1:
# Input: n = 1
# Output: true
# Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.

# Example 2:
# Input: n = 2
# Output: false
# Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).

# Example 3:
# Input: n = 4
# Output: true
# Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = {}
        def dfs(n) :
            if n == 0 :
                return False
            if n in dp :
                return dp[n]
            for i in range(1 , math.floor(math.sqrt(n)) + 1) :
                if dfs(n -(i**2)) == False :
                    dp[n] = True
                    return dp[n]
            dp[n] = False
            return dp[n]
        return dfs(n)
'''       
can remove 1,4,9,16,...

                           n=4 True  
                            / Alice remove 4
                          n=0 False  
          n=3 True
         / Alice remove 1
        n=2 False
        / Bob remove 1
     n=1 True
      / Alice remove 1
    n=0 False

                                     ____ 7 _____
                    Alice remove 1  /            \ Alice remove 4 ->#not optimal Bob gonna win -> Alice dont make this move
                                __6___            3
                         Bob -1/      \-4          \ Bob remove 1
                              5         2            2
                    Alice -1 / \-4       \-1          \ Alcie remove 1
                            4    1         1            1
  #not optimal <--  Bob -1 / \-4  \-1       \-1          \ Bob remove 1
   Alice gonna win       3    0    0->B win  0 ->B win    0  ->Bob win
                        /    ->B win
                   A -1/         *** 7 -> False Bob win
                      2
                 B -1/
                    1
               A -1/
                  0 ->Alice win
'''
