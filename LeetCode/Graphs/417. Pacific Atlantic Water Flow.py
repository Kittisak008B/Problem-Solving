# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_queue , a_queue = collections.deque() , collections.deque()
        p_set , a_set = set() , set()
        rows , cols = len(heights) , len(heights[0])
        for row in range(rows) :
            p_queue.append((row , 0))
            p_set.add((row, 0))
        for col in range(1 , cols) :
            p_queue.append((0 , col))
            p_set.add((0 , col))
        for row in range(rows) :
            a_queue.append((row , cols-1))
            a_set.add((row , cols-1))
        for col in range(0 , cols-1) :
            a_queue.append((rows-1 , col))
            a_set.add((rows-1 , col))
        # print(p_queue)
        # print(p_set)
        # print(a_queue)
        # print(a_set)
        def bfs(queue , seen_set) :
            while queue :
                i , j = queue.popleft()
                for pos in [(0,1),(0,-1),(1,0),(-1,0)] :
                    next_i , next_j = i+pos[0] , j+pos[1]
                    if 0 <= next_i < rows and 0 <= next_j < cols and heights[next_i][next_j] >= heights[i][j] and (next_i , next_j) not in seen_set :
                        seen_set.add((next_i , next_j))
                        queue.append((next_i , next_j))
            return seen_set
        bfs(p_queue , p_set)
        bfs(a_queue , a_set)
        # print(p_set)
        # print(a_set)
        ans = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in p_set and (r, c) in a_set:
                    ans.append([r, c])
        return ans
      
