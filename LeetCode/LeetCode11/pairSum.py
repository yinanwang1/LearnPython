from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        max_sum = 0
        n = len(val_list)
        if 2 == n:
            return sum(val_list)

        for i in range(int(n / 2 )):
            max_sum = max(val_list[i] + val_list[n - i - 1], max_sum)

        return max_sum
