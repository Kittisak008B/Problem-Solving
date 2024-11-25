# On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. 
# A move consists of choosing 0 and a 4-directionally adjacent number and swapping it. The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
# Given the puzzle board board, return the least number of moves required so that the state of the board is solved. 
# If it is impossible for the state of the board to be solved, return -1.

# Example 1:
# 1 2 3
# 4 _ 5
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
  
# Example 2:
# 1 2 3
# 5 4 _
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
  
# Example 3:
# 4 1 2 
# 5 _ 3
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
 
# Constraints:
# board.length == 2
# board[i].length == 3
# 0 <= board[i][j] <= 5
# Each value board[i][j] is unique.

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        neighbors = {0:[1,3] , 1:[0,2,4] , 2:[1,5] , 3:[0,4] , 4:[1,3,5] , 5:[2,4]}
        cur = ''.join(str(number) for row in board for number in row)
        queue = collections.deque([(cur , 0 , cur.index('0'))]) #current board , moves , index of 0
        visited = set([cur])
        while queue :
            cur_board , moves , idx_zero = queue.popleft()
            if cur_board == '123450' :
                return moves
            for nei in neighbors[idx_zero] :
                new_board_arr = list(cur_board)
                #swap '0' with neighbor
                new_board_arr[idx_zero] , new_board_arr[nei] = new_board_arr[nei] , new_board_arr[idx_zero]
                new_board_str = ''.join(new_board_arr)
                if new_board_str not in visited :
                    visited.add(new_board_str)
                    queue.append((new_board_str , moves +1 , nei))
        return -1
      
