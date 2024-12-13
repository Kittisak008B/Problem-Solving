# You are given an array nums consisting of positive integers. Starting with score = 0, apply the following algorithm:
# Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
# Add the value of the chosen integer to score. Mark the chosen element and its two adjacent elements if they exist.
# Repeat until all the array elements are marked. Return the score you get after applying the above algorithm.

# Example 1:
# Input: nums = [2,1,3,4,5,2]
# Output: 7
# Explanation: We mark the elements as follows:
# - 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2*,1*,3*,4,5,2].
# - 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2*,1*,3*,4,5*,2*].
# - 4 is the only remaining unmarked element, so we mark it: [2*,1*,3*,4*,5*,2*].
# Our score is 1 + 2 + 4 = 7.

# Constraints:  1 <= nums.length <= 10**5    1 <= nums[i] <= 10**6

class Solution:
    def findScore(self, nums: List[int]) -> int:
        q = sorted(enumerate(nums) , key = lambda x : (x[1] , x[0]))
        visited = set()
        score = 0
        for index , num in q :
            if index not in visited :
                score += num
                visited.add(index)
                if index > 0 :
                    visited.add(index - 1)
                if index < len(nums) - 1 :
                    visited.add(index + 1)
        return score
      
