# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        ll = head
        arr = [ll]
        while ll.next is not None:
            arr.insert(0,ll.next)
            ll = ll.next
        ll = arr[0]
        firstnode = ll
        for i in range(1, len(arr)):
            ll.next = arr[i]
            ll = ll.next
        ll.next = None
        return firstnode