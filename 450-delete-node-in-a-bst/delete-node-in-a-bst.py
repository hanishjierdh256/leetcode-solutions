# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if root is None:
            return None
        
        if key < root.val: #traverse to left
            root.left = self.deleteNode(root.left, key)
        elif key > root.val: #traverse to right
            root.right = self.deleteNode(root.right, key)
        else: # found value
            #case 1 leaf node or 1 child node
            if not root.left: # catch leaf node or 1 left child node
                return root.right
            if not root.right: # catch 1 right child node
                return root.left
            #Case 2
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)

        return root