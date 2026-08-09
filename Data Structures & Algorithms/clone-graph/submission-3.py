"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hm = {}

        def dfs(node):
            if node in hm:
                return hm[node]

            head = Node(node.val)
            hm[node] = head
            for nei in node.neighbors:
                head.neighbors.append(dfs(nei))

            return head

        return dfs(node) if node else None