# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []
 
# Constraints:  lists[i] is sorted in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)) :
            if lists[i] :
                heapq.heappush(heap , (lists[i].val , i , lists[i]))
        dummy = ListNode()
        pointer = dummy
        while heap :
            val , i , node = heapq.heappop(heap)
            pointer.next = node 
            pointer = node
            if node.next :
                heapq.heappush(heap , (node.next.val , i , node.next))   
        return dummy.next    
'''
Input: lists = [[1,4,5],[1,3,4],[2,6]]   Output: [1,1,2,3,4,4,5,6]

heap = [(node.val , i , node)] = [(1,0,node1) (1,1,node1) (2,2,node2)]

dummy =ListNode()
pointer = dummy

heap = [(1,0,node1) (1,1,node1) (2,2,node2) (4,0,node4)]
           pop                                 push
dummy->node1
       pointer    

heap = [(1,1,node1) (2,2,node2) (3,1,node3) (4,0,node4)]
           pop                     push
dummy->node1->node1
                p     

heap = [(3,1,node3) (4,0,node4) (6,2,node6)]
dummy->node1->node1->node2
                       p    

heap = [(4,0,node4) (4,1,node4) (6,2,node6)]
dummy->node1->node1->node2->node3
                              p  
heap = [(4,1,node4) (5,0,node5) (6,2,node6)]
dummy->node1->node1->node2->node3->node4
                                     p   
heap = [(5,0,node5) (6,2,node6)]
dummy->node1->node1->node2->node3->node4->node4
                                            p  
heap = [(6,2,node6)]
dummy->node1->node1->node2->node3->node4->node4->node5
                                                   p
heap = []
dummy->node1->node1->node2->node3->node4->node4->node5->node6
                                                          p
'''
