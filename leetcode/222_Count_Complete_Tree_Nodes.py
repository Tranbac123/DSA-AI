from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node, count):
            if node is None:
                return count
            left = dfs(node.left, count + 1)
            right = dfs(node.right, left)
            return right
        return dfs(root, 0)