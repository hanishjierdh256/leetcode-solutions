# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head.next is None:
            return None
        n=0
        ln = head
        while ln is not None:
            n += 1
            ln = ln.next
        ln = head
        for i in range (n//2 - 1):
            ln = ln.next
        ln.next = ln.next.next
        return head
        