# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        s = None
        f = head.next.next

        while f:
            s = s.next if s else head
            if not f.next:
                break
            f = f.next.next

        prev = None
        curr = s.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        s.next = prev
        s = s.next

        p = head

        while p if not f else p.next.next:
            temp = p.next
            p.next = s
            p = s
            s = temp

     



        