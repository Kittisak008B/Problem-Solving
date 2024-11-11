# You are given a 0-indexed integer array nums of length n. You can perform the following operation as many times as you want:
# Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
# Return true if you can make nums a strictly increasing array using the above operation and false otherwise.
# A strictly increasing array is an array whose each element is strictly greater than its preceding element.

# Example 1:
# Input: nums = [4,9,6,10]
# Output: true
# Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
# In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
# After the second operation, nums is sorted in strictly increasing order, so the answer is true.
  
# Example 2:
# Input: nums = [6,8,11,12]
# Output: true
# Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.

# Example 3:
# Input: nums = [5,8,3]
# Output: false
# Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.
 
# Constraints:
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# nums.length == n

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def check_prime(n) :
            if n <= 1:  
                return False
            if n == 2:  
                return True
            for i in range(2 , int(sqrt(n)) + 1) :
                if n % i == 0 :
                    return False
            return True
        prime_arr = [False , False] #0 not prime , 1 not prime
        for x in range(2 , max(nums)) :
            if check_prime(x) :
                prime_arr.append(True)
            else :
                prime_arr.append(False)
        prev_val = 0
        for num in nums :
            biggest_prime = 0
            for x in range(num - prev_val -1 , 2 -1 , -1) :
                if prime_arr[x] :
                    biggest_prime = x
                    break
            if num - biggest_prime <= prev_val :
                return False
            prev_val = num - biggest_prime
        return True
      
