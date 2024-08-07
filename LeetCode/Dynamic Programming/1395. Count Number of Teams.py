# There are n soldiers standing in a line. Each soldier is assigned a unique rating value. You have to form a team of 3 soldiers amongst them under the following rules:
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

# Example 1:
# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

# Example 2:
# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.

# Constraints:
# n == rating.length
# 3 <= n <= 1000
# 1 <= rating[i] <= 10**5
# All the integers in rating are unique.

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        dp = {}
        def helper(i , count , DESC) :
            if (i , count , DESC) in dp :
                return  dp[(i , count , DESC)]
            if count == 3 :
                return 1
            if i == len(rating) :
                return 0
            res = 0
            for j in range(i + 1 , len(rating)) :
                if DESC and rating[i] > rating[j] :
                    res += helper(j , count + 1 , DESC)
                if not DESC and rating[i] < rating[j] :
                    res += helper(j , count + 1 , DESC)
            dp[(i , count , DESC)] = res
            return dp[(i , count , DESC)]
        ans = 0
        for i in range(len(rating)) :
            ans += helper(i , 1 , DESC=True)
            ans += helper(i , 1 , DESC=False)
        return ans
