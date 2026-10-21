# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeafArr(self, root:TreeNode | None, arr: list[int]) -> None:
        if root is None:
            return
        if root.left is None and root.right is None:
            arr.append(root.val)
            return
        self.getLeafArr(root.left, arr)
        self.getLeafArr(root.right, arr)


    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        arr1 = []
        arr2 = []
        self.getLeafArr(root1, arr1)
        self.getLeafArr(root2, arr2)
        n = len(arr1)
        m = len(arr2)
        return arr1 == arr2