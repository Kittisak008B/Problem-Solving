# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

# Example 1:
# Input: timePoints = ["23:59","00:00"]
# Output: 1

# Example 2:
# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0
 
# Constraints:
# 2 <= timePoints.length <= 2 * 10**4
# timePoints[i] is in the format "HH:MM".

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def to_minute(t) :
            h , m = map(int , t.split(':'))
            return h*60 + m
        times = [False]*60*24 #1440
        for t in timePoints :
            minute = to_minute(t)
            if times[minute] == True : 
                return 0
            times[minute] = True
        minutes = [i for i in range(1440) if times[i]]
        res = 1440
        for i in range(len(minutes)) :
            res = min(res , minutes[i] - minutes[i-1]) %1440
        return res
      
