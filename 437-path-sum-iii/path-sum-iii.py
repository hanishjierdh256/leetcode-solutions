# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        total = 0
        def bfscount(root, val):
            nonlocal total
            if (root is None):
                return
            val += root.val
            if (val == targetSum):
                total += 1
            bfscount(root.left, val)
            bfscount(root.right, val)
        def bfs(root):
            if (root is None):
                return 0
            else:
                bfscount(root, 0)
                return bfs(root.left) + bfs(root.right)
        bfs(root)
        return total

