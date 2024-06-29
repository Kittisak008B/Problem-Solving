# You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).
# You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.
# Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.
# A node u is an ancestor of another node v if u can reach v via a set of edges.

# Example 1:
# Input: n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
# Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
# Explanation:
# The above diagram represents the input graph.
# - Nodes 0, 1, and 2 do not have any ancestors.
# - Node 3 has two ancestors 0 and 1.
# - Node 4 has two ancestors 0 and 2.
# - Node 5 has three ancestors 0, 1, and 3.
# - Node 6 has five ancestors 0, 1, 2, 3, and 4.
# - Node 7 has four ancestors 0, 1, 2, and 3.

# Constraints:   edges[i].length == 2     There are no duplicate edges.     The graph is directed and acyclic.

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = [0] * n
        adj_list = defaultdict(list)
        for u,v in edges :
            adj_list[u].append(v)
            indegree[v] += 1

        q = collections.deque() #find start node (does't have any ancestors)
        for i in range(len(indegree)) :
            if indegree[i] == 0 :
                q.append(i)

        ans = [set() for _ in range(n)]
        while q :
            cur = q.popleft()
            for neighbor in adj_list[cur] :
                ans[neighbor].add(cur)
                ans[neighbor].update(ans[cur])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0 :
                    q.append(neighbor)
        return [sorted(x) for x in ans]
      
