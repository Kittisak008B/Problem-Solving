# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).
# You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. 
# The difficulty of a day is the maximum difficulty of a job done on that day.
# You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].
# Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

# Example 1:
# Input: jobDifficulty = [6,5,4,3,2,1], d = 2
# Output: 7
# Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
# Second day you can finish the last job, total difficulty = 1.
# The difficulty of the schedule = 6 + 1 = 7 

# Example 2:
# Input: jobDifficulty = [9,9,9], d = 4
# Output: -1
# Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
  
# Example 3:
# Input: jobDifficulty = [1,1,1], d = 3
# Output: 3
# Explanation: The schedule is one job per day. total difficulty will be 3.

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        dp = {}
        def dfs(i , d , cur_maxjobDif) :
            if i == len(jobDifficulty) :
                return 0 if d == 0 else float('inf')
            if d == 0 :
                return float('inf')
            if (i , d , cur_maxjobDif) in dp :
                return dp[(i , d , cur_maxjobDif)]
            cur_maxjobDif = max(cur_maxjobDif , jobDifficulty[i])
            min_diff = min(dfs(i+1 , d , cur_maxjobDif) , cur_maxjobDif + dfs(i+1 , d-1 , float('-inf')) )
            dp[(i , d , cur_maxjobDif)] = min_diff
            return dp[(i , d , cur_maxjobDif)]
        return dfs(0 , d , float('-inf'))
'''
jobDifficulty = [6,5,4,3,2,1], d = 2

                 (i , d , max_jobDif)
                    ( 0 , 2 , 6)
         still same day/       \next day   
                   (1,2,6)       (1,1,-inf) 
                   /     \          /    \
                 (2,2,6)                  (2,0,-inf)
                 /     \                      inf
                (3,2,6)
                /      \ 
               (4,2,6)
               /   \ 6+dfs()
         (5,2,6)   (5,1,-inf)
         inf         /    \6+1+0=7
              (6,1,-inf)  (6,0,-inf) ->first day finish 5 jobs jobDif=6  second day finish 1 job jobDiff=1 #6+1=7
                inf           0      
'''
