# You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.
# For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].
# Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

# Example 1:
# Input: arr = [1,2,3,5], k = 3
# Output: [2,5]
# Explanation: The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
# The third fraction is 2/5.

# Example 2:
# Input: arr = [1,7], k = 1
# Output: [1,7]

# Constraints: arr[i] is a prime number for i > 0. All the numbers of arr are unique and sorted in strictly increasing order.

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # fraction range [0 1]
        low , high = 0 , 1
        p , q = 0 , 0
        while low < high :
            mid = (low+ high) / 2
            count = 0  # num of fraction not higher than current mid
            maxF = 0   # maximum fraction not higher than current mid
            j = 1
            for i in range(len(arr)-1) :
                while j < len(arr) and arr[i]/arr[j] > mid :
                    j += 1
                if j >= len(arr) :
                    break
                count += len(arr) - j
                if arr[i]/arr[j] > maxF :   
                    p , q = arr[i] , arr[j]
                    maxF = p / q
            if count == k :
                return [p , q]
            elif count > k :
                high = mid 
            else :
                low = mid
''' 
Ex.1   Input: arr = [1,2,3,5], k = 3

mid = 1/2
[1 2 3 5]
 i j       --> count += 4-1 =3 -> not higher than mid 1/2 : 1/2 1/3 1/5    maxF=1/2 (p=1 q=2)
   i   j   --> count += 4-3 =1 -> not higher than mid 1/2 : 2/5            maxF=1/2 same as above
     i   j --> break    totalcount = 3+1 = 4  

0  [1/5, 1/3, 2/5, 1/2, 3/5, 2/3]  1
low                mid            high
                   maxF
         k=3 < count --> high = mid = 1/2   new_mid =(0+1/2)/2 =1/4
-----------------------------------------
mid = 1/4
[1 2 3 5]
 i     j    --> count += 4-3 = 1 -> not higher than mid 1/4 : 1/5  maxF = 1/5 (p=1 q=5)
   i     j  --> break
   
   0   1/5  ,#1/4  1/3, 2/5, 1/2, 3/5, 2/3  1
   low        mid            high 

   totalcount = 1  < k  --> low =mid =1/4   new_mid = (1/4+1/2)/2 = 3/8
-----------------------------------------
mid = 3/8
[1 2 3 5]
 i   j     --> count += 4-2 = 2 -> not higher than mid 3/8 :1/3 1/5   maxF = 1/3
   i     j --> break
   totalcount = 2 < k --> low=mid = 3/8 new_mid = (3/8 + 1/2)/2 =7/16                                              
----------------------------------------
mid = 7/16 = 0.4375
[1 2 3 5]
 i   j    --> count += 4-2 = 2 -> not higher than mid 7/16 :1/3 1/5   maxF = 1/3
   i   j  --> count += 4-3 = 1 -> not higher than mid 7/16 :2/5       maxF = 2/5 (p=2 q=5)
     i   j--> break
   total count = 3 == k  -> return [p,q] = [2,5] 
'''
              
