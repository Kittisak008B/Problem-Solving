# You are given an array of integers nums and the head of a linked list. 
# Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

# Example 1:
# Input: nums = [1,2,3], head = [1,2,3,4,5]
# Output: [4,5]
# Explanation: Remove the nodes with values 1, 2, and 3.

# Example 2:
# Input: nums = [1], head = [1,2,1,2,1,2]
# Output: [2,2,2]
# Explanation: Remove the nodes with value 1.

# Example 3:
# Input: nums = [5], head = [1,2,3,4]
# Output: [1,2,3,4]
# Explanation: No node has value 5.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pointer = dummy
        nums_set = set(nums)
        while pointer.next :
            if pointer.next.val in nums_set :
                pointer.next = pointer.next.next
            else :
                pointer = pointer.next
        return dummy.next
