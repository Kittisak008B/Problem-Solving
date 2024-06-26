# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.
# Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.
# The answer is guaranteed to fit in a 32-bit signed integer.

# Example 1:
# Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# Output: 4
# Explanation: Since your initial capital is 0, you can only start the project indexed 0.
# After finishing it you will obtain profit 1 and your capital becomes 1.
# With capital 1, you can either start the project indexed 1 or the project indexed 2.
# Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
# Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

# Example 2:
# Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
# Output: 6

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_cap = [(capital[i] , profits[i]) for i in range(len(profits))]
        heapq.heapify(min_cap)
        max_heap = []
        for _ in range(k) :
            while min_cap and min_cap[0][0] <= w :
                c , p = heapq.heappop(min_cap)
                heapq.heappush(max_heap , -p)
            if max_heap :
                w += -heapq.heappop(max_heap)
        return w
