# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

# Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        i , j = 1 , max(piles)
        def k_check_hrs(mid) :
            hours = 0
            for pile in piles :
                hours += (pile + mid - 1) // mid
            return hours <= h

        while i <= j :
            k = (i+j) // 2
            if k_check_hrs(k) :
                j = k - 1
            else:
                i = k + 1
        return i
# piles = [3,6,7,11], h = 8
# k = 1 to 11 bananas per hours [1,2,3,4,5,6,7,8,9,10,11]

# k = 1,
# 3/1 + 6/1 + 7/1 + 11/1 = 3 + 6 + 7 + 11 = 27hrs > 8 hrs = Not enough time
# k = 2,
# 3/2 + 6/2 + 7/2 + 11/2 = 2 + 3 + 4 + 6 = 15 hrs > 8 hrs = Not enough time
# k = 3,
# 3/3 + 6/3 + 7/3 + 11/3 = 1+ 2+ 3 + 4 = 10hrs > 8 hrs = Not enough time
# k = 4,
# 3/4 + 6/4 + 7/4 + 11/4 = 1 + 2 + 2 + 3 = 8hrs = GOOD
# k = 5,
# 3/5 + 6/5 + 7/5 + 11/5 = 1 + 2 + 2 + 3 = 8hrs = GOOD, but not the minimum k
# k = 6,
# 3/6 + 6/6 + 7/6 + 11/6 = 1 + 1 + 2 + 2 = 4hrs = GOOD, but not the minimum k
# ... k = 11
# So the answer is k = 4 .
