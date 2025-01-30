# You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.
# You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.
# Divide the nodes of the graph into m groups (1-indexed) such that:
# Each node in the graph belongs to exactly one group.
# For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
# Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

# Example 1:
# group1|group2|group3|group4
#   5 ----- 1 --- 2 ---- 3
#             \      \   
#               \      \
#                 4 ---- 6
# Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
# Output: 4
# Explanation: As shown in the image we:
# - Add node 5 to the first group.
# - Add node 1 to the second group.
# - Add nodes 2 and 4 to the third group.
# - Add nodes 3 and 6 to the fourth group.
# We can see that every edge is satisfied.
# It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.

# Example 2:
# Input: n = 3, edges = [[1,2],[2,3],[3,1]]
# Output: -1
# Explanation: If we add node 1 to the first group, node 2 to the second group, and node 3 to the third group to satisfy the first two edges, we can see that the third edge will not be satisfied.
# It can be shown that no grouping is possible.
 
# Constraints:
# 1 <= n <= 500
# 1 <= edges.length <= 10**4
# edges[i].length == 2
# 1 <= ai, bi <= n
# ai != bi
# There is at most one edge between any pair of vertices.

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
      
        def isBipartite(graph , n) :
            def dfs(node , color , arr , graph) :
                arr[node] = color
                for nei in graph[node] :
                    if arr[nei] == -1 :
                        if dfs(nei , 1 - color , arr , graph) == False :
                            return False
                    elif arr[nei] == color :
                        return False
                return True
            arr = [-1] * (n+1)
            for node in range(1 , n+1) :
                if arr[node] == -1 :
                    if dfs(node , 0 , arr , graph) == False :
                        return False
            return True

        adj_list = defaultdict(list)
        for (src , dest) in edges :
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        #print(adj_list , n)
        if isBipartite(adj_list , n) == False :
            return -1

        def get_nodes_in_ConnectedComponent(src) :
            visited.add(src)
            q = collections.deque([src])
            component = set()
            component.add(src)
            while q :
                cur_node = q.popleft()
                for nei_node in adj_list[cur_node] :
                    if nei_node not in visited :
                        visited.add(nei_node)
                        component.add(nei_node)
                        q.append(nei_node)
            return component

        def bfs_get_max_group_from_each_node(src) :
            q = collections.deque([(src , 1)]) #node , group
            dist = {src : 1} 
            while q :
                cur_node , length = q.popleft()
                for nei in adj_list[cur_node] :
                    if nei not in dist :
                        dist[nei] = length + 1
                        q.append((nei , length + 1))
            return max(dist.values())

        res = 0
        visited = set()
        for node in range(1 , n + 1) :
            if node in visited :
                continue
            visited.add(node)
            connected_nodes_set = get_nodes_in_ConnectedComponent(node)
            #print(connected_nodes_set)
            max_group = 0  
            for src in connected_nodes_set :
                cur_group = bfs_get_max_group_from_each_node(src)
                max_group = max(max_group , cur_group)
            res += max_group #groups from each connected nodes
        return res
      
