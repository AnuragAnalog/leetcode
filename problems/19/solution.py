# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sp, fp = head, head

        for _ in range(n):
            fp = fp.next

        if fp == None:
            return head.next

        while fp.next != None:
            sp = sp.next
            fp = fp.next

        sp.next = sp.next.next

        return head
