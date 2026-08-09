# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        next = None
        prev = head.next

        while head.next is not None:
            head.next = next
            next = head
            head = prev
            prev = prev.next

        head.next = next

        return head

