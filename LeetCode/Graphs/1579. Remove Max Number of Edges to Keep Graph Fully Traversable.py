# Alice and Bob have an undirected graph of n nodes and three types of edges:
# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can be traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, 
# find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. 
# The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.
# Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

# Example 1:
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. 
# Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.

# Example 2:
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# Output: 0
# Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.

# Example 3:
# Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# Output: -1
# Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. 
# Therefore it's impossible to make the graph fully traversable.

# Constraints:   edges[i].length == 3     1 <= typei <= 3     1 <= ui < vi <= n     All tuples (typei, ui, vi) are distinct.

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
            return False #can remove edge
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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice , bob = UnionFind(n+1) , UnionFind(n+1)
        ans , alice_edges , bob_edges = 0 , 0 , 0
        for e_type , u , v in edges :
            if e_type == 3 :
                if alice.union(u , v) :
                    bob.union(u , v)
                    alice_edges += 1
                    bob_edges += 1
                else :
                    ans += 1
        for e_type , u , v in edges :
            if e_type == 1 : 
                if alice.union(u , v) :
                    alice_edges += 1
                else :
                    ans += 1
            if e_type == 2 :
                if bob.union(u , v) :
                    bob_edges += 1
                else :
                    ans += 1
        return ans if alice_edges == bob_edges == n-1 else -1
