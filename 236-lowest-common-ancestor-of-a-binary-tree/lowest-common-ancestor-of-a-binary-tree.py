# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def dfs (node):
            nonlocal ans
            if node is None:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            found = node is p or node is q
            if left + right + found >= 2:
                ans = node
            return left or right or found

        dfs(root)
        return ans


