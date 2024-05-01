# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        count = {x:0 for x in nums}
        for x in nums :
            count[x] += 1
        def backtrack() :
            if len(cur) == len(nums) :
                ans.append(cur[:])
                return
            for x in count :
                if count[x] > 0 :
                    cur.append(x)
                    count[x] -= 1
                    backtrack()

                    count[x] += 1
                    cur.pop()
        backtrack()
        return ans
    #       [1]      [2]
    #    [1,1][1,2]  [2,1]
    #[1,1,2][1,2,1]  [2,1,1]
