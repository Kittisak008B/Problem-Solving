# You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. 
# You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.
# Return the number of complete connected components of the graph.
# A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
# A connected component is said to be complete if there exists an edge between every pair of its vertices.

# Example 1:
#               0-----1       3
#    5           \   /        |
#                  2          4
# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
# Output: 3
# Explanation: From the picture above, one can see that all of the components of this graph are complete.
  
# Example 2:
#     0----1         5-----3
#      \  /               /  
#       2                4
# Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
# Output: 1
# Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. 
# On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. 
# Thus, the number of complete components in this graph is 1.
 
# Constraints:
# 1 <= n <= 50
# 0 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no repeated edges.

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a , b in edges :
            adj[a].append(b)
            adj[b].append(a)
        def dfs(x) :
            component.add(x)
            for child in adj[x] :
                if child not in visited :
                    visited.add(child)
                    dfs(child)
        res = 0
        visited = set()
        for i in range(n) :
            if i not in visited :
                component = set()
                visited.add(i)
                dfs(i)
                is_complete = True
                for node in component :
                    if len(adj[node]) != len(component) - 1 :
                        is_complete = False
                        break  
                if is_complete :
                    res += 1 
        return res
      
