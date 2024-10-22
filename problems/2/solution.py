# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getNumber(self, l1):
        curr = l1
        num = 0

        while curr is not None:
            num = num * 10 + curr.val
            curr = curr.next

        return num

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        n1 = self.getNumber(l1)
        n2 = self.getNumber(l2)

        n3 = n1 + n2
        dummy = ListNode(0)
        curr = dummy
        print(n1, n2, n3)

        if n3 == 0:
            return dummy

        while n3 > 0:
            curr.next = ListNode(n3 % 10)
            n3 //= 10
            curr = curr.next

        return dummy.next
