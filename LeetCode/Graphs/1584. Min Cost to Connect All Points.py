# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

# Example 1:
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.

# Constraints:  All pairs (xi, yi) are distinct.

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ans = 0
        visited = set()
        heap = [(0,0)]
        while heap :
            dist , i = heapq.heappop(heap)
            if i not in visited :
                visited.add(i)
                ans += dist
                xi , yi = points[i]
                for j in range(len(points)) :
                    if j not in visited :
                        xj , yj = points[j]
                        manhattan_dist = abs(xi-xj) + abs(yi-yj)
                        heapq.heappush(heap , (manhattan_dist , j))
        return ans
        #Minimum Spanning Tree
        #Prim's Algorithm 
