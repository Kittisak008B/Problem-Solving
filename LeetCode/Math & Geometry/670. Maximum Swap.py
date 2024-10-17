# You are given an integer num. You can swap two digits at most once to get the maximum valued number.
# Return the maximum valued number you can get.

# Example 1:
# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
  
# Example 2:
# Input: num = 9973
# Output: 9973
# Explanation: No swap.
 
# Constraints:
# 0 <= num <= 10**8

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)  
        res = num
        for i in range(len(num_str)) :
            for j in range(i + 1 , len(num_str)) :
                num_list = list(num_str)  
                num_list[i] , num_list[j] = num_list[j] , num_list[i] 
                temp = int(''.join(num_list)) 
                res = max(res , temp)
        return res
