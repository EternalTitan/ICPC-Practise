# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = None
        result_last = None
        carry_over = 0
        while l1 is not None or l2 is not None:
            l1_value = 0
            l2_value = 0
            if l1 is not None:
                l1_value = l1.val
            if l2 is not None:
                l2_value = l2.val
            sum = l1_value + l2_value + carry_over
            carry_over = sum // 10
            if result is None:
                result = ListNode(sum % 10)
                result_last = result
            else:
                result_last.next = ListNode(sum % 10)
                result_last = result_last.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry_over == 1:
            result_last.next = ListNode(1)
        return result

Solution().addTwoNumbers(
    ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
    ListNode(9, ListNode(9, ListNode(9))),
)