# You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

# Example 1:
# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].

# Example 2:
# Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
# Output: [1,1]
 
# Constraints:
# nums.length == k
# 1 <= k <= 3500
# 1 <= nums[i].length <= 50
# -10**5 <= nums[i][j] <= 10**5
# nums[i] is sorted in non-decreasing order.

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        left = nums[0][0]
        right = nums[0][0]
        for i in range(len(nums)) :
            left = min(left , nums[i][0])
            right = max(right , nums[i][0])
            heapq.heappush(min_heap , (nums[i][0] , i , 0))
        #print(min_heap)
        #print(left , right)
        res = [left , right]
        while True :
            num , i , idx = heapq.heappop(min_heap)
            idx += 1
            if idx == len(nums[i]) :
                break
            next_num = nums[i][idx]
            heapq.heappush(min_heap , (next_num , i , idx))
            #print(min_heap)
            right = max(right , next_num)
            left = min_heap[0][0]
            if right - left < res[1] - res[0] :
                res = [left , right]
        return res
'''
Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]

min_heap = [(0, 1, 0), (4, 0, 0), (5, 2, 0)]
left , right = 0 , 5

[(4, 0, 0), (5, 2, 0), (9, 1, 1)]     #pop 0 push 9   right=9 left=4
[(5, 2, 0), (9, 1, 1), (10, 0, 1)]    #pop 4 push 10  right=10 left=5
[(9, 1, 1), (10, 0, 1), (18, 2, 1)]   #pop 5 push 18  right=18 left=9
[(10, 0, 1), (18, 2, 1), (12, 1, 2)]  #pop 9 push 12  right=18 left=10
[(12, 1, 2), (18, 2, 1), (15, 0, 2)]  #pop 10 push 15 right=18 left=12 
[(15, 0, 2), (18, 2, 1), (20, 1, 3)]  #pop 12 push 20 right=20 left=15
[(18, 2, 1), (20, 1, 3), (24, 0, 3)]  #pop 15 push 24 right=24 left=18
[(20, 1, 3), (24, 0, 3), (22, 2, 2)]  #pop 18 push 22 right=24 left=20 right-left=4->smallest 
pop 20 idx=3 +1 =4  == len(nums[1]) -> break
'''
