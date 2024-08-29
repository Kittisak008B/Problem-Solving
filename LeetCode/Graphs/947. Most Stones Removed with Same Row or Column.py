# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, 
# return the largest possible number of stones that can be removed.

# Example 1:
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Explanation: One way to remove 5 stones is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,1].
# 2. Remove stone [2,1] because it shares the same column as [0,1].
# 3. Remove stone [1,2] because it shares the same row as [1,0].
# 4. Remove stone [1,0] because it shares the same column as [0,0].
# 5. Remove stone [0,1] because it shares the same row as [0,0].
# Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
  
# Example 2:
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# Explanation: One way to make 3 moves is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,0].
# 2. Remove stone [2,0] because it shares the same column as [0,0].
# 3. Remove stone [0,2] because it shares the same row as [0,0].
# Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

# Example 3:
# Input: stones = [[0,0]]
# Output: 0
# Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
 
# Constraints:
# 1 <= stones.length <= 1000
# 0 <= xi, yi <= 10**4
# No two stones are at the same coordinate point.

class UnionFind:
    def __init__(self , n) :
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)] 

    def find_parent(self , x) :
        if x != self.parent[x] :
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    def union(self , x , y) :
        Px = self.find_parent(x)
        Py = self.find_parent(y)
        if Px == Py : #don't need to union ->parent_x and parent_y already in the same set
            return False 
        if Px != Py :
            if self.rank[Px] > self.rank[Py]:
                self.parent[Py] = Px
            elif self.rank[Px] < self.rank[Py]:
                self.parent[Px] = Py
            else:
                self.parent[Px] = Py
                self.rank[Py] += 1
            return True

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        X , Y = {} , {}
        Uf = UnionFind(len(stones))
        count = 0
        for stone_i , (x,y) in enumerate(stones) :
            if x in X :
                count += Uf.union(stone_i , X[x])
            else :
                X[x] = stone_i
            if y in Y :
                count += Uf.union(stone_i , Y[y])
            else :
                Y[y] = stone_i
        return count
'''
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
         stone_0  1     2     3     4     5  
X : 0:stone_0 , 1:stone_2 , 2:stone_4
Y : 0:stone_0 , 1:stone_1 ,2:stone_3  

stone_0 -- stone_1 -- stone_4 -- stone_5
 |                                 |
 stone_2 -- stone_3  ---------------  -> union(stone_5,stone_3) already has same parent  
                          
count = 0
stone_0-connect-stone_1 ->count=1
stone_0-stone_2 ->count=2
stone_2-stone_3 ->count=3
stone_1-stone_4 ->count=4
stone_4-stone_5 ->count=5
stone_5-stone_3 ->count=5 -> union(stone_5,stone_3) already has same parent (gonna return False)
'''
