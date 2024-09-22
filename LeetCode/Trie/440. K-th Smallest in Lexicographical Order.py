# Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

# Example 1:
# Input: n = 13, k = 2
# Output: 10
# Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.

# Example 2:
# Input: n = 1, k = 1
# Output: 1
 
# Constraints:
# 1 <= k <= n <= 10**9

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_step(start , end) : #how many numbers exist between prefix1 and prefix2
            steps = 0
            while start <= n :
                steps += min(n+1 , end) - start
                start *= 10
                end *= 10
            return steps
        cur = 1
        k -= 1
        while k > 0 :
            steps = count_step(cur , cur+1)
            if steps <= k : #If steps are less than or equal to k, skip this prefix's subtree
                cur += 1 #Move to the next prefix and decrease k by the number of steps we skip
                k -= steps
            else :
                cur *= 10 #Move to the next level of the tree 
                k -= 1
        return cur
'''
        /     \        \ 
       1___    2    ... 9
      /    \ 
     10 ...19
    /  \
  100...109   
'''
        # lexi = []
        # def dfs(x) :
        #     if x > n :
        #         return 
        #     lexi.append(x)
        #     x *= 10
        #     for i in range(10) :
        #         dfs(x+i)
        # for i in range(1,10) :
        #     dfs(i)
        # return lexi[k-1]
