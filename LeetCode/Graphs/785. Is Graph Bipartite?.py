# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, 
# where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. 
# The graph has the following properties:
# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.
# Return true if and only if it is bipartite.

# Example 1:
# 0-----1
# |  \  |
# 3----2
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

# Example 2:
# 0-----1
# |     |
# 3-----2
# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 
# Constraints:
# graph.length == n
# 1 <= n <= 100
# 0 <= graph[u].length < n
# 0 <= graph[u][i] <= n - 1
# graph[u] does not contain u.
# All the values of graph[u] are unique.
# If graph[u] contains v, then graph[v] contains u.

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #A bipartite graph can be colored with two colors (let’s say 0 and 1) so that no adjacent nodes share the same color
        def dfs(node , color , arr) :
            arr[node] = color
            for nei in graph[node] :
                if arr[nei] == -1 : #if neighbor is uncolored->try to color it with opposite color
                    if dfs(nei , 1 - color , arr) == False :
                        return False
                elif arr[nei] == color : #if same color
                    return False
            return True
        N = len(graph)
        arr = [-1] * N #uncolored (unvisited)
        for node in range(N) :
            if arr[node] == -1 :
                if dfs(node , 0 , arr) == False :
                    return False
        return True
     
# class Solution:  #bfs
#     def isBipartite(self, graph: List[List[int]]) -> bool:  
#         N = len(graph)   
#         arr = [-1] * N
#         for node in range(N) :
#             if arr[node] == -1 :
#                 q = collections.deque([node])
#                 arr[node] = 0
#                 while q :
#                     src = q.popleft() 
#                     for nei in graph[src] :
#                         if arr[nei] == - 1 :
#                             arr[nei]  = 1 - arr[src]
#                             q.append(nei)
#                         elif arr[nei] == arr[src] :
#                             return False
#                         #print(src, nei ,arr, q)
#         return True 
