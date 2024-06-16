# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

# Example 1:
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3

# Example 2:
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
 
# Constraints:  points[i].length == 2   All the points are unique.

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0 
        for i in range(len(points)) :
            x1 , y1 = points[i][0] , points[i][1]
            slope = defaultdict(int)
            for j in range(i + 1 , len(points)) :
                x2 , y2 = points[j][0] , points[j][1] 
                m = (y2- y1)/(x2 - x1) if (x2 - x1) != 0 else float('inf')
                slope[m] += 1
                ans = max(ans , slope[m]) 
        return ans + 1
