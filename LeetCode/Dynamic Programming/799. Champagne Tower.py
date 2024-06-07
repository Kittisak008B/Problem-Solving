# We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.
# Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)
# For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.
# Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)

# Example 1:
# Input: poured = 1, query_row = 1, query_glass = 1
# Output: 0.00000
# Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

# Example 2:
# Input: poured = 2, query_row = 1, query_glass = 1
# Output: 0.50000
# Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. 
# The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.

# Example 3:
# Input: poured = 100000009, query_row = 33, query_glass = 17
# Output: 1.00000

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        Top_row = [poured]
        for row in range(1 , query_row+1) :
            cur_row = [0 for _ in range(row+1)]
            for i in range(row) :
                water_flow = (Top_row[i] - 1) / 2
                if  water_flow > 0 :
                    cur_row[i] += water_flow
                    cur_row[i + 1] += water_flow
            Top_row = cur_row
        return Top_row[query_glass] if Top_row[query_glass] < 1 else 1
'''
poured = 10
(value , water flow)
              (1 , 10)                 Water flow through the glass 10
              /      \
       (1 , 4.5)     (1 , 4.5)               flow (10-1)/2 = 4.5 
           /    \     /    \
       (1,1.75) (1, 3.5) (1,1.75)            flow (4.5-1)/2 = 1.75
      /       \   /    \   /     \
(0.375,0.375)(1,1.625)(1,1.625)(0.375,0.375) flow (1.75-1)/2 = 0.375 , (3.5-1)/2 = 1.25
'''

# class Solution:
#     def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
#         dp = {}
#         def dfs(i , j) :
#             if i == 0 and j == 0 :
#                 return poured
#             if j > i or j < 0 or i < 0 :
#                 return 0
#             if (i , j) in dp :
#                 return dp[(i , j)]
#             dp[(i,j)] = max( (dfs(i-1 , j-1) - 1)/2 , 0) + max( (dfs(i-1 , j) - 1)/2 , 0)
#             return dp[(i,j)]
#         return min(dfs(query_row,query_glass) , 1)
