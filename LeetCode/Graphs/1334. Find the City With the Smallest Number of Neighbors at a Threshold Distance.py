# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
# Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

# Example 1:
# Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
# Output: 3
# Explanation: The figure above describes the graph. 
# The neighboring cities at a distanceThreshold = 4 for each city are:
# City 0 -> [City 1, City 2] 
# City 1 -> [City 0, City 2, City 3] 
# City 2 -> [City 0, City 1, City 3] 
# City 3 -> [City 1, City 2] 
# Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
  
# Constraints:
# 2 <= n <= 100
# 1 <= edges.length <= n * (n - 1) / 2
# edges[i].length == 3
# 0 <= fromi < toi < n
# 1 <= weighti, distanceThreshold <= 10^4
# All pairs (fromi, toi) are distinct.

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def dijkstra(src):
            heap = [(0 , src)]
            visited_node = set()
            while heap :
                dist , node = heapq.heappop(heap)
                if node not in visited_node :
                    visited_node.add(node)
                    for neighbor , dist2 in graph[node] :
                        nei_dist = dist + dist2
                        if nei_dist <= distanceThreshold :
                            heapq.heappush(heap , (nei_dist , neighbor))
            return visited_node

        graph = defaultdict(list)
        for i , j , d in edges:
            graph[i].append((j , d))
            graph[j].append((i , d))
        min_count = float('inf')
        res = None
        for node in range(n):
            count = len(dijkstra(node)) -1
            if count <= min_count:
                min_count = count
                res = node
        return res
