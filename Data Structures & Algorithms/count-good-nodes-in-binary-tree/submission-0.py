# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node, currmax):
            if not node:
                return
            nonlocal ans
            dfs(node.left, max(currmax, node.val))
            if node.val >= currmax:
                ans += 1
            dfs(node.right, max(currmax, node.val))
            
        dfs(root, root.val)
        return ans

            
