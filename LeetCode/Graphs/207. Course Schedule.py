# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
  
# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 
# Constraints:   prerequisites[i].length == 2    0 <= ai, bi < numCourses     All the pairs prerequisites[i] are unique.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for course , pre_req in prerequisites :
            adj_list[course].append(pre_req)
        # print(adj_list)

        seen = set()
        def dfs(course) :
            if course in seen :
                return False
            if adj_list[course] == [] :
                return True
        
            seen.add(course)
            for pre_req in adj_list[course] :
                if not dfs(pre_req):
                    return False
            seen.remove(course)
        
            adj_list[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
      
