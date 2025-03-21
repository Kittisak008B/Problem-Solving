# There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where 
# graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].
# A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).
# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
  
# Example 1:
#           +---------------------------+
#           |                           |
#           v                           |
#         +----+        +----+        +----+
#         | 0  | ---->  | 1  | ---->  | 3  |
#         +----+        +----+        +----+
#           |              |             
#           |  +-----------+  
#           |  |              
#           v  v             
#        +----+       +----+     +----+
#        | 2  | ----> | 5  |     | 6  |   (node 5 , node 6 : No outgoing edges)
#        +----+       +----+     +----+
#                       ^
#                       |   
#                     +----+
#                     | 4  |
#                     +----+
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: The given graph is shown above. Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
# Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

# Constraints:
# n == graph.length
# 1 <= n <= 10**4
# 0 <= graph[i].length <= n
# 0 <= graph[i][j] <= n - 1
# graph[i] is sorted in a strictly increasing order.
# The graph may contain self-loops.
# The number of edges in the graph will be in the range [1, 4 * 10**4].

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        dp = {}
        def dfs(i) :
            if i in dp :
                return dp[i]
            dp[i] = False
            for nei in graph[i] :
                if dfs(nei) == False :
                    return dp[i]
            dp[i] = True
            return dp[i]
        res = []
        for i in range(len(graph)) :
            if dfs(i) : # No cycle, safe paths
                res.append(i)
        return res
      
