# Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. 
# The objective of the game is to end with the most stones. 
# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
# The game continues until all the stones have been taken.
# Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

# Example 1:
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. 
# Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, 
# then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

# Example 2:
# Input: piles = [1,2,3,4,5,100]
# Output: 104

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        def dfs(p , i , M) :
            if i >= len(piles) :
                return 0
            if (p , i , M) in dp :
                return dp[(p , i , M)]
            ans = 0 if p==1 else float('inf')
            sum_piles = 0
            for x in range(1 , 2*M +1) :
                if i + x - 1 < len(piles) :
                    sum_piles += piles[i + x -1]
                    if p == 1 :
                        ans = max(ans , sum_piles + dfs(2 , i + x , max(M, x)))
                    else :
                        ans = min(ans , dfs(1 , i + x , max(M, x)))
            dp[(p , i , M)] = ans
            return dp[(p , i , M)]
        return dfs(1 , 0 , 1) # p=1 Alice , p=2 Bob
'''
piles = [1,2,3,4,5,100]     Assuming Alice and Bob play optimally
                       
                M=1 , 1 <= x <= 2M can take 1 or 2piles
                      /   \ 
Alice take x=1 piles(1)      Alice take x=2 piles(1+2) x=2 -> M=2  1 <= x <= 2M -> 1 <= x <= 4 
       /            \                                     not optimal Bob gonna take 4 (3+4+5+100) :Alice only got 3
      /              \                              
     /                \            
Bob take 1piles(2)    Bob take 2piles(2+3) ->M=2 not optimal Alice gonna take 3 (4+5+100) :Bob only got 5
  /                \
 /                   \
Alice take 1piles(3)   Alcie take 2piles(3+4) ->not optimal Bob gonna take 2 (5+100) :Alice only got 8              
|                   \  
|                    \
Bob take 1piles(4)   Bob take 2piles(4+5)
->not optimal              \
Alice gonna take            ALice take 1piles(100)  
2piles (5+100)             ### Alice got 104 , Bob got 11 
:Bob only got 6                 
'''
