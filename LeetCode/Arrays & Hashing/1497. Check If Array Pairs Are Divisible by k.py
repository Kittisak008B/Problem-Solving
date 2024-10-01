# Given an array of integers arr of even length n and an integer k.
# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k. 
# Return true If you can find a way to do that or false otherwise.

# Example 1:
# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

# Example 2:
# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).

# Example 3:
# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
 
# Constraints:
# arr.length == n
# 1 <= n <= 10**5
# n is even.
# -10**9 <= arr[i] <= 10**9
# 1 <= k <= 10**5
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = collections.defaultdict(int)
        for num in arr :
            remainder = k - (num%k)
            if d[remainder] > 0 :
                d[remainder] -= 1
            else :
                d[num%k] += 1
            #print(d)
        for num in d :
            if num != 0 and d[num] != 0 :
                return False
        return True
