# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:
# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

# Example 1:
# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
  
# Example 2:
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.

# Constraints:
# 1 <= nums.length <= 2 * 10**4
# 1 <= nums[i] <= 10**4

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count_num = defaultdict(int)
        for num in nums :
            count_num[num] += 1
        unique_num = []
        for key in count_num.keys() :
            unique_num.append(key)
        unique_num.sort()
        dp = {}
        def dfs(i) :
            if i >= len(unique_num) :
                return 0
            if i in dp :
                return dp[i]
            if i == len(unique_num) - 1 :
                return unique_num[i] * count_num[unique_num[i]]
            #pick
            if unique_num[i] + 1 == unique_num[i+1] :   
                pick = unique_num[i]*count_num[unique_num[i]] + dfs(i+2)
            else :
                pick = unique_num[i]*count_num[unique_num[i]] + dfs(i+1)
            #not pick
            not_pick = dfs(i+1)
            res = max(pick , not_pick)
            dp[i] = res
            return dp[i]
        return dfs(0)
'''
nums = [2,2,3,3,3,4]

count_num = {2:2 , 3:3 , 4:1} 
unique_num = [2,3,4]

               dfs(0)
               [2,3,4]
                i
        pick 2       not_pick 2
        /                   \ 
     2*2+dfs(2)             [2,3,4]
         [2,3,4]               i
              i                pick 3    not pick 3
             4*1               3*3=9       [2,3,4]
   this path->4+4 = 8        #9 is max          i  -> 4*1=4
'''
