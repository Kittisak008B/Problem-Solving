# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), 
# where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. 
# If it is impossible for all the n nodes to receive the signal, return -1.

# Example 1:
# (1)<-1--(2)--1->(3)--1->(4)
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

# Example 2:
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u , v , time in times :
            graph[u].append((v ,time))
        # print(graph)
        min_times = {}
        min_heap = [(0 , k)]
        while min_heap :
            time_to_node , node = heapq.heappop(min_heap)
            if node not in min_times :
                min_times[node] = time_to_node

                for nei_node , nei_time in graph[node] :
                    if nei_node not in min_times :
                        heapq.heappush(min_heap , (nei_time + time_to_node , nei_node))
        return max(min_times.values()) if len(min_times) == n else -1
      
