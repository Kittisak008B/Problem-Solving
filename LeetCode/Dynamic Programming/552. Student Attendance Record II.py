# An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. 
# The record only contains the following three characters:
# 'A': Absent.
# 'L': Late.
# 'P': Present.
# Any student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

# Example 1:
# Input: n = 2
# Output: 8
# Explanation: There are 8 records with length 2 that are eligible for an award:
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

# Example 2:
# Input: n = 1
# Output: 3

# Constraints:    1 <= n <= 10**5

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        memo = [[[0]*3 for _ in range(2)] for _ in range(n+1)]
      
        def count(day , absent , late) :
            if day == n :
                return 1
            if memo[day][absent][late] != 0 :
                return memo[day][absent][late]
            total = 0
            total += count(day+1 , absent , 0) #Present.
            if absent + 1 < 2 :
                total += count(day+1 , absent+1 , 0) #Absent.
            if late + 1 < 3 :
                total += count(day+1 , absent , late+1) #Late. 
              
            memo[day][absent][late] = total % MOD
            return memo[day][absent][late]
          
        return count(0 , 0 , 0)
      
