# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None: #if 0 or 1 length
            return head
        ll1 = head
        ll2 = head.next
        evenhead = head.next
        counter = 0
        while ll1.next is not None and ll2.next is not None:
            ll1.next = ll1.next.next
            ll2.next = ll2.next.next
            ll1 = ll1.next
            ll2 = ll2.next
        ll1.next = evenhead
        ll1 = head
        return ll1
        

            