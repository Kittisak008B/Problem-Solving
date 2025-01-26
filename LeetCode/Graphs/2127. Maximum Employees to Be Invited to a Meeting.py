# A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.
# The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.
# Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, 
# return the maximum number of employees that can be invited to the meeting.

# Example 1:
#   1 <----> 2   <---3
#     table  ^
#           /
#          0
# Input: favorite = [2,2,1,2]
# Output: 3
# Explanation:
# The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
# All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
# Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
# The maximum number of employees that can be invited to the meeting is 3. 

# Example 2:
#   0 -------> 1
#   ^  table   |
#    \        /
#      -- 2 <-
# Input: favorite = [1,2,0]
# Output: 3
# Explanation: 
# Each employee is the favorite person of at least one other employee, and the only way the company can invite them is if they invite every employee.
# The seating arrangement will be the same as that in the figure given in example 1:
# - Employee 0 will sit between employees 2 and 1.
# - Employee 1 will sit between employees 0 and 2.
# - Employee 2 will sit between employees 1 and 0.
# The maximum number of employees that can be invited to the meeting is 3.

# Example 3:
# Input: favorite = [3,0,1,4,1]
# Output: 4
# Explanation:
# The above figure shows how the company will invite employees 0, 1, 3, and 4, and seat them at the round table.
# Employee 2 cannot be invited because the two spots next to their favorite employee 1 are taken.
# So the company leaves them out of the meeting.
# The maximum number of employees that can be invited to the meeting is 4.
 
# Constraints:
# n == favorite.length
# 2 <= n <= 10**5
# 0 <= favorite[i] <= n - 1
# favorite[i] != i

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # find max cycle length (Cycle with size > 2)
        def get_max_cycle_length(fav) :
            person_count = len(fav)
            max_cycle_length = 0
            visited = set()
            for i in range(person_count) :
                if i not in visited :
                    start_person = i
                    cur_visited = set()
                    cur_person = i
                    while cur_person not in visited : # try to find cycle
                        visited.add(cur_person)
                        cur_visited.add(cur_person)
                        cur_person = fav[cur_person]
                    # print('vistied :',visited)
                    # print('cur_visited :',cur_visited)
                    # print('cur_person :', cur_person)
                    if cur_person in cur_visited : # Cycle detected
                        cur_cycle_length = len(cur_visited)
                        while start_person != cur_person :
                            cur_cycle_length -= 1
                            start_person = fav[start_person]
                        max_cycle_length = max(max_cycle_length , cur_cycle_length)
            return max_cycle_length
          
        # find longest path ((Cycle with size == 2) + extended paths)
        def get_longest_path(fav) :
            def bfs(node , dest) :
                q = collections.deque([(node , 0)]) #node , length
                max_length = 0
                while q :
                    node , length = q.popleft()
                    if node != dest :
                        max_length = max(max_length , length)
                        for neighbor in d[node] :
                            q.append((neighbor , length + 1))
                return max_length
            #find cycle with size == 2 (a<-->b) pairs
            pairs = []
            visited = set()
            for i in range(len(fav)) :
                if i not in visited and fav[fav[i]] == i :
                    pairs.append((i , fav[i])) # a<-->b
                    visited.add(i)
                    visited.add(fav[i])
            #print(pairs)
            d = defaultdict(list)
            for node , destination in enumerate(fav) :
                d[destination].append(node)
            #print(d)
            longest_path = 0 
            for per1 , per2 in pairs :
                longest_path += 2 + bfs(per1 , per2) + bfs(per2 , per1) #(Cycle with size == 2) + extended paths
            return longest_path

        return max( get_max_cycle_length(favorite) , get_longest_path(favorite) )
