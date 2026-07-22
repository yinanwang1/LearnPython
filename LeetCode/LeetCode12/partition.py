from typing import Optional


# 86. 分隔链表
# https://leetcode.cn/problems/partition-list/description/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_head = ListNode()
        big_head = ListNode()
        left = small_head
        right = big_head
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next

        right.next = None
        left.next = big_head.next

        return small_head.next

