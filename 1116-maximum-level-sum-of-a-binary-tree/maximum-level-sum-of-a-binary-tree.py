# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        queue = deque([root])
        output = None
        maxVal = []
        while queue:
            temp = None
            total = 0
            for i in range(len(queue)):
                temp = queue.popleft()
                total += temp.val
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            maxVal.append(total)
        return maxVal.index(max(maxVal))+1