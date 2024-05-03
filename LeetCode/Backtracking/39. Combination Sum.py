# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7. These are the only two combinations.
  
# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Constraints:
# All elements of candidates are distinct.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        def backtrack(i , summ) :
            if summ == target :
                ans.append(cur[:])
                return
            if summ > target or i >= len(candidates) :
                return
            cur.append(candidates[i])
            backtrack(i , summ + candidates[i])
            cur.pop() 

            backtrack(i+1 , summ)
        backtrack(0 , 0)
        return ans
#                                                []                                 i=0
#                             [2]                                  []               i=1
#                 [2,2]                  [2]                [3]           []        i=2
#         [2,2,2]      [2,2]        [2,3]     [2]       [3,6]  [3]     [6]     []   i=3
# [2,2,2,2][2,2,2] [2,2,3][2,2] [2,3,6][2,3] [2,6][2]       [3,7][3] [6,7][6] [7][] i=4

# sol2
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         ans = []
#         cur = []
#         def backtrack(start , summ) :
#             if summ > target :
#                 return 
#             if summ == target and cur not in ans :
#                 ans.append(cur[:])
#             for i in range(start , len(candidates)) :
#                 cur.append(candidates[i])
#                 backtrack(i , summ + candidates[i])
#                 cur.pop()
#         backtrack(0 , 0)
#         return ans

# candidates = [2,3,6,7], target = 7
#          _______ [ ] ___________________
#         /                \         \    \
#       [2]__________      [3]____   [6]  [7]ok
#       /     \      \       \    \     \
#      [22]__  [23] [26]ok   [33] [35]x [66]x
#     /      \    \            \
#    [222] [223]ok [233]x      [333]x
#   /
# [2222]x
