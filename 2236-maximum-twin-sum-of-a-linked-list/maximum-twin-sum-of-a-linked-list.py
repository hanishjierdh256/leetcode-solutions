# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        if head is None:
            return 0
        ll = head
        arr = []
        while ll is not None:
            arr.append(ll.val)
            ll = ll.next
        n = len(arr)
        m = n // 2
        arr1 = arr[n-1:m-1:-1]
        for i in range(m):
            arr1[i] = arr1[i] + arr[i]
        return max(arr1)
