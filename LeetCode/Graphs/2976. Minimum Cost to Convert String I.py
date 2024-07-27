# You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. 
# You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].
# You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z 
# if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.
# Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.
# Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

# Example 1:
# Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
# Output: 28
# Explanation: To convert the string "abcd" to string "acbe":
# - Change value at index 1 from 'b' to 'c' at a cost of 5.
# - Change value at index 2 from 'c' to 'e' at a cost of 1.
# - Change value at index 2 from 'e' to 'b' at a cost of 2.
# - Change value at index 3 from 'd' to 'e' at a cost of 20.
# The total cost incurred is 5 + 1 + 2 + 20 = 28.
# It can be shown that this is the minimum possible cost.

# Example 2:
# Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
# Output: 12
# Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.

# Example 3:
# Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
# Output: -1
# Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.
 
# Constraints:
# 1 <= source.length == target.length <= 10**5
# source, target consist of lowercase English letters.
# 1 <= cost.length == original.length == changed.length <= 2000
# original[i], changed[i] are lowercase English letters.
# 1 <= cost[i] <= 10**6
# original[i] != changed[i]

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def dijkstra(src):
            heap = [(0 , src)]
            min_cost = {}
            while heap :
                cost , node = heapq.heappop(heap)
                if node not in min_cost :
                    min_cost[node] = cost
                    for neighbor , nei_cost in adj[node] :
                        heapq.heappush(heap , (cost + nei_cost , neighbor))
            return min_cost
        adj = defaultdict(list)
        for src , dest , cost in zip(original , changed , cost) :
            adj[src].append((dest , cost))
        min_cost = {}
        for src in set(source) :
            min_cost[src] = dijkstra(src)
        ans = 0
        for src , tar in zip(source , target) :
            if tar not in min_cost[src] :
                return -1
            ans += min_cost[src][tar]
        return ans
