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
        pre = defaultdict(list)
        for course , p_course in prerequisites :
            pre[course].append(p_course)
        # print(pre)

        visited =set()
        def dfs(course) :
            if not pre[course] :
                return True
            if course in visited :
                return False
            visited.add(course)
            for p_course in pre[course] :
                if not dfs(p_course) :
                    return False
            pre[course] = []
            return True

        for course in range(numCourses) :
            if not dfs(course) :
                return False
        return True
      
