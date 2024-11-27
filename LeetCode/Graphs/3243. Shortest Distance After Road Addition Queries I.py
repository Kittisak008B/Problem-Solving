# You are given an integer n and a 2D integer array queries.
# There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.
# queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. 
# After each query, you need to find the length of the shortest path from city 0 to city n - 1.
# Return an array answer where for each i in the range [0, queries.length - 1], 
# answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.

# Example 1:
# Input: n = 5, queries = [[2,4],[0,2],[0,4]]
# Output: [3,2,1]
# Explanation:
# 0 -> 1 -> 2 -> 3 -> 4
#            |________|   After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.

# 0 -> 1 -> 2 -> 3 -> 4
# |________| |________|   After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.

# 0 -> 1 -> 2 -> 3 -> 4
# |________| |________|
# |___________________|   After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

# Constraints:
# 3 <= n <= 500
# 1 <= queries.length <= 500
# queries[i].length == 2
# 0 <= queries[i][0] < queries[i][1] < n
# 1 < queries[i][1] - queries[i][0]
# There are no repeated roads among the queries.

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs(neighbor) :
            q = collections.deque([(0 , 0)])  #(city, distance)
            visited = set([(0)])
            while q :
                for _ in range(len(q)) :
                    city , distance = q.popleft()  
                    if city == n - 1 :
                        return distance
                    for nei in neighbor[city] :
                        if nei not in visited :
                            q.append((nei , distance + 1))
                            visited.add(nei)
            return -1
        res = []
        neighbor  = [[i+1] for i in range(n-1)] + [[]]
        for start , end in queries :
            neighbor[start].append(end)
            distance = bfs(neighbor)
            res.append(distance)
        return res
      
