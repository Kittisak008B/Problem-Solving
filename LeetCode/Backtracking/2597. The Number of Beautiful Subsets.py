# You are given an array nums of positive integers and a positive integer k.
# A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.
# Return the number of non-empty beautiful subsets of the array nums.
# A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

# Example 1:
# Input: nums = [2,4,6], k = 2
# Output: 4
# Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
# It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

# Example 2:
# Input: nums = [1], k = 1
# Output: 1
# Explanation: The beautiful subset of the array nums is [1].
# It can be proved that there is only 1 beautiful subset in the array [1].

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        def bt(i , hm) :
            if i == len(nums) :
                return 1
            ans = bt(i+1 , hm)  # NOT include nums[i]
            if not hm[nums[i]+k] and not hm[nums[i]-k]:  # Include nums[i]
                hm[nums[i]] += 1
                ans += bt(i+1 , hm)
                hm[nums[i]] -= 1
            return ans
        return bt(0 , defaultdict(int)) -1
'''
[2,4,6] k=2
          _____[ ]_____
         /             \        
       []               [2]
      /   \            /    \     
    []    [4]       [2]     [2,4] x
    /\     /\        /\  
   /  \   /  \      /  \          
 []x [6] [4][4,6]x [2][2,6]  ans =4

'''

# class Solution:
#     def beautifulSubsets(self, nums: List[int], k: int) -> int:
#         ans = []
#         cur = []
#         self.res = 0
#         def bt(start , hm) :
#             if start == len(nums) :
#                 return
#             ans.append(cur[:])
#             for i in range(start , len(nums)) :
#                 if not hm[nums[i]-k] and not hm[nums[i]+k] :
#                     hm[nums[i]] += 1
#                     cur.append(nums[i])
#                     self.res += 1
#                     bt(i+1 , hm)
#                     hm[nums[i]] -= 1
#                     cur.pop()
#         bt(0 , defaultdict(int))
#         # print(ans)
#         # return len(ans) -1
#         return self.res
'''
       _____ [ ]x_____
      /          |     \
     [2]         [4]    [6]
    /   \        |
  [2,4]x[2,6]    [4,6]x
  /
[2,4,6]x
'''
