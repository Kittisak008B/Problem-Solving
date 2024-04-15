# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        hm = {}
        for x in nums1 :
            if x not in hm :
                hm[x] = 0
            hm[x] += 1
        for y in nums2 :
            if y in hm and hm[y] > 0 :
                hm[y] -= 1
                ans.append(y)
        return ans
