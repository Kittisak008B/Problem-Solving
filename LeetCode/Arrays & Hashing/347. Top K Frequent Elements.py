# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for x in nums :
            if x not in hm :
                hm[x] = 0
            hm[x] += 1

        buckets = [[] for _ in range(len(nums)+1)]
        for key, freq in hm.items() :
            buckets[freq].append(key)
        
        ans = []
        for i in range(len(nums),0,-1) :
            for y in buckets[i] :
                ans.append(y)
            if len(ans) == k :
                return ans
