# There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.
# We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:
# Every worker in the paid group must be paid at least their minimum wage expectation.
# In the group, each worker's pay must be directly proportional to their quality. This means if a worker’s quality is double that of another worker in the group, then they must be paid twice as much as the other worker.
# Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10-5 of the actual answer will be accepted.

# Example 1:
# Input: quality = [10,20,5], wage = [70,50,30], k = 2
# Output: 105.00000
# Explanation: We pay 70 to 0th worker and 35 to 2nd worker.
  
# Example 2:
# Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
# Output: 30.66667
# Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        worker = [(wage[i] / quality[i],quality[i]) for i in range(len(quality))]
        worker.sort(key = lambda x : x[0])
        quality_sum = 0
        min_cost = float('inf')
        max_heap = []
        for ratio , q in worker :
            heapq.heappush(max_heap , -q)
            quality_sum += q
            if len(max_heap) > k :
                quality_sum += heapq.heappop(max_heap)
            if len(max_heap) == k :
                min_cost = min(min_cost , quality_sum*ratio)
        return min_cost
'''
quality = [10,20,5], wage = [70,50,30], k = 2  
                     quality_sum*ratio->(10+5)*7  Output: 105.00000

worker = [(2.5, 20), (6.0, 5), (7.0, 10)]

quality_sum = 20
min_cost = inf
max_heap = [-20]

quality_sum = 25
min_cost = (20+5)*6 = 150
max_heap = [-20 -5]

quality_sum = 15
min_cost = 15*7=105
max_heap = [ -5 -10]
-----------------------
quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667

worker = [(0.2, 10), (0.2, 10), (1.3333333333333333, 3), (7.0, 1), (8.0, 1)]

quality_sum = 23
min_cost = 30.666666666666664
max_heap = [-10, -10, -3]

quality_sum = 14
min_cost = 30.666666666666664
max_heap = [-10, -1, -3]

quality_sum = 5
min_cost = 30.666666666666664
max_heap = [-3, -1, -1]
'''
