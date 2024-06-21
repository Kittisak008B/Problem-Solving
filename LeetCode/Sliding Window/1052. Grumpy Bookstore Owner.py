# There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
# On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
# Return the maximum number of customers that can be satisfied throughout the day.

# Example 1:
# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
# Output: 16
# Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

# Example 2:
# Input: customers = [1], grumpy = [0], minutes = 1
# Output: 1
 
# Constraints:
# n == customers.length == grumpy.length
# 1 <= minutes <= n <= 2 * 104     0 <= customers[i] <= 1000
# grumpy[i] is either 0 or 1.

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        cur = 0
        for i in range(len(customers)) :
            cur += customers[i] if grumpy[i] == 0 else 0
        max_sum = cur 
        for i in range(len(customers)) :
            cur += customers[i] if grumpy[i] == 1 else 0
            if i >= minutes :
                cur -= customers[i - minutes] if grumpy[i - minutes] == 1 else 0
            if cur > max_sum :
                max_sum = cur
        return max_sum
'''
customers =   1 0 1 2 1 1 7 5     minutes = 3
grumpy    =   0 1 0 1 0 1 0 1
              cur = 1+1+1+7=10
              max_sum = cur        

customers =   1 0 1 2 1 1 7 5     minutes = 3
grumpy    =   0 1 0 1 0 1 0 1
              x x x              sliding window length=minutes  if grumpy ->add , delete number
              cur = 10 + 0 = 10      
              if cur > max_sum : max_sum = cur 
              
customers =   1 0 1 2 1 1 7 5     minutes = 3
grumpy    =   0 1 0 1 0 1 0 1
                x x x
             i-3    i
              cur = 10 + 2 =12 -> max_sum = 12

customers =   1 0 1 2 1 1 7 5     minutes = 3
grumpy    =   0 1 0 1 0 1 0 1
                  x x x
              cur = 12-0=12
customers =   1 0 1 2 1 1 7 5     minutes = 3
grumpy    =   0 1 0 1 0 1 0 1
                    x x x
              cur = 12 + 1 = 13 ->max_sum =13
customers =   1 0 1 2 1 1 7 5     minutes = 3
grumpy    =   0 1 0 1 0 1 0 1
                      x x x
              cur = 13-2 =11
customers =   1 0 1 2 1 1 7 5     minutes = 3
grumpy    =   0 1 0 1 0 1 0 1
                        x x x
             cur = 11 + 5 = 16 -> max_sum =16
'''
