# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def bfs(root, minNum) -> int:
            if (root is None):
                return 0
            if (root.val >= minNum):
                minNum = max(minNum,root.val)
                return 1 + bfs(root.left, minNum) + bfs(root.right, minNum)
            else:
                return bfs(root.left, minNum) + bfs(root.right, minNum)
        count = bfs(root, root.val)
        return count
