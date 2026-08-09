# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minHeap, (lists[i].val, i , lists[i]))

        res = ListNode()
        curr = res

        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(minHeap, (node.val, i , node))

        return res.next

        