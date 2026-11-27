# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:

        def find(root):
            if (root.val == val):
                return root
            if (root.val > val and root.left):
                return find(root.left)
            if (root.val < val and root.right):
                return find(root.right)
            return None

        return find(root)