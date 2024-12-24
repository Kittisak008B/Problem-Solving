# There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. 
# You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, 
# where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that 
# there is an edge between nodes ui and vi in the second tree.
# You must connect one node from the first tree with another node from the second tree with an edge.
# Return the minimum possible diameter of the resulting tree. The diameter of a tree is the length of the longest path between any two nodes in the tree.

# Example 1:
#       0                0 
#     / | \                \
#    3  2  1                1
# Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]
# Output: 3
# Explanation: We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.

# Example 2:
#       6                  4     6
#       |                 /     /
#   7   3    1       7---2     3
#    \   \  /           / \   /
# 4---2----0           5    0 -----1
#    /
#   5
# Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
# Output: 5
# Explanation: We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.

# Constraints:
# 1 <= n, m <= 10**5
# edges1.length == n - 1
# edges2.length == m - 1
# edges1[i].length == edges2[i].length == 2
# edges1[i] = [ai, bi]
# 0 <= ai, bi < n
# edges2[i] = [ui, vi]
# 0 <= ui, vi < m
# The input is generated such that edges1 and edges2 represent valid trees.

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def find_diameter(edges) :
            adj = defaultdict(list)
            for i , j in edges :
                adj[i].append(j)
                adj[j].append(i)
            res = [0]
            def dfs(node , parent) :
                max_Depth = 1
                for neighbor in adj[node] :
                    if neighbor != parent :
                        depth = dfs(neighbor , node)
                        res[0] = max(res[0] , max_Depth + depth)
                        max_Depth = max(max_Depth , depth + 1)
                return max_Depth
            dfs(0 , -1)
            return res[0]
        d1 = find_diameter(edges1)
        d2 = find_diameter(edges2)
        return max(d1//2 + d2//2 +1 , d1 - 1 , d2 - 1)
      
