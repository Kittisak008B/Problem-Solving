# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes. Return the head of the linked list after doubling it.

# Example 1:
# Input: head = [1,8,9]
# Output: [3,7,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.

# Example 2:
# Input: head = [9,9,9]
# Output: [1,9,9,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.

# Constraints:
# The number of nodes in the list is in the range [1, 104]     0 <= Node.val <= 9
# The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        while head :
            num = num*10 + head.val
            head = head.next
        num *= 2
        #print(num)

        digits = []
        if num == 0:
            digits = [0]
        while num > 0 :
            digits.append(num%10)
            num //= 10
        #print(digits)

        i = 0
        j = len(digits) - 1
        while i < j :
            digits[i] , digits[j] = digits[j] , digits[i]
            i += 1
            j -= 1
        #print(digits)

        dummy = ListNode()
        pointer = dummy
        for x in digits :
            pointer.next = ListNode(x)
            pointer = pointer.next
        
        return dummy.next
      
