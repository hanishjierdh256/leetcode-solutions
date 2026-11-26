# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:      
        maxCount = 0  
        def dfscount(root, left_right):
            nonlocal maxCount
            rootLeft, rootRight = root.left, root.right
            leftCount, rightCount = 0, 0
            while(rootLeft is not None and left_right != 0):
                leftCount += 1
                rootLeft = rootLeft.right if (leftCount % 2 == 1) else rootLeft.left
            while(rootRight is not None and left_right != 1):
                rightCount += 1
                rootRight = rootRight.left if (rightCount % 2 == 1) else rootRight.right
            maxCount = max(maxCount, rightCount, leftCount)

        def dfs(root, left_right):
            if(root is None):
                return
            dfscount(root, left_right)
            dfs(root.left, 1) 
            dfs(root.right, 0)

        dfs(root,-1)
        return maxCount