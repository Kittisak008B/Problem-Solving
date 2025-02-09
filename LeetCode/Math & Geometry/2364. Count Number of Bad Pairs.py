# You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
# Return the total number of bad pairs in nums.

# Example 1:
# Input: nums = [4,1,3,3]
# Output: 5
# Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
# The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
# The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
# The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
# The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
# There are a total of 5 bad pairs, so we return 5.

# Example 2:
# Input: nums = [1,2,3,4,5]
# Output: 0
# Explanation: There are no bad pairs.
 
# Constraints:
# 1 <= nums.length <= 10**5
# 1 <= nums[i] <= 10**9

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        #bad:  i - j != nums[i] - nums[j]
        #bad:  i - nums[i] != j - nums[j]
        N = len(nums)
        d = defaultdict(int)
        for i in range(N) :
            d[i - nums[i]] += 1
        total = N*(N-1)//2 #combinations C(n,r) = n!/((n-r)!r!)
        good_pairs = 0
        for count in d.values() :
            good_pairs += count*(count-1)//2
        bad_pairs = total - good_pairs
        return bad_pairs
      
