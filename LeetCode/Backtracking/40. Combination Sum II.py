# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        cur = []
        def backtrack(start , summ) :
            if summ > target :
                return 
            if summ == target and cur not in ans :
                ans.append(cur[:])
            for i in range(start , len(candidates)) :
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                cur.append(candidates[i])
                backtrack(i+1 , summ + candidates[i])
                cur.pop()
        backtrack(0 , 0)
        return ans
        
# candi = [1,1,2,5,6,7,10] target = 8
#                      [ ]__________________________________________________
#                    /  \                                      \      \     \
#                   /  [1]x start=0 i=1 candi[i]==candi[i-1]   [2]     [5]   ...
#                 [1]_________________________________          / \      \ 
#                /           \        \       \      \        [25] [26]ok  ...
#               [1,1]_______  [1,2]   [1,5]   [1,6] [1,7]ok     /
#               /     \    \       \       \     \            [256]x
#              [112] [115] [116]ok [125]ok [156]x [167]x
#             /           \
#            [1125]x  [1156]x    
