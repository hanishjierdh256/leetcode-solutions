# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        total = 0
        def dfscount(root, val):
            nonlocal total
            if (root is None):
                return
            val += root.val
            if (val == targetSum):
                total += 1
            dfscount(root.left, val)
            dfscount(root.right, val)

        def dfs(root):
            if (root is None):
                return
            dfscount(root, 0)
            return dfs(root.left), dfs(root.right)

        dfs(root)
        return total

