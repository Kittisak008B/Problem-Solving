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

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # Constraints: arr[i] is a prime number for i > 0. 
        #              All the numbers of arr are unique and sorted in strictly increasing order.  -> fraction range [0 1]
        low , high = 0 , 1
        p , q = 0 , 0
        while low < high :
            mid = (low + high)/2
            count = 0  # num of fraction less than current mid
            maxF = 0   # maximum fraction less than current mid
            j = 1
            for i in range(len(arr)) :
                while j < len(arr) and arr[i]/arr[j] > mid :
                    j += 1
                if j >= len(arr) :
                    break
                count += len(arr) - j
                if arr[i]/arr[j] > maxF :
                    p , q = arr[i] , arr[j]
                    maxF = p/q
            if count == k :
                return [p,q]
            elif count > k :
                high = mid
            else :
                low = mid
              
