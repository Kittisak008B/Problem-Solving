# There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, 
# where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.
# You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. 
# You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.
# The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. 
# The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.
# Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

# Example 1:
# Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
# Output: 0.78333
# Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.

# Constraints:
# 1 <= classes.length <= 10**5
# classes[i].length == 2
# 1 <= passi <= totali <= 10**5
# 1 <= extraStudents <= 10**5

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        min_heap = [[-( (p+1)/(t+1) - (p/t) ) , p , t ] for p , t in classes] 
        # delta ratio (student+1 ratio - old ratio) , pass , total
        heapq.heapify(min_heap)
        #print(min_heap)
        for _ in range(extraStudents) :
            x = heapq.heappop(min_heap)
            x[1] += 1
            x[2] += 1
            x[0] = -( (x[1]+1)/(x[2]+1) - (x[1]/x[2]) )
            heapq.heappush(min_heap , x)
            #print(min_heap)
        total_ratio = 0
        for x in min_heap :
            total_ratio += (x[1] / x[2])
        return total_ratio / len(min_heap)
      
