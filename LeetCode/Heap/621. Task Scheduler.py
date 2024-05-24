# You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, 
# but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.
# ​Return the minimum number of intervals required to complete all tasks.

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
# After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

# Example 2:
# Input: tasks = ["A","C","A","B","D","B"], n = 1
# Output: 6
# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
# With a cooling interval of 1, you can repeat a task after just one other task.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        char_count = defaultdict(int)
        for char in tasks :
            if char not in char_count :
                char_count[char] = 0
            char_count[char] += 1
        max_heap = [-x for x in char_count.values()]
        heapq.heapify(max_heap)
        time = 0
        queue = collections.deque()
        while queue or max_heap :
            time += 1
            if max_heap :
                char_remain = heapq.heappop(max_heap) + 1
                if char_remain != 0 :
                    queue.append([char_remain , time + n])
            if queue and queue[0][1] == time :
                heapq.heappush(max_heap , queue.popleft()[0] )
        return time
'''
task = [A,A,A,B,B,B] n=2  
time  max_heap      queue  
0      -3 -3  
1         -3      [-2,3]              A
2                 [-2,3] [-2,4]       AB
3      -2                [-2,4]       AB_
4         -2      [-1,6]              AB_A
5                 [-1,6] [-1,7]       AB_AB
6      -1                [-1,7]       AB_AB_                 
7         -1                          AB_AB_A
8   --> return time                   AB_AB_AB
'''
