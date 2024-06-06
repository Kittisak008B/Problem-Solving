# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array,
# then treat it as if there is a balloon with a 1 painted on it.
# Return the maximum coins you can collect by bursting the balloons wisely.

# Example 1:
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

# Example 2:
# Input: nums = [1,5]
# Output: 10

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for length in range(1 , len(nums) + 1) :
            for i in range(len(nums) + 1 - length) :
                j = i + length - 1
                for lastburst in range(i,j+1) :
                    left_val = 1
                    right_val = 1
                    if i != 0 :
                        left_val = nums[i-1]
                    if j != len(nums) - 1 :
                        right_val = nums[j+1]
                    val1_in_dp = 0
                    val2_in_dp = 0
                    if i != lastburst :
                        val1_in_dp = dp[i][lastburst - 1]
                    if j != lastburst :
                        val2_in_dp = dp[lastburst + 1][j]
                    dp[i][j] = max(dp[i][j] , val1_in_dp + val2_in_dp + left_val*nums[lastburst]*right_val)
        return dp[0][len(nums)-1]     
'''
    0      1      2       3    j (value , index of last burst balloon)
0 (3,0) (30,0) (159,0) (167,3)
1       (15,1) (135,2) (159,3)
2              (40,2)  (48,3)
3                      (40,3)
i

     [3 1 5 8]      
index 0 1 2 3   
     i,j
       i,j
         i,j
           i,j
length = 1 -> i,j=0 : (1*3*1,0)   i,j=1 :(3*1*5,1)   i,j=2 :(1*5*8,2)  i,j=3 :(5*8*1,3) 
----------
     [3 1 5 8]      
index 0 1 2 3  
      i j
        i j
          i j
length = 2 -> i=0,j=1 : if 0 last burst balloon -> 15 + 1*3*5 = 30
                        1 last burst -> 3 + 1*1*5 = 8  ; 0 last burst balloon value > 1 -> i=0,j=1 (30,0) 
           i=1,j=2 : if 1 last burst -> 40 + 3*1*8 = 64
                        2 last burst -> 15 + 3*8*5 = 135 ; (135,2)
           i=2,j=3 : if 2 last burst -> 40 + 1*5*1 = 45
                        3 last burst -> 40 + 1*8*1 = 48 ; (48,3)
----------
     [3 1 5 8]      
index 0 1 2 3
      i   j
        i   j
length = 3 -> i=0,j=2 : if 0 last -> 135 + 1*3*8 = 159
                        1 last -> 3 + 40 + 1*1*8 = 51
                        2 last -> 30 + 1*5*8 = 70 ; (159,0)
           i=1,j=3 : if 1 last -> 48 + 3*1*1 = 51
                        2 last -> 15 + 40 + 3*5*1 = 70
                        3 last -> 135 + 3*8*1 = 159 ; (159,3)
----------
     [3 1 5 8]      
index 0 1 2 3
      i     j
length = 4 -> i=0,j=3 : if 0 last -> 159 + 1*3*1 = 162
                        1 last -> 3 + 48 + 1*1*1 = 52
                        2 last -> 30 + 40 + 1*5*1 = 75
                        3 last -> 159 + 1*8*1 = 167 ; (167,3)

                        ## value = 167 and last burst balloon is index 3 

                        backtrack to find order of burst balloons 
                         [3 1 5 8]
                    index 0 1 2 3     
                                x burst last
                         [3 1 5]
                    index 0 1 2
                          x burst last
                           [1 5]
                    index   1 2
                              x burst last
                           [1]
                    index   1
                            x first to burst
                    ## index to burst to get max value -> index 1 , 2 , 0 , 3 
                                                       which is 1   5   3   8 in array         
'''
