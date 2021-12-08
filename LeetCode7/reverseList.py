# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        p = head.next
        head.next = None
        while p is not None:
            t = p.next
            p.next = head
            head = p
            p = t

        return head
