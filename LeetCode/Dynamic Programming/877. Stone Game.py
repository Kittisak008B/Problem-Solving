# Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
# The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.
# Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row.
# This continues until there are no more piles left, at which point the person with the most stones wins.
# Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

# Example 1:
# Input: piles = [5,3,4,5]
# Output: true
# Explanation: 
# Alice starts first, and can only take the first 5 or the last 5.
# Say she takes the first 5, so that the row becomes [3, 4, 5].
# If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
# If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alice, so we return true.

# Example 2:
# Input: piles = [3,7,2,3]
# Output: true

# Constraints:
# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles[i]) is odd.

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(p , i , j ) :
            if i > j :
                return 0
            if (p , i , j ) in dp :
                return dp[(p , i , j )] 
            if p == 0 :
                dp[(p , i , j)] = max(piles[i] + dfs(1 , i+1 , j) , piles[j] + dfs(1 , i , j-1))
                return dp[(p , i , j)] 
            else :
                dp[(p , i , j)] = min( -piles[i] + dfs(0 , i+1 , j) , -piles[j] + dfs(0 , i , j-1))
                return dp[(p , i , j)] 
        return dfs(p=0 , i=0 , j=len(piles) - 1) > 0  #p=0 Alice, p=1 Bob


# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         dp = {}
#         def dfs(i , j) :
#             if i > j :
#                 return 0
#             if (i , j) in dp :
#                 return dp[(i , j)]
#             ans = float('-inf')
#             ans = max(ans , piles[i] - dfs(i+1 , j) , piles[j] - dfs(i , j-1))
#             dp[(i , j)] = ans 
#             return dp[(i , j)]
#         return dfs(0 , len(piles)-1) > 0
'''
piles = [3,7,2,3]

ans = max(-inf , 3 - max(-inf , 7 - max(-inf , 2-max(-inf,3) , 3-max(-inf,2)) , 3- max(-inf,7-max(-inf,2),2-max(-inf,7)) ) , 3 - max(-inf, 3 - 5 , 2 - 4 ))
ans = max(-inf , 3 - max( 7- 1 , 3- 5 ) , 3 - max( 3 - 5 , 2 - 4 ))
ans = max(-inf , 3 - max( 6 , -2 ) ,3 - max( -2 , -2 ))
ans = max(-inf , 3 - 6 , 3 - (-2))
ans = max(-inf , -3 , 5 ) -> relative_score = 5 (Alice pick 3 form last then Bob pick 3 at first then Alice pick 7 then bob pick 2  ## Alice 3+7=10 Bob 3+2=5 relative_score=10-5= 5)
'''
