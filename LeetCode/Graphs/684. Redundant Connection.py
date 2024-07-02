# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
# The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. 
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

# Example 1:
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]

# Example 2:
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
 
# Constraints:   
# edges[i].length == 2   
# 1 <= ai < bi <= edges.length    ai != bi
# There are no repeated edges.    The given graph is connected.

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [0 for i in range(len(edges) + 1)]
        def find_par(x) :
            if x != parent[x] :
                parent[x] = find_par(parent[x])
            return parent[x]
        def union(x , y) :
            par_x = find_par(x)
            par_y = find_par(y)
            if par_x == par_y :
                return False
            if rank[par_x] > rank[par_y] :
                parent[par_y] = par_x
            elif rank[par_y] > rank[par_x] :
                parent[par_x] = par_y
            else :
                parent[par_x] = par_y
                rank[par_y] += 1
            return True 

        for x , y in edges :
            if union(x , y) == False :
                return [x , y]
