# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        output = []
        queue = deque([root])
        while queue: #while queue not empty
            level_size = len(queue) # size of queue from last pass
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    output.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return output