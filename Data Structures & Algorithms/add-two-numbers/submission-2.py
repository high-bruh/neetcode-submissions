# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = l2  # Remember the head of l2 to return later
        prev = None  # To track the last valid node

        while l1 and l2:
            total = l1.val + l2.val + carry
            l2.val = total % 10
            carry = total // 10
            prev = l2
            l1 = l1.next
            l2 = l2.next

        if l1:
            prev.next = l1  # Append the rest of l1
            while l1:
                total = l1.val + carry
                l1.val = total % 10
                carry = total // 10
                prev = l1
                l1 = l1.next

        elif l2:
            while l2:
                total = l2.val + carry
                l2.val = total % 10
                carry = total // 10
                prev = l2
                l2 = l2.next

        if carry:
            prev.next = ListNode(carry)

        return head
