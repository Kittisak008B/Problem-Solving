# You are given two integers m and n, which represent the dimensions of a matrix.
# You are also given the head of a linked list of integers.
# Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), 
# starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
# Return the generated matrix.

# Example 1:
# 3->0->2->6->8
#             | 
# 5->0 -1 -1  1
# |           |
# 5<-2<-4<-9<-7
# Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
# Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
# Explanation: The diagram above shows how the values are printed in the matrix.
# Note that the remaining spaces in the matrix are filled with -1.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1]*n for _ in range(m)]
        left , right = 0 , n
        top , bottom = 0 , m
        while head :
            for i in range(left , right) : #left ->right 
                if not head :
                    return grid
                grid[top][i] = head.val
                head = head.next
            top += 1
            for i in range(top , bottom) : #top->bottom 
                if not head :
                    return grid
                grid[i][right -1] = head.val
                head = head.next
            right -= 1 
            for i in range(right-1 , left-1 ,-1) : #right ->left
                if not head :
                    return grid
                grid[bottom -1][i] = head.val
                head = head.next
            bottom -= 1
            for i in range(bottom-1 ,top-1 ,-1) : #bottom->top
                if not head :
                    return grid
                grid[i][left] = head.val
                head = head.next
            left += 1
        return grid
      
