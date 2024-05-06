# You are given the head of a linked list.
# Remove every node which has a node with a greater value anywhere to the right side of it.
# Return the head of the modified linked list.

# Example 1:
# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.

# Example 2:
# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pointer = dummy
        stack = []
        while pointer.next :
            while stack and stack[-1].val < pointer.next.val :
                stack.pop()
            stack.append(pointer.next)
            pointer = pointer.next
        #print(list(x.val for x in stack))

        dummy.next = stack[0]
        for i in range(1 , len(stack)) :
            stack[i-1].next = stack[i]
        stack[-1].next = None
        return dummy.next
      
